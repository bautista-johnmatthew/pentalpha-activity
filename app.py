# 3 points
from flask import Flask, jsonify, request
from models import add_note, view_notes, update_note, delete_note

app = Flask(__name__)

# GET - View all notes
@app.route('/notes', methods=['GET'])
def get_notes():
    return jsonify(view_notes())

# POST - Create a new note
@app.route('/notes/<content>', methods=['POST'])
def create_note(content):
    new_note = add_note(content)
    return jsonify(new_note), 201

# PUT - Update a note
@app.route('/notes', methods=['PUT'])
def modify_note():
    contents = request.json
    updated_note = update_note(contents["id"], contents["new_content"])
    return jsonify(updated_note)

# DELETE - Delete a note
@app.route('/notes/<int:id>', methods=['DELETE'])
def remove_note(id):
    result = delete_note(id)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
