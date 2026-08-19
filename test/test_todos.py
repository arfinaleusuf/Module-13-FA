from test.test_main import client
from main import app
from fastapi import status
from router.auth import get_current_user
from database import SessionLocal
from models import Todos

def override_get_current_user():
    return {
        'id' : 1,
        'usename': 'testuser'
    }

def test_todo():
    db = SessionLocal()

    # remove old test data if its exist
    db.query(Todos).filter(Todos.id == 99).delete()

    todo = Todos(
        id = 99,
        title ='Testing',
        description = 'Testing',
        priority = 5,
        completed = True,
        owner_id = 1
    )

    db.add(todo)
    db.commit()


app.dependency_overrides[get_current_user] = override_get_current_user

def test_read_todos():
    respons = client.get('/')
    assert respons.status_code == status.HTTP_200_OK

def test_read_specific_todos():
    respons = client.get('/todo/99')
    assert respons.status_code == status.HTTP_200_OK