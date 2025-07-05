import os
from flask import Flask, jsonify
from models import add_note, view_notes, update_note, delete_note

app = Flask(__name__)

@app.route('/notes', methods=['GET'])
def get_notes():
    return jsonify(view_notes())

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
