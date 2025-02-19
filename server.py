from flask import Flask 
from dotenv import load_dotenv, find_dotenv
from datetime import timedelta

import os

app = Flask(
    __name__,
    static_folder = './static',
    static_url_path = '/',
   
)

app.secret_key = os.environ.get("SECRET_KEY")
app.config['SESSION_PERMANENT'] = True
app.permanent_session_lifetime = timedelta(days=30)


@app.get("/home")
def home() :
    return "Welcome to the home page"

if __name__ == '__main__':
    app.run(
        port=4001,
        debug=True
    )

