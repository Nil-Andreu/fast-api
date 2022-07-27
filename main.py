from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/")
async def main():
    return {"hello", "World"}

@app.get("/products/{id}/{type}")
async def get_products(id: int = Path(..., ge=1), type: str = Path(..., min_length=10, max_length=12)):
    return {"id":id, "type":type}