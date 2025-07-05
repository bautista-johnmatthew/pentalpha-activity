# 3 points
from flask import Flask, jsonify
from models import add_note, view_notes, update_note, delete_note

app = Flask(__name__)

@app.route('/notes', methods=['GET'])
# nilalagay ang route
def get_notes():
    return jsonify(view_notes())

def delete_note():
    return jsonify(delete_note())
    
def put_note():
    return jsonify(update_note())

def post_note():
    return jsonify(add_note())



app.run()

