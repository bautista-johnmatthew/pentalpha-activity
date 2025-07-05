# MORALES: 3 points
from flask import Flask, jsonify
from models import add_note, view_notes, update_note, delete_note

app = Flask(__name__)

@app.route('/notes', methods=['GET'])
def get_notes():
    return jsonify(view_notes())


app.run()

