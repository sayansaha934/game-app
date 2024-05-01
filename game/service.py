import uuid
from .model import Game
from .schema import GameSchema


class GameService:
    def __init__(self) -> None:
        pass

    def create_game(self, SESSION, name, url, author):
        new_game = Game(name=name, url=url, author=author)
        SESSION.add(new_game)
        SESSION.commit()
        data = GameSchema(only=["id"]).dump(new_game)
        return data

    def get_game(self, SESSION, game_id: uuid.UUID):
        game = SESSION.query(Game).filter(Game.id == game_id).first()
        data = GameSchema().dump(game)
        return data

    def delete_game(self, SESSION, game_id: uuid.UUID):
        game_to_delete = SESSION.query(Game).filter(Game.id == game_id).first()
        if game_to_delete:
            game_to_delete.status = "archived"
            SESSION.commit()
            return True

    def get_all_games(self, SESSION):
        games = SESSION.query(Game).filter(Game.status == "published").all()
        data = GameSchema(many=True).dump(games)
        return data

    def edit_game(self, SESSION, game_id: uuid.UUID, name: str, url: str, author: str):
        game_to_edit = SESSION.query(Game).filter(Game.id == game_id).first()
        if game_to_edit:
            game_to_edit.name = name
            game_to_edit.url = url
            game_to_edit.author = author
            SESSION.commit()
            data = GameSchema().dump(game_to_edit)
            return data
