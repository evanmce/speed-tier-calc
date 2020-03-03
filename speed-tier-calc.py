import json
import os

import click
from flask_migrate import Migrate

from app import create_app, db
from app.models import Pokemon

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)

@app.cli.command("initdb")
def initdb_command():
    db.drop_all()
    db.create_all()

    pkmn = []
    with open('app/assets/pokemon.json') as f:
        data = json.load(f)
        for p in data:
            id_no = p['id']
            name = p['name']
            stage = p['stage']
            galar_dex = p['galar_dex']
            base_stats = p['base_stats']
            abilities = list(set(p['abilities']))
            types = p['types']
            level_up_moves = p['level_up_moves']
            egg_moves = p['egg_moves']
            tms = p['tms']
            trs = p['trs']
            mon = Pokemon(id_no, name, stage, galar_dex, base_stats, abilities,
                          types, level_up_moves, egg_moves, tms, trs)
            if id_no < 100:
                id_no = "0{}".format(id_no)
            mon.set_image_url('https://www.serebii.net/pokedex-swsh/icon/{}.png'.format(id_no))
            pkmn.append(mon)

    for p in pkmn:
        db.session.add(p)

    db.session.commit()
    print("database populated")

