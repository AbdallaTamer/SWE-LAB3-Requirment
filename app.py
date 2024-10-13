from flask import Flask, jsonify
from routes.todo import todo_bp

app = Flask(__name__)

app.register_blueprint(todo_bp)

@app.route('/')
def index():
    return jsonify({"message": "Welcome to the Book Collection API!"})

if __name__ == '__main__':
    app.run(debug=True,port=5000)
