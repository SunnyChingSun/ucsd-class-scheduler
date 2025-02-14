from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Hello, UCSD Enrollment System!"})

if __name__ == '__main__':
    app.run(debug=True)

