import uuid
from .model import Game
from .schema import GameSchema


class GameService:
    def __init__(self) -> None:
        pass

    def create_game(self, SESSION, name, url, author):
        """
        Creates a new game with the given name, URL, and author.

        Parameters:
            SESSION (Session): The SQLAlchemy session object.
            name (str): The name of the game.
            url (str): The URL of the game.
            author (str): The author of the game.

        Returns:
            str: The ID of the newly created game.
        """
        new_game = Game(name=name, url=url, author=author)
        SESSION.add(new_game)
        SESSION.commit()
        data = GameSchema(only=["id"]).dump(new_game)
        return data

    def get_game(self, SESSION, game_id: uuid.UUID):
        """
        Retrieves a game from the database based on the given game ID.

        Parameters:
            SESSION (Session): The SQLAlchemy session object.
            game_id (uuid.UUID): The unique identifier of the game.

        Returns:
            dict: The serialized game data in dictionary format.
        """
        game = SESSION.query(Game).filter(Game.id == game_id).first()
        data = GameSchema().dump(game)
        return data

    def delete_game(self, SESSION, game_id: uuid.UUID):
        """
        Deletes a game from the database.

        Parameters:
            SESSION (Session): The SQLAlchemy session object.
            game_id (uuid.UUID): The unique identifier of the game to be deleted.

        Returns:
            bool: True if the game is successfully deleted, False otherwise.
        """
        game_to_delete = SESSION.query(Game).filter(Game.id == game_id).first()
        if game_to_delete:
            game_to_delete.status = "archived"
            SESSION.commit()
            return True

    def get_all_games(self, SESSION):
        """
        Retrieves all published games from the database.

        Parameters:
            SESSION (Session): The SQLAlchemy session object.

        Returns:
            list: A list of serialized game data in dictionary format.
        """
        games = SESSION.query(Game).filter(Game.status == "published").all()
        data = GameSchema(many=True).dump(games)
        return data

    def edit_game(self, SESSION, game_id: uuid.UUID, name: str, url: str, author: str):
        """
        Edits a game with the provided game ID, name, URL, and author.

        Parameters:
            SESSION (Session): The SQLAlchemy session object.
            game_id (uuid.UUID): The unique identifier of the game.
            name (str): The new name of the game.
            url (str): The new URL of the game.
            author (str): The new author of the game.

        Returns:
            The serialized game data after editing.
        """
        game_to_edit = SESSION.query(Game).filter(Game.id == game_id).first()
        if game_to_edit:
            game_to_edit.name = name
            game_to_edit.url = url
            game_to_edit.author = author
            SESSION.commit()
            data = GameSchema().dump(game_to_edit)
            return data
