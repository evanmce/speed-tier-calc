from flask import render_template, session, redirect, url_for, current_app
from ..import db
from . import main
from ..models import Pokemon

@main.route('/', methods=['GET', 'POST'])
def index():
    pokemon = Pokemon.query.order_by(Pokemon.galar_dex).all()
    return render_template('index.html', pokemon=pokemon)