import pytest
from flask import Flask
from unittest.mock import patch
from datetime import datetime

from src.controllers.RobotController import blueprint
from src.models.Executions import Executions


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
    mock_execution = Executions(
        id=1,
        timestamp=datetime(2024, 1, 1),
        command_count=2,
        result=4,
        duration=0.001
    )

    mock_robot_service.save_execution.return_value = mock_execution

    response = client.post('/tibber-developer-test/enter-path', json={
        "start": {"x": 10, "y": 22},
        "commands": [
            {"direction": "east", "steps": 2},
            {"direction": "north", "steps": 1}
        ]
    })

    assert response.status_code == 201

    assert response.json['id'] == mock_execution.id
    assert response.json['timestamp'] == mock_execution.timestamp.isoformat()
    assert response.json['command_count'] == mock_execution.command_count
    assert response.json['result'] == mock_execution.result
