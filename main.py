from fastapi import FastAPI


app = FastAPI(
    title="Phone catalog"
)


@app.get("/")
def hello():
    return "Hello, world!"
