from unittest.mock import patch, MagicMock
import pytest

from src.models.Executions import Executions
from src.services.RobotService import RobotService
from src.repositories.RobotRepository import RobotRepository

test_cases = [
    {
        "description": "Minimal Input",
        "input": {
            "start": {"x": 0, "y": 0},
            "commands": []
        },
        "expected": 1
    },
    {
        "description": "Single Command",
        "input": {
            "start": {"x": 0, "y": 0},
            "commands": [{"direction": "north", "steps": 1}]
        },
        "expected": 2
    },
    {
        "description": "Multiple Commands",
        "input": {
            "start": {"x": 10, "y": 22},
            "commands": [
                {"direction": "east", "steps": 2},
                {"direction": "north", "steps": 1}
            ]
        },
        "expected": 4
    },
    {
        "description": "Large Number of Commands",
        "input": {
            "start": {"x": 0, "y": 0},
            "commands": [{"direction": "east", "steps": 10000}]
        },
        "expected": 10001
    },
    {
        "description": "Edge Coordinates",
        "input": {
            "start": {"x": 100000, "y": 100000},
            "commands": [
                {"direction": "west", "steps": 100000},
                {"direction": "south", "steps": 100000}
            ]
        },
        "expected": 200001
    },
    {
        "description": "Non-Standard Paths",
        "input": {
            "start": {"x": 10, "y": 10},
            "commands": [
                {"direction": "north", "steps": 10},
                {"direction": "east", "steps": 10},
                {"direction": "south", "steps": 10},
                {"direction": "west", "steps": 10},
                {"direction": "north", "steps": 5},
                {"direction": "east", "steps": 5}
            ]
        },
        "expected": 45
    }
]


@pytest.mark.parametrize("test_case", test_cases, ids=[tc["description"] for tc in test_cases])
def test_process_paths(test_case):
    result = RobotService.process_path(test_case["input"]["start"], test_case["input"]["commands"])
    assert result == test_case["expected"]


@patch.object(RobotRepository, 'save')
def test_save_execution(mock_save):
    service = RobotService()
    command_count = 2
    result = 4
    duration = 0.001

    mock_execution = MagicMock()
    mock_save.return_value = mock_execution

    execution = service.save_execution(command_count, result, duration)

    mock_save.assert_called_once()
    assert isinstance(execution, Executions)
    assert execution.command_count == command_count
    assert execution.result == result
    assert execution.duration == duration
