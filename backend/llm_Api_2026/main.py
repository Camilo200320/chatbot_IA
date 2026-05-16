from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.chat_router import router  # Asegúrate de importar el router desde chat_router.py

app = FastAPI()

app.include_router(router)  # Asegúrate de importar el router desde chat_router.py
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}

