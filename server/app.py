from flask import Flask, jsonify
from flask_cors import CORS


# Config
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enagle CORS
CORS(app)

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


if __name__ == '__main__':
    app.run()
