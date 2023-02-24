from fastapi import FastAPI

app = FastAPI()

todos =[
    {
        "id": 1,
        "activity": "Brush the teeth"
    },
        {
        "id": 2,
        "activity": "Brush the teeth"
    },
        {
        "id": 3,
        "activity": "Brush the teeth"
    },
]

@app.get("/", tags=['ROOT'])
async def root():
    return {"Ping": "Pong"}



## GET Todo

@app.get("/todo", tags=['todos'])
async def get() -> dict:
    return("data from database", todos)

## POST todo


## UPDATE todo


## DELETE todo