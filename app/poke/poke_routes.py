from flask_login import login_required, current_user
import requests
from flask import Blueprint, render_template, request, redirect, url_for
from .forms import PokemonSearchForm, Catch, Run
from app.models import Pokedex, db, User, pokemans
from psycopg2 import IntegrityError

poke = Blueprint('poke', __name__, template_folder='poketemplates')

@poke.route('/pokemon', methods=["GET", "POST"])
def getPokemon():
    form = PokemonSearchForm()
    my_dict = {}
    poke_name = form.poke_name.data
    try:
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
                        'hp': data['stats'][0]['base_stat'],
                        'attack': data['stats'][1]['base_stat'],
                        'defense': data['stats'][2]['base_stat']
                    }
                    # this might work to make it so that the pokemon can be saved to the db
                    pokedex = Pokedex(poke_name, my_dict['ability'], my_dict['img_url'], my_dict['hp'], my_dict['attack'], my_dict['defense'])

                    db.session.add(pokedex)
                    db.session.commit()
                    return render_template('pokemon.html', form=form, pokemon=my_dict)
    except:
            IntegrityError
            db.session.rollback()
            return render_template('pokemon.html', form = form, pokemon = my_dict)
    return render_template('pokemon.html', form = form, pokemon = my_dict)


@poke.route('/pokemon/catch<id>', methods=["GET", "POST"])
@login_required
def catchPoke():
    form = Catch()
    if request.method=="POST":
        pokemon = id
        caughtpoke = pokemans(pokemon)

        db.session.add(caughtpoke)
        db.session.commit()

    return render_template('pokemon.html', form=form)

@poke.route('/pokemon/run<id>', methods = ["GET", "POST"])
@login_required
def runaway():
    form = Run()
    if request.method=="POST":
        wildpoke = id
        runfromwild = pokemans(wildpoke)

        db.session.add(wildpoke)
        db.session.commit()

    return render_template('pokemon.html', form=form)

# @poke.route('/release/<int:pokemon_id>')
# @login_required
# def releasePoke(pokemon_id):
#     user = User.query.get(pokemon_id)
#     current_user.release(user)
#     return redirect(url_for('pokemon'))