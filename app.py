# CORPUS: 3 points

from flask import Flask, request, jsonify
from models import view_notes

app = Flask(__name__)

@app.route('/notes', methods=['GET'])
def get_note():
    return jsonify(view_notes())


app.run(host="0.0.0.0", port=10000, debug=True)