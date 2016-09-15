from flask import Flask, send_from_directory
app = Flask(__name__)

@app.route("/hello/")
@app.route("/hello/<name>")
def hello(name="Michelle"):
    return "Hello %s!" % name

@app.route("/")
@app.route("/<path:filepath>")
def index(filepath="index.html"):
    return send_from_directory("", filepath)

if __name__ == "__main__":
    app.run(debug=True)
