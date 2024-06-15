import os
from flask import Flask
from dotenv import load_dotenv

load_dotenv()

from src.configs.db import init_db
from src.controllers.RobotController import blueprint


def create_app(test_config=None):
    new_app = Flask(__name__)

    new_app.config.from_mapping(
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        SQLALCHEMY_DATABASE_URI=os.getenv('DATABASE_URI')
    )

    if test_config:
        new_app.config.from_mapping(test_config)

    init_db(new_app)

    new_app.register_blueprint(blueprint)

    return new_app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=os.getenv('PORT'))
