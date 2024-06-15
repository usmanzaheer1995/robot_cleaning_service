from flask import Blueprint, request, jsonify
from src.services.RobotService import RobotService
import time

blueprint = Blueprint('robot_controller', __name__)


@blueprint.route('/tibber-developer-test/enter-path', methods=['POST'])
def enter_path():
    data = request.json
    start = data['start']
    commands = data['commands']

    start_time = time.time()
    unique_places_cleaned = RobotService.process_path(start, commands)
    duration = time.time() - start_time

    execution = RobotService.save_execution(len(commands), unique_places_cleaned, format_duration(duration))

    return jsonify({
        'id': execution.id,
        'timestamp': execution.timestamp.isoformat(),  # Example formatting
        'command_count': execution.command_count,
        'result': execution.result,
        'duration': format_duration(execution.duration)
    }), 201


def format_duration(duration):
    return f"{duration:.6f}"
