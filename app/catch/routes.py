from sqlite3 import dbapi2
from flask import Blueprint, render_template, request, url_for, redirect
from flask_login import current_user, login_required
from app.models import Team
from .forms import CatchPokeForm

catch = Blueprint('catch', __name__, template_folder='templates_catch')

@catch.route('/catch/<pokemon_id>', methods=["GET", "POST"])
@login_required
def catchPoke(pokemon_id):
    T = Team(current_user.id, pokemon_id)
    T.saveToDB()

    return redirect(url_for("SearchPokemon"))



