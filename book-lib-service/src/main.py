from fastapi import FastAPI, HTTPException, status
from .api import routes
from .db.mongo_utils import get_client, get_collection, get_database
app = FastAPI()
app.include_router(routes.router)
client = get_client()
db = get_database(client, "books_db")
books_collection = get_collection(db, "books_collection")


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/import-data")
async def import_data():
    try:
        pass
    except Exception as e:
        
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)