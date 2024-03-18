from flask import jsonify
from app import create_app
from app.firebase_utils import read_from_database

app = create_app()

@app.route('/api')
def api():
    docs = read_from_database()
    data = {entry.id: entry.to_dict() for entry in docs}
    return jsonify(data)
