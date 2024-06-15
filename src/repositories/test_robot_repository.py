import pytest
from app import create_app
from src.models.Executions import Executions
from src.repositories.RobotRepository import RobotRepository
from src.configs.db import db
from datetime import datetime


@pytest.fixture
def app():
    app = create_app({
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:',
        'SQLALCHEMY_TRACK_MODIFICATIONS': False
    })

    with app.app_context():
        db.create_all()

        yield app

        db.session.remove()
        db.drop_all()


@pytest.fixture
def session(app):
    with app.app_context():
        yield db.session
        db.session.rollback()


def test_save_execution(session):
    repository = RobotRepository()
    execution = Executions(
        timestamp=datetime(2024, 1, 1, 0, 0, 0),
        command_count=2,
        result=4,
        duration=0.001
    )

    repository.save(execution)

    saved_execution = Executions.query.first()
    assert saved_execution is not None
    assert saved_execution.command_count == 2
    assert saved_execution.result == 4
    assert saved_execution.duration == 0.001
