from flask import Blueprint, request, jsonify
import time

from src.services.RobotService import RobotService

blueprint = Blueprint('robot_controller', __name__)


@blueprint.route('/tibber-developer-test/enter-path', methods=['POST'])
def enter_path():
    data = request.json
    start = data['start']
    commands = data['commands']

    start_time = time.time()
    unique_places_cleaned = RobotService.process_path(start, commands)
    duration = round(time.time() - start_time, 5)

    execution = RobotService.save_execution(len(commands), unique_places_cleaned, duration)

    return jsonify({
        'id': execution.id,
        'timestamp': execution.timestamp.isoformat(),
        'command_count': execution.command_count,
        'result': execution.result,
        'duration': duration
    }), 201
