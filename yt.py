from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello world!"

@app.route("/<yooo>")
def user(name):
    return "Hello " + name


if __name__ == "__main__":

    app.run()