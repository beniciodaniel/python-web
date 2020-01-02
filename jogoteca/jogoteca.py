from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = "randomtestsecretkey"

class Game:
    def __init__(self, name, category, console):
        self.__name = name
        self.__category = category
        self.__console = console

    @property
    def name(self):
        return self.__name

    @property
    def category(self):
        return self.__category

    @property
    def console(self):
        return self.__console

game1 = Game('Final Fantasy VII', 'RPG', 'PS1')
game2 = Game('Final Fantasy VI', 'RPG', 'SNES')
game3 = Game('Donkey Kong 2', 'Action', 'SNES')
list = [game1, game2, game3]

@app.route("/")
def index():
    return render_template('index.html', title="Games", games=list)

@app.route("/create")
def create():
    return render_template('create.html', title="New Game")

@app.route("/store", methods=['POST',])
def store():
    name = request.form['name']
    category = request.form['category']
    console = request.form['console']

    game = Game(name, category, console)
    list.append(game)

    return redirect('/')


@app.route("/login")
def login():
    return render_template("login.html", title="Login")

@app.route("/authenticate", methods=["POST",])
def authenticate():
    if 'masterkey' == request.form['password']:
        session['logged_user'] = request.form['username']
        flash(request.form['username'] + ' successfully logged in!')
        return redirect('/')
    else:
        flash('Username or Password invalid. Please, try again.')
        return redirect('/login')

app.run(debug=True)
