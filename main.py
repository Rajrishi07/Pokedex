import pypokedex
from flask import Flask, render_template, request
#
# pokemon = pypokedex.get(name="Pikachu")
# stats = pokemon.BaseStats()
# print(pokemon.name)
# print(pokemon.hp)
# print(pokemon.abilities)
# print(pokemon.types[0])
# print(pokemon.height)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/Pokemon',methods=["post"])
def to_pokemon():
    pokemon_name = request.form['Pname']
    pokemon = pypokedex.get(name=pokemon_name)
    return render_template("pokemon.html", name=pokemon.name.capitalize())


if "__main__" == __name__:
    app.run(debug=True)