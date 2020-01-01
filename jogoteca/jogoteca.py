from flask import Flask, render_template

app = Flask(__name__)


@app.route("/start")
def hi():
    return render_template('list.html')


app.run()
