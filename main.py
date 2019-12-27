from flask import Flask
from flask_cors import CORS
from apis import api

app = Flask(__name__)
api.init_app(app)
CORS(app)

if __name__ == '__main__':
    app.run(port=5002)
