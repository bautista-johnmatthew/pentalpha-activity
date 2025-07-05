from flask import Flask, jsonify
from models import view_notes, add_note, update_note, delete_note

app = Flask(__name__)

def add_name(func):
    def wrapper():
        print("Ernesto Bernas III")
        return func()
    return wrapper

@app.route("/")
@add_name
def homepage():
    return "Home Page!"

@app.route("/notes", methods = ['GET'])
def get_notes():
    return jsonify(view_notes())
    
@app.route("/notes/<contents>", methods = ['POST'])
def post_note():
    return jsonify(add_note())
    
@app.route("/notes/<id>", methods = ['DELETE'])
def delete_notes():
    return jsonify(delete_note())
    
@app.route("/notes/<id>", methods = ['PUT'])
def put_notes():
    return jsonify(update_note())

if __name__ == "__main__":
    app.run(debug=True)