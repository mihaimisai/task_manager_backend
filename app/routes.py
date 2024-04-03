from flask import jsonify, request
from app.firebase_utils import db, auth
from app import app
#from datetime import datetime, timedelta

# Allow for a tolerance of 5 minutes for token validation
#ALLOWED_SKEW = timedelta(minutes=5)


@app.route('/add_data', methods=['GET', 'POST'])
def add_data():
    try:
        id_token = request.headers.get("Authorization").split(" ")[1]
        decoded_token = auth.verify_id_token(id_token)
        uid = decoded_token['uid']
        doc_ref = db.collection("users").document(uid)
        data = request.json()
        print(data)
        
        return jsonify('added')
    except Exception as e:  # Catch all exceptions
        return jsonify(str(e))
    
@app.route("/get_user_data", methods=["GET"])
def get_user_data():
    try:
        id_token = request.headers.get("Authorization").split(" ")[1]
        # Verify the ID token while checking if the token is revoked by
        # passing check_revoked=True.
        decoded_token = auth.verify_id_token(id_token)
        #print(decoded_token)
        #issuance_time = datetime.utcfromtimestamp(decoded_token['iat'])
        #current_time = datetime.utcnow()
        #time_difference = current_time - issuance_time
        #print(time_difference)
        #if time_difference > ALLOWED_SKEW:
           # print ("Token used too early")
        
        # Token is valid and not revoked.
        uid = decoded_token['uid']
        user_data = db.collection('users').document(uid)
        user_data = user_data.get().to_dict()
        return jsonify(user_data)
        
    except auth.RevokedIdTokenError as e:
        # Token revoked, inform the user to reauthenticate or signOut().
        return jsonify('RevokedIdTokenError')
    except auth.UserDisabledError as e:
        # Token belongs to a disabled user record.
        return jsonify('UserDisabledError')
    except auth.InvalidIdTokenError as e:
        # Token is invalid
        return jsonify('InvalidIdTokenError')
    except Exception as e:
        return jsonify(str(e))