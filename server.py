from flask import Flask 
from dotenv import load_dotenv, find_dotenv
from datetime import timedelta
from mongoManager import MongoManager
from flask_cors  import cross_origin, CORS

import os

app = Flask(
    __name__,
    static_folder = './front-end/build',
    static_url_path = '/',
   
)

CORS(app)

mongoManager = MongoManager()

app.secret_key = os.environ.get("SECRET_KEY")
app.config['SESSION_PERMANENT'] = True
app.permanent_session_lifetime = timedelta(days=30)


@app.get("/home")
def home() :
    return app.send_static_file("index.html")

@app.route("/login/", methods=[ "POST"])
@cross_origin()
def loginPost(request):
    username = request.json['username']
    password = request.json['password']
    print(username, password)

if __name__ == '__main__':
    app.run(
        port=4001,
        debug=True
    )

