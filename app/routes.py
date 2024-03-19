from flask import jsonify
from app.firebase_utils import read_from_database
from app import app


@app.route('/api')
def api():
    docs = read_from_database()
    for entry in docs:
        return jsonify({entry.id: entry.to_dict()})
@app.route('/')
def index():
    return 'Hello World'