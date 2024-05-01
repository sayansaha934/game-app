from fastapi import APIRouter
from fastapi.responses import JSONResponse
from .service import GameService
from .request import CreateGameRequest, EditGameRequest
from db import SESSION

router = APIRouter()


@router.post("")
def create_game(args: CreateGameRequest):
    try:
        new_game = GameService().create_game(
            SESSION=SESSION, name=args.name, url=args.url, author=args.author
        )
        SESSION.close()
        return JSONResponse(status_code=200, content=new_game)
    except Exception as e:
        print(e)
        SESSION.rollback()
        return JSONResponse(status_code=500, content=str(e))


@router.put("/{id}")
def edit_game(id: str, args: EditGameRequest):
    try:
        edited_game = GameService().edit_game(
            SESSION=SESSION,
            game_id=id,
            name=args.name,
            url=args.url,
            author=args.author,
        )
        SESSION.close()
        return JSONResponse(status_code=200, content=edited_game)
    except Exception as e:
        print(e)
        SESSION.rollback()
        return JSONResponse(status_code=500, content=str(e))


@router.delete("/{id}")
def delete_game(id: str):
    try:
        is_deleted = GameService().delete_game(SESSION=SESSION, game_id=id)
        SESSION.close()
        if not is_deleted:
            return JSONResponse(status_code=404, content={"message": "Game not found"})
        return JSONResponse(
            status_code=200, content={"message": "Game deleted successfully"}
        )
    except Exception as e:
        print(e)
        SESSION.rollback()
        return JSONResponse(status_code=500, content=str(e))


@router.get("/{id}")
def get_game(id: str):
    try:
        game = GameService().get_game(SESSION=SESSION, game_id=id)
        SESSION.close()
        if not game:
            return JSONResponse(status_code=404, content={"message": "Game not found"})
        return JSONResponse(status_code=200, content=game)
    except Exception as e:
        print(e)
        SESSION.rollback()
        return JSONResponse(status_code=500, content=str(e))


@router.get("")
def get_all_games():
    try:
        games = GameService().get_all_games(SESSION=SESSION)
        SESSION.close()
        return JSONResponse(status_code=200, content=games)
    except Exception as e:
        print(e)
        SESSION.rollback()
        return JSONResponse(status_code=500, content=str(e))
