from fastapi import APIRouter
from fastapi import Request

api_book = APIRouter()

@api_book.get("/")
async def root():
    return {"message": "It's a book!"}