import requests
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
            response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{poke_name}')
            data = response.json()
            pokeDict = {}
            pokemon = data['name']
            pokeDict[pokemon] = {
                'name' : data['forms'][0]['name'],
                'abilities' : data['abilities'][0]['ability']['name'],
                'base_exp' : data['base_experience'],
                'sprite' : data['sprites']['front_shiny'],
                'attack' : data['stats'][0]['base_stat'],
                'hp' : data['stats'][1]['base_stat'],
                'defense' : data['stats'][2]['base_stat']
                }
            return pokeDict
            db.session.add(pokemon)
            db.session.commit()
            return redirect(url_for('app.getPokeInfo'))
        else:
            print('Validation failed')
    else:
        print('GET request made')

    return render_template('pokemon.html', form = form)

