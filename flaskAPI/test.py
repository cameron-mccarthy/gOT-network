from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def test_func():
    return {'result' : 'Sucessful test'}

if __name__ == '__main__':
    app.run()