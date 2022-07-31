from flask import Blueprint, render_template, request, flash
from flask_login import current_user, login_required
from app.save_poke.forms import SavePokemon
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

# @save_poke.route('/save_poke')
# def showSavedPokemon():
#     team = PokeTeam.query.all() # might have to edit this to show user's specific Pokemon team
#     return render_template('showSavedPoke.html', team=team)


# Need to figure this portion out as well (aka show the saved team)
@save_poke.route('/save_poke', methods=["GET", "POST"])
def showPokeTeam(team_id):
    team = PokeTeam.query.get(team_id)
    return render_template('savePoke.html', team=team)

# unsure if I want to add this yet
@save_poke.route('/save_poke/remove', methods=["GET", "POST"])
def removePokemon():
    return render_template('savePoke.html')