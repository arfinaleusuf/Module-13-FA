from test.test_main import client
from main import app
from fastapi import status

def test_read_todos():
    respons = client.get('/')
    assert respons.status_code == status.HTTP_401_UNAUTHORIZED
    