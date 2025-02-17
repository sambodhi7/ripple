from flask import Flask 
from dotenv import load_dotenv, find_dotenv

import os

load_dotenv(find_dotenv())



print(os.environ.get("SECRET_KEY"))