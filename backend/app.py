from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api")
def test():
    return jsonify("This message is from Backend!")
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)