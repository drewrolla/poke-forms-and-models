import requests
from flask import Blueprint, redirect, render_template, request, url_for, flash
from flask_login import current_user, login_required
from app.save_poke.forms import SavePokemon
from .forms import SavePokemon
from app.models import PokeTeam, db

save_poke = Blueprint('save_poke', __name__, template_folder='savetemplates')

@save_poke.route('/save_poke', methods=["GET", "POST"])
@login_required
def savedPokemon():
    form = SavePokemon()
    if request.method == "POST":
        if form.validate():
            pokemon1 = form.pokemon1.data
            pokemon2 = form.pokemon2.data
            pokemon3 = form.pokemon3.data            
            pokemon4 = form.pokemon4.data
            pokemon5 = form.pokemon5.data

            team = PokeTeam(pokemon1, pokemon2, pokemon3, pokemon4, pokemon5, current_user.id)

            db.session.add(team)
            db.session.commit()
            flash('Saved Pokemon team', 'success')
        else:
            flash('Error saving team. Please try again!', 'error')
    return render_template('savePoke.html', form=form)


# Need to figure this portion out as well (aka show the saved team)
@save_poke.route('/roster', methods=["GET", "POST"])
def showRoster():
#     form = SavePokemon()
#     roster = PokeTeam.query.all()
#     my_dict = {}
#     if request.method == "POST":
#         print('Post request made.')
#         if form.validate():
#             poke_name = form.poke_name.data
#             url = f"https://pokeapi.co/api/v2/pokemon/{poke_name}"
#             res = requests.get(url)
#             if res.ok:
#                 data = res.json()
#                 my_dict = {
#                     'name': data['name'],
#                     'ability': data['abilities'][0]['ability']['name'],
#                     'img_url': data['sprites']['front_shiny'],
#                     "hp": data['stats'][0]['base_stat'],
#                     'attack': data['stats'][1]['base_stat'],
#                     'defense': data['stats'][2]['base_stat']
#                 }
#     return render_template('roster.html', roster=roster, pokemon=my_dict)
    return render_template('roster.html')



# unsure if I want to add this yet
@save_poke.route('/save_poke/edit', methods=["GET", "POST"])
def editRoster():
    form = SavePokemon()
    newRoster = PokeTeam.query.filter_by(user_id=current_user.id).first()
    if current_user.id != newRoster.user_id:
        flash('You are not allowed to update another user\s team!', 'danger')
        return redirect(url_for('save_poke.showRoster'))
    if request.method=="POST":
        if form.validate():
            pokemon1 = form.pokemon1.data
            pokemon2 = form.pokemon2.data
            pokemon3 = form.pokemon3.data
            pokemon4 = form.pokemon4.data
            pokemon5 = form.pokemon5.data
            newRoster.pokemon1 = pokemon1
            newRoster.pokemon2 = pokemon2
            newRoster.pokemon3 = pokemon3
            newRoster.pokemon4 = pokemon4
            newRoster.pokemon5 = pokemon5
            db.session.commit()
        return redirect(url_for('save_poke.showRoster'))
    return render_template('savePoke.html', form=form, newRoster=newRoster)