from flask import Blueprint, render_template, render_template_string, request, redirect
from app.models import Poke
save_poke = Blueprint('save_poke', __name__, template_folder='savetemplates')
from app.models import db

@save_poke.route('/save_poke', methods=["GET", "POST"])
def savedPokemon():
    if request.method == "POST":
        print('Post request made.')
    return render_template('savePoke.html')