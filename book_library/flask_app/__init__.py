from flask import Flask
app = Flask(__name__)
app.secret_key = "what a ruddy mess"


from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)