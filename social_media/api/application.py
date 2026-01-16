from fastapi import FastAPI
from social_media.datalayer.dbconfig import configure_db


def create_app():
    app = FastAPI()

    # inicializar db/tortoise
    configure_db(app)

    return app


app = create_app()

@app.get('/')
async def home():
    return {'status': 'ok'}
