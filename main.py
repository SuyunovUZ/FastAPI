from fastapi import FastAPI
from fastapi_jwt_auth import AuthJWT

from auth_router import auth_router
from schemas import Settings, LoginModel

app = FastAPI()


@AuthJWT.load_config
def get_config():
    return Settings()


app.include_router(auth_router)


@app.get('/')
async def root():
    return {"message": "Bu asosiy sahifa"}
