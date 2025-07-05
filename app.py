from flask import Flask, jsonify
from models import NOTES_DB, view_notes
# score 3/10
app = Flask(__name__)



def print_name(func):
   def wrapper():
      print ("Gian Rafael B. Roldan")
      return (func)
   return (wrapper)

@app.route('/')
def home():
    return "Home page!"

@app.route('/notes', methods=['GET'])
def get_notes():
    return jsonify(view_notes())

@app.route('/notes', methods=['DELETE'])
def Delete_notes():
    return jsonify(Delete_notes())

@app.route('/notes', methods=['PUT'])
def update_notes():
    return jsonify(update_notes())

@app.route('/notes', methods=['POST'])
def update_notes():
    return jsonify(view_notes())



app.run()

# @app.notes('/note', methods=['POST'])
# def post_note():
#     contents = request.json
#     new_note = add_note(contents["contents"], contents["created_date"])
#     return jsonify({"message": " added successfully!",
#     "data": new_note, "location" : f"note/{new_note['id']}"}), 201

# @app.notes('/note/<int:note_id>/<new_contents>/<new_created_date>', methods=['PUT'])
# def put_note(note_id, new_contents, new_created_date):
#     update_notess(note_id, new_contents, new_created_date)
#     update_notes = {'id': note_id,
#     'contents': new_contents,
#     'created_date': new_created_date}
#     return jsonify({"message": "Book updated successfully!",
#     "data": update_notes}), 200

# def search_book(note_id, note):
#     indexed_book = None
#     for note in note:
#         if note[0] == note_id:
#             indexed_book = {
#             "id": note[0],
#             "contents": note[1],
#             "created_date": note[2]
#             }
#             return indexed_book
        
# @app.notes('/note/<int:note_id>', methods=['GET','DELETE'])
# def manage_book(note_id):
#     indexed_book = search_book(note_id, view_notes())
#     if indexed_book is None:
#         return jsonify({"error": "Book not found"}), 404
#     if request.method =='DELETE':
#         delete_note(note_id)
#         return jsonify({"message": "Book Successfully Deleted"}), 200
#     return jsonify(indexed_book), 200

if __name__ == '__main__':
 app.run(debug = True)
