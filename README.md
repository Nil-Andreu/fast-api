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