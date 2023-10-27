from fastapi import FastAPI
from models import User

app = FastAPI()

fake_users = {
    1: {"username" : "john_doe", "email": "john@example.com"},
    2: {"username" : "jane_smith", "email": "jane@example.com"}
}

@app.get('/users/{user_id}')
def red_user(user_id: int):
    return fake_users.get(user_id, {'error': 'User not found'})
    # if user_id in fake_users:
    #     return fake_users[user_id]
    # return {'error': 'User not found'}