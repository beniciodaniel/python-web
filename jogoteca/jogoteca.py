from flask import Flask

app = Flask(__name__)

@app.route("/start")
def hi():
    return "<h1>Hello, Flask</h1>"

app.run()