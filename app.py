from models import create_database, add_note, view_notes, update_note, delete_note
from flask import Flask, jsonify
# score 7/10
import sqlite3
NOTES_DB = 'notes.db'
app = Flask(__name__)
NOTES_DB = 'notes.db'
def getName():
     print("Zane Raiden Mendoza")

getName()



@app.route('/notes') 
def get_notes(): 
  return view_notes()

get_notes()

@app.route('/notes/<id>', methods=['GET', 'DELETE'])
def delete_notes(id):
   return jsonify(delete_note(id))


@app.route('/notes/<id>/<mensahe>', methods=['PUT']) #hindi pa nagana
def put_note(mensahe):
   return jsonify(update_note(mensahe))

@app.route('/notes/<message>', methods=['POST']) #nagana
def post_note(message):
   return jsonify(add_note(message))


if __name__ == '__main__':
  app.run(debug=True)
