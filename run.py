from app import app


if __name__ == "__main__":
    # Run Flask app with Gunicorn
    app.run('0.0.0.0', debug=True)
