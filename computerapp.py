from flask import Flask, request, jsonify
from flask_sqlachemy import SQLAlchemy
from flask_marshmellow import Marshmellow
import os

#Init app
app = Flask(__name__)

#Run Server
if __name__ == '__main__':
    app.run(debug=True)