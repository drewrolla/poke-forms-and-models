import requests
from flask import Blueprint, redirect, render_template, request, url_for, flash
from flask_login import current_user, login_required
from app.save_poke.forms import SavePokemon
from .forms import SavePokemon
from app.models import PokeTeam, db, User
from app.poke.savePokemon import savePokemon

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
# does not show saved roster
@save_poke.route('/roster', methods=["GET", "POST"])
def showRoster():
    savedPokes = []
    thing = []
    form = SavePokemon()
    roster = PokeTeam.query.all()
    my_dict = {}
    if request.method == "POST":
        print('Post request made.')
        if form.validate():
            savePoke = form.pokemon1.data
            saved = savePokemon(savePoke)
            x = saved[0][savePoke]
            pokemon1 = x['Name']

            for poke in savedPokes:
                saved = savePokemon(poke)
                x = saved[0][poke]
                savedPokes.append(x)
            
            thing = PokeTeam(pokemon1)

    return render_template('roster.html', roster=roster, pokemon=my_dict, thing=thing, savedPokes=savedPokes)


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

# @save_poke.routes('/savePokemon/<int:pokemon_id>')
# @login_required
# def savePokemon(pokemon_id):
#     pokemon = PokeTeam.query.get(pokemon_id)
#     current_user.follow(pokemon_id)
#     return redirect(url_for('home'))

# @save_poke.routes('/unsavePokemon/<int:pokemon_id>')
# @login_required
# def unsavePokemon(pokemon_id):
#     pass