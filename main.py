from flask import Flask
from app.router import router

app = Flask(__name__)
app.register_blueprint(router)

if __name__ == "__main__":
    app.run(debug=True) # To run the server, use the command: python app.py