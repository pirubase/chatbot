import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app import entrypoints

app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(entrypoints.rag_router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8001)
@app.get("/")
def read_root():
    return {"message": "Hello World"}