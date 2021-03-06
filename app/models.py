from . import db
from sqlalchemy import types
from sqlalchemy_json import MutableJson, NestedMutableJson
from sqlalchemy_utils import ScalarListType, URLType

class Pokemon(db.Model):
    __tablename__ = 'pokemon'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    stage = db.Column(db.Integer)
    galar_dex = db.Column(db.Integer)
    base_stats = db.Column(ScalarListType(int))
    abilities = db.Column(ScalarListType())
    types = db.Column(ScalarListType())
    level_up_moves = db.Column(NestedMutableJson)
    egg_moves = db.Column(ScalarListType())
    tms = db.Column(ScalarListType(int))
    trs = db.Column(ScalarListType(int))
    image = db.Column(URLType())

    def __init__(self, id_no, name, stage, galar_dex, base_stats, abilities, types,
                level_up_moves, egg_moves, tms, trs):
        self.id = id_no
        self.name = name
        self.stage = stage
        self.galar_dex = galar_dex
        self.base_stats = base_stats
        self.abilities = abilities
        self.types = types
        self.level_up_moves = level_up_moves
        self.egg_moves = egg_moves
        self.tms = tms
        self.trs = trs

    def set_image_url(self, url):
        self.image = url
