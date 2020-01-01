from flask import Flask, render_template

app = Flask(__name__)

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

@app.route("/index")
def index():

    game1 = Game('Final Fantasy VII', 'RPG', 'PS1')
    game2 = Game('Final Fantasy VI', 'RPG', 'SNES')
    game3 = Game('Donkey Kong 2', 'Action', 'SNES')

    list = [game1, game2, game3]
    return render_template('list.html', title="Games", games=list)


app.run()
