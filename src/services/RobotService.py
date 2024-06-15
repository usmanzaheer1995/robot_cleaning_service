from src.repositories.RobotRepository import RobotRepository
from src.models.Executions import Executions
from datetime import datetime


class RobotService:

    @staticmethod
    def process_path(start, commands):
        x, y = start['x'], start['y']
        visited = set()
        visited.add((x, y))

        for command in commands:
            direction = command['direction']
            steps = command['steps']

            for _ in range(steps):
                if direction == 'north':
                    y += 1
                elif direction == 'east':
                    x += 1
                elif direction == 'south':
                    y -= 1
                elif direction == 'west':
                    x -= 1
                visited.add((x, y))

        return len(visited)

    @staticmethod
    def save_execution(command_count, result, duration):
        execution = Executions(
            timestamp=datetime.utcnow(),
            command_count=command_count,
            result=result,
            duration=duration
        )
        RobotRepository.save(execution)
        return execution

    @staticmethod
    def calculate_total_duration(commands):
        total_seconds = sum(command['steps'] for command in commands)
        return total_seconds
