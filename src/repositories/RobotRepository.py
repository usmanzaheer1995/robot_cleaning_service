from src.configs.db import db


class RobotRepository:

    @staticmethod
    def save(execution):
        db.session.add(execution)
        db.session.commit()
