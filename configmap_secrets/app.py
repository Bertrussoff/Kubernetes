from flask import Flask
import os
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    db_url = os.getenv('DATABASE_URL')
    db_username = os.getenv('DB_USERNAME')
    db_password = os.getenv('DB_PASSWORD')

    # Simulate database connection (you would replace this with actual connection code)
    db_connection = mysql.connector.connect(
        host=db_url.split('/')[2].split(':')[0],
        user=db_username,
        password=db_password
    )

    return f'Connected to database at {db_url} with user {db_username}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
