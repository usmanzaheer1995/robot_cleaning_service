import pytest
from flask import Flask
from src.controllers.RobotController import blueprint
from unittest.mock import patch
from datetime import datetime


@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(blueprint)
    app.config['TESTING'] = True
    return app


@pytest.fixture
def client(app):
    return app.test_client()


@patch('src.controllers.RobotController.RobotService')
def test_enter_path(mock_robot_service, client):
    mock_execution = {
        'id': 1,
        'timestamp': datetime(2024, 1, 1).isoformat(),
        'command_count': 2,
        'result': 4,
        'duration': 0.001
    }

    mock_robot_service.process_path.return_value = 4
    mock_robot_service.save_execution.return_value = mock_execution

    response = client.post('/tibber-developer-test/enter-path', json={
        "start": {"x": 10, "y": 22},
        "commands": [
            {"direction": "east", "steps": 2},
            {"direction": "north", "steps": 1}
        ]
    })

    assert response.status_code == 201
    assert response.json == mock_execution
