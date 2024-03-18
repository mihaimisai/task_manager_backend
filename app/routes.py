from flask import jsonify
from app import app
from app.firebase_utils import read_from_database

@app.route('/api')
def api():
    docs = read_from_database()
    for entry in docs:
        return jsonify({entry.id: entry.to_dict()})
