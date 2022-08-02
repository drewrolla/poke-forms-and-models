from flask_login import login_required, current_user
import requests
from flask import Blueprint, render_template, request, redirect, url_for
from .forms import PokemonSearchForm
from app.models import PokeTeam, db, User

poke = Blueprint('poke', __name__, template_folder='poketemplates')

@poke.route('/pokemon', methods=["GET", "POST"])
def getPokemon():
    form = PokemonSearchForm()
    my_dict = {}

    if request.method == "POST":
        print('Post request made.')
        if form.validate():
            poke_name = form.poke_name.data

            url = f"https://pokeapi.co/api/v2/pokemon/{poke_name}"
            res = requests.get(url)
            if res.ok:
                data = res.json()
                my_dict = {
                    'name': data['name'],
                    'ability': data['abilities'][0]['ability']['name'],
                    'img_url': data['sprites']['front_shiny'],
                    "hp": data['stats'][0]['base_stat'],
                    'attack': data['stats'][1]['base_stat'],
                    'defense': data['stats'][2]['base_stat']
                }


    return render_template('pokemon.html', form=form, pokemon=my_dict)

@poke.route('/catch/<int:pokemon_id>')
@login_required
def catchPoke(pokemon_id):
    user = User.query.get(pokemon_id)
    current_user.catch(user)
    return redirect(url_for('pokemon'))


@poke.route('/release/<int:pokemon_id>')
@login_required
def releasePoke(pokemon_id):
    user = User.query.get(pokemon_id)
    current_user.release(user)
    return redirect(url_for('pokemon'))