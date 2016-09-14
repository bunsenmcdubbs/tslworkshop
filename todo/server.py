from flask import Flask, send_from_directory
app = Flask(__name__)

@app.route("/hello/")
@app.route("/hello/<name>")
def hello(name="World"):
    return "Hello %s!" % name

@app.route("/")
@app.route("/<path:filepath>")
def index(filepath="index.html"):
    return send_from_directory("views", filepath)

if __name__ == "__main__":
    app.run()
