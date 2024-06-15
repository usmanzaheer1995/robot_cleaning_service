from src.configs.db import db


class Executions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, nullable=False)
    command_count = db.Column(db.Integer, nullable=False)
    result = db.Column(db.Integer, nullable=False)
    duration = db.Column(db.Float, nullable=False)
