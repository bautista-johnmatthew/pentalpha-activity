from flask import Flask, jsonify, request
from models import create_database, view_notes, update_note, delete_note, add_note

app = Flask(__name__)

def add_name(func):
    def wrapper():
        print("Altheno!")
        return func()
    return wrapper


@app.route('/', methods = ['GET'])
@add_name
def home_page():
    return 'Home Page!'

@app.route("/notes", methods = ['GET'])
def get_notes():
    return jsonify(view_notes())

@app.route('/notes/id', methods=['POST'])
def post_note(id):
    return jsonify(add_note(id))

@app.route('/notes/<id>', methods = ['DELETE'])
def delete_notes(note):
    return jsonify(delete_note())

@app.route('/notes/<id>', methods = ['PUT'])
def put_notes(note):
    return jsonify(update_note())

@app.route("/notes/<id>", methods = ['GET'])
def search_note(id, notes):
    indexed_note = None

    for note in notes:
        if note[0] == id:
            indexed_note = {
                "contents": note[1],
                "created_date": note[2],
                "id": note[0]
            }

    return indexed_note

if __name__ == '__main__':
    app.run(debug=True)

