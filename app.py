from flask import Flask, jsonify, request
from models import create_database, add_note, view_notes
from models import update_note, delete_note

# score: 4/10

app = Flask(__name__)

def print_name(func):
    def wrapper():
        print("Abrianne Buenacifra ")
        return func()
    return wrapper

@app.route('/')
@print_name
def home():
    return "Home Page!"

@app.route('/notes', methods=['GET'])
def get_notes():
    return jsonify(view_notes())

@app.route('/notes', methods=['POST'])
def post_note():
    return jsonify(add_note())

@app.route('/notes/<int:id>/<new_contents>', methods=['PUT'])
def put_note():
    return jsonify(update_note())
        
@app.route('/notes/<int:id>', methods=['GET','DELETE'])
def manage_note():
    return jsonify(delete_note())

if __name__ == '__main__':
    app.run(debug = True)