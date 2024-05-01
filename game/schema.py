from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from .model import Game


class GameSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Game
        load_instance = True