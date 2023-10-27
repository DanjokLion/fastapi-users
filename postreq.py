from fastapi import FastAPI

app = FastAPI()

@app.get('/calculate/{item_id}')
async def calc(item_id: str):
    a, b = map(int, item_id.split('+'))
    return {'result': a + b }