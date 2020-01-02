from flask import Flask, render_template, request, redirect, session, flash, url_for

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


class User:
    def __init__(self, id, username, password):
        self.__id = id
        self.__username = username
        self.__password = password

    @property
    def id(self):
        return self.__id

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password


user1 = User('beni', 'Benicio Daniel', '1234')
user2 = User('doe', 'John Doe', '4321')
user3 = User('jw', 'Jose', 'ericclapton')
users = {user1.id: user1,
         user2.id: user2,
         user3.id: user3}

game1 = Game('Final Fantasy VII', 'RPG', 'PS1')
game2 = Game('Final Fantasy VI', 'RPG', 'SNES')
game3 = Game('Donkey Kong 2', 'Action', 'SNES')
list = [game1, game2, game3]


@app.route("/")
def index():
    return render_template('index.html', title="Games", games=list)


@app.route("/create")
def create():
    if 'logged_user' not in session or session['logged_user'] == None:
        return redirect(url_for('login', next=url_for('create')))
    return render_template('create.html', title="New Game")


@app.route("/store", methods=['POST',])
def store():
    name = request.form['name']
    category = request.form['category']
    console = request.form['console']

    game = Game(name, category, console)
    list.append(game)

    return redirect(url_for('index'))


@app.route("/login")
def login():
    next = request.args.get('next')
    return render_template("login.html", title="Login", next=next)


@app.route("/authenticate", methods=["POST",])
def authenticate():

    if request.form['username'] in users:
        user = users[request.form['username']]
        if user.password == request.form['password']:
            session['logged_user'] = user.id
            flash(user.username + ' successfully logged in!')
            next_page = request.form['next']
            return redirect(next_page)

    else:
        flash('Username or Password invalid. Please, try again.')
        return redirect(url_for('login'))


@app.route("/logout")
def logout():
    session['logged_user'] = None
    flash('User not logged in!')
    return redirect(url_for('index'))


app.run(debug=True)
