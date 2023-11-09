import requests
import logging

URL = "http://127.0.0.1:8000"

data = [
    {
        'name': 'John Doe',
        'email': 'jothdoe34@gmail.com',
        'age': 32,
        'is_subscribed': True
    },
    {
        'name': 'Lena Golovach',
        'email': 'golovachlena@mail.ru'
    },
    {
        'name': 'Prorok Sunboy',
        'email': 'rotporvy1488@yandex.ru'
    },
    {
        'name': 'James Cameron',
        'email': 'jamescameron13@gmail.com',
        'age': 18,
        'is_subscribed': False
    },
]

for x in data:
    resp = requests.post(URL + '/create_user', json=x)
    if resp.status_code == 422:
        logging.error('TypeError: %s\n', resp.content)
    else:
        logging.warning('Success!: %s', resp.content)