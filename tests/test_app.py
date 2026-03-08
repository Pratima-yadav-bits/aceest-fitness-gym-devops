import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import pytest
from app import app


@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client


def test_home(client):
    response = client.get("/")
    assert response.status_code == 200


def test_programs(client):
    response = client.get("/programs")
    assert response.status_code == 200


def test_single_program(client):
    response = client.get("/program/Fat Loss (FL)")
    assert response.status_code == 200