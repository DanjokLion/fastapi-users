from fastapi import FastAPI
from models import User, Feedback


app = FastAPI()
ls = []

fake_users = {
    1: {"username" : "john_doe", "email": "john@example.com"},
    2: {"username" : "jane_smith", "email": "jane@example.com"}
}

@app.get('/users/{user_id}')
def read_user(user_id: int):
    return fake_users.get(user_id, {'error': 'User not found'})
    # if user_id in fake_users:
    #     return fake_users[user_id]
    # return {'error': 'User not found'}

@app.get('/users/')
def read_users(limit: int = 10):
    return dict(list(fake_users.items())[:limit])

@app.get('/feedback')
async def send_fb(feedback: Feedback):
    ls.append({'name': feedback.name, 'comments': feedback.message})
    return f'Feedback received. Thank you, {feedback.name}!'

@app.get('/comments')
async def show_fb():
    return ls