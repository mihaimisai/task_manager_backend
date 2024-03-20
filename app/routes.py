from flask import jsonify, request
import app.firebase_utils
from firebase_admin import auth
from app import app

    
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        
        try:
            #if the email address already exists throw an error
            existing_user = auth.get_user_by_email(email)
            return jsonify('User already exists')
        except auth.UserNotFoundError:
            #if not, proceed to registering a new user
            try:
                user = auth.create_user(
                    email=email,
                    password=password)
                return jsonify('Succesfully created new user!')
            except Exception as e:
                return jsonify(str(e))
            
@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        data = request.json()
        email = data.get('email')
        password = data.get('password')
        
        try:
            # find the user with the email
            find_user = auth.get_user_by_email(email)
            print(find_user)
            #if the user exists check password
            #check_password
            return jsonify('User logged in succesfully!')
        except Exception as e:
            return jsonify(str(e))
            
            #if the user does not exists throw error
            
            #if the password is wrong send error
            #if email+password ok then loging and send confirmation
            
        