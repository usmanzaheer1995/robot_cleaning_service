from unittest.mock import patch, MagicMock

from src.models.Executions import Executions
from src.services.RobotService import RobotService
from src.repositories.RobotRepository import RobotRepository


def test_process_path():
    service = RobotService()
    start = {"x": 10, "y": 22}
    commands = [
        {"direction": "east", "steps": 2},
        {"direction": "north", "steps": 1}
    ]

    result = service.process_path(start, commands)
    assert result == 4


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
