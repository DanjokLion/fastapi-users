from fastapi import FastAPI
from models import User, Feedback, UserCreate
from db import Database

app = FastAPI()
db = Database()

@app.post('/user')
async def check_user_age(user: User):
    user.is_adult = (user.age >= 18)
    return user.__dict__

@app.post('/feedback')
async def process_feedback(fb: Feedback):
    db.add_feedback(fb.name, fb.message)
    return {'message': 'Feedback received. Thanks ' + fb.name}

@app.get('/reviews')
async def show_reviews()
    all_feedbacks = []
    for u in db.get_all_reviews():
        all_feedbacks.append(dict(zip(('name', 'message'), u)))
    return {'reviews': all_feedbacks}

@app.post('/create_user')
async def create_user(user: UserCreate):
    db.add_user(user)
    return user

@app.get('/users')
async def get_users():
    return db.get_all_users