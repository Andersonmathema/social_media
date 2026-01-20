from fastapi import FastAPI
from social_media.api.configuration import configure_db, configure_routes


def create_app():
    app = FastAPI()

    # inicializar db/tortoise
    configure_routes(app)
    configure_db(app)

    return app


app = create_app()
