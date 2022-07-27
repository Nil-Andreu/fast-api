# Fast API 
Fast API is a library from Python that allows you to create simple & performant REST APIs.

To start, we will install both FastAPI and uvicorn.

To create the necessary setup to run the project on the local computer:
```
    make setup
```

## Creating Simple REST API
To create a simple Rest API, we need to define the *app = FastAPI()*, and then define the endpoints.

So an example would be:
```
    from fastapi import FastAPI

    app = FastAPI()

    @app.get("/")
    async def main():
        return {"hello", "World"}
```

Then to run it, we use *uvicorn run main:app*, where **main** is the name of the file, and **app** is the FastAPI instance that we defined inside this file.
If we want to specify the port, **--port** tag.

If we wanted to see the documentation, we would go to */docs*, and we would see the automatic interactive Swagger.

### Path Parameters
We can define Path Parameters in the following way:
```
    @app.get("/products/{id}/{type}")
    async def get_products(id: int, type: str):
        return {"id":id, "type":type}
```

As we can see, we pass the path parameters of *id* and *type*, with type hinting in the parameters of the function as *int* and *str* respectively.

Type Hinting will help in the automatic validation of the fields that FastAPI makes.

To add more validation, we can use the *Path* function provided by FastAPI:
```
    @app.get("/products/{id}/{type}")
    async def get_products(id: int = Path(..., ge=1), type: str = Path(..., min_length=10, max_length=12)):
        return {"id":id, "type":type}
```

Where we are checking that the id is greater than 1, and that the type name length is between 10 - 12.

### Query Parameters
We can also have query parameters:
```
    @app.get("/products")
    async def get_products(id: int = Query(..., ge=1), type: str = Query(..., min_length=10, max_length=12)):
        return {"id":id, "type":type}
```

Where those parameters will be passed via: /products?id=1&type=productPremium.

For the validation, insteado of using the Path function, we use the Query function.