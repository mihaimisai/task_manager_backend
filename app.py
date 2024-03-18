from flask import Flask, jsonify
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access environment variables
DATABASE_KEY = os.getenv("DATABASE_KEY")

app = Flask(__name__)

# Use a service account.
try:
    cred = credentials.Certificate({
    "type": os.getenv("FIREBASE_TYPE"),
    "project_id": os.getenv("FIREBASE_PROJECT_ID"),
    "private_key_id": os.getenv("FIREBASE_PRIVATE_KEY_ID"),
    "private_key": os.getenv("FIREBASE_PRIVATE_KEY"),
    "client_email": os.getenv("FIREBASE_CLIENT_EMAIL"),
    "client_id": os.getenv("FIREBASE_CLIENT_ID"),
    "auth_uri": os.getenv("FIREBASE_AUTH_URI"),
    "token_uri": os.getenv("FIREBASE_TOKEN_URI"),
    "auth_provider_x509_cert_url": os.getenv("FIREBASE_AUTH_PROVIDER_X509_CERT_URL"),
    "client_x509_cert_url": os.getenv("FIREBASE_CLIENT_X509_CERT_URL"),
    "universe_domain": os.getenv("FIREBASE_UNIVERSE_DOMAIN")
})
    firebase_admin.initialize_app(cred)
    db = firestore.client()
except Exception as e:
    print("Error initializing Firebase:", e)

Obj1 = {
    'name' : 'Mihai',
    'date' : '18.03.2024',
    'message' : 'I am creating my own task management app!!!'
}

data = [Obj1]
    
#Writing to database
for entry in data:
    doc_ref = db.collection('users').document(entry['name'])
    doc_ref.set(entry)
    
#Reading from database
readDb = db.collection('users')
docs = readDb.stream()
    
@app.route('/api')
def api():
    for entry in docs:
        return print(f"{entry.id} => {entry.to_dict()}")
    
