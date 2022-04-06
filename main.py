from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer

from routers import auth_router, sources_router

app = FastAPI(debug=True)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
app.include_router(auth_router)
app.include_router(sources_router)
