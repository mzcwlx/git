from fastapi import APIRouter

api_compute = APIRouter()

@api_compute.get("/add")
async def add_numbers(a: int, b: int):
    result = a + b
    return {"result": result}

@api_compute.get("/subtract")
async def subtract_numbers(a: int, b: int):
    result = a - b
    return {"result": result}