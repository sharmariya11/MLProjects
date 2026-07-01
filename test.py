from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello"

print("Before app.run")

app.run(host="127.0.0.1", port=5000, debug=False)

print("After app.run")