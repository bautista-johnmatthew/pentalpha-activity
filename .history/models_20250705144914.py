import sqlite3

NOTES_DB = 'notes.db'

# A decorator is a function na nag execute before another function
# So this decorator makes sure the database is created before any function call
def create_database(func):
    """Decorator to create a database if it doesn't exist."""

    # This wrapper is the actual functionality that will be executed
    # when the decorated function 'create_database' is attached
    def wrapper(*args, **kwargs):
        print("Creating database if it doesn't exist...")
        conn = sqlite3.connect(NOTES_DB)
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS notes '
                + '(id INTEGER PRIMARY KEY, contents TEXT, '
                + 'created_date DATE DEFAULT (datetime(\'now\')))')
        conn.commit()
        conn.close()
        return func(*args, **kwargs)
    
    return wrapper

@create_database
def add_note(note):
    """Function to add a note to the database."""
    print("Adding note to the database...")
    conn = sqlite3.connect(NOTES_DB)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO notes (contents) VALUES (?)', (note,))

     # Get the ID of the newly inserted note
    new_note_id = cursor.lastrowid
    cursor.execute("SELECT * FROM notes WHERE id = ?", (new_note_id,))
    new_note = cursor.fetchone()
    conn.commit()
    conn.close()

    return {
        "id": new_note[0],
        "contents": new_note[1],
        "created_date": new_note[2]
    }

@create_database
def view_notes():
    # """Function to view all notes in the database."""
    print("Retrieving notes from the database...")
    conn = sqlite3.connect(NOTES_DB)
    cursor = conn.execute('SELECT * FROM notes')
    notes = cursor.fetchall()
    conn.close()

    formatted_notes = []
    for note in notes:
        dict_note = {
            "id": note[0],
            "contents": note[1],
            "created_date": note[2]
        }
        formatted_notes.append(dict_note)

    return formatted_notes

@create_database
def update_note(id, new_contents):
    conn = sqlite3.connect(NOTES_DB)
    cursor = conn.cursor()
    success = cursor.execute('UPDATE notes SET contents = ? WHERE id = ?', (new_contents, id))
    conn.commit()
    conn.close()

    if success.rowcount == 0:
        return {"error": f"Note with ID {id} does not exist."}

    return {
        "message": f"Note with ID {id} has been updated.",
        "new_contents": new_contents
    }

@create_database
def delete_note(id):
    """ Function to delete a note from the database by ID."""
    conn = sqlite3.connect(NOTES_DB)
    cursor = conn.cursor()
    success = cursor.execute('DELETE FROM notes WHERE id = ?', (id,))
    conn.commit()
    conn.close()

    if success.rowcount == 0:
        return {"error": f"Note with ID {id} does not exist."}

    return {"message": f"Note with ID {id} has been deleted."}




