import firebase_admin
from firebase_admin import credentials, firestore
import os

# Load Firebase credentials from environment variables
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

# Initialize Firebase app
firebase_admin.initialize_app(cred)
db = firestore.client()

def write_to_database(data):
    # Write data to Firestore database
    for entry in data:
        doc_ref = db.collection('users').document(entry['name'])
        doc_ref.set(entry)

def read_from_database():
    # Read data from Firestore database
    readDb = db.collection('users')
    docs = readDb.stream()
    return docs
