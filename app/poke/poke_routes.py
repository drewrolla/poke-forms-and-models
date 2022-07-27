from flask import Blueprint, render_template, request, redirect, url_for
from .forms import UserCreationForm

from app.models import Poke

poke = Blueprint('poke', __name__, template_folder='poketemplates')

from app.models import db

@poke.route('/pokeinfo')
def getPokeInfo():
    return render_template('pokeinfo.html')

@poke.route('/pokemon', methods=["GET", "POST"])
def getPokemon():
    form = UserCreationForm()
    if request.method == "POST":
        print('Post request made.')
        if form.validate():
            poke_name = form.poke_name.data

            print(poke_name)

            pokemon = Poke(poke_name)

            db.session.add(pokemon)
            db.session.commit()

            return redirect(url_for('app.getPokeInfo'))
        else:
            print('Validation failed')
    else:
        print('GET request made')

    return render_template('pokemon.html', form = form)

