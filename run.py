from app import app

if __name__ == "__main__":
    # Run Flask app with Gunicorn
    app.run(host='0.0.0.0', port=5000)
