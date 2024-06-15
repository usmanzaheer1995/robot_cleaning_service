# Robot Cleaning Service

## Overview

The Robot Cleaning Service is a Flask-based microservice designed to simulate a robot moving in an office space and cleaning designated places. The service accepts commands via HTTP requests to specify the starting coordinates and movement directions of the robot on a grid-like office environment. After completing its cleaning path, the service stores execution details in a PostgreSQL database and returns the results in JSON format.

## Environment Used

- Python 3.10
- Flask 3.0.3
- SQLAlchemy 3.1.1
- PostgreSQL (Version 13)
- Docker (for containerization)

## Requirements

To run this project locally, ensure you have the following installed:

- Python (3.10 recommended)
- pip package manager
- PostgreSQL database (you can use Docker to run it locally)
- Docker (optional, for containerization)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/usmanzaheer1995/robot_cleaning_service.git
   cd robot_cleaning_service
   
2. Install dependencies using pip:
    ```bash
   pip install -r requirements.txt

3. Create a .env file in the root directory of the project with the following variables:
    ```bash
   DATABASE_URI=postgresql://user:password@localhost:5432/tibber
   PORT=5000

## Running the application
- Run through docker-compose:
    ```bash
    docker-compose up --build

The application will be accessible at http://localhost:5000.


## API Endpoints
- <strong>POST /tibber-developer-test/enter-path:</strong> Endpoint to simulate the robot's movement and cleaning operation. Sends commands to the service in JSON format specifying starting coordinates and movement directions.


- Example curl request:
    
```bash
  curl -X POST \
  http://localhost:5000/tibber-developer-test/enter-path \
  -H 'Content-Type: application/json' \
  -d '{
        "start": {
          "x": 10,
          "y": 22
        },
        "commands": [
          {
            "direction": "east",
            "steps": 2
          },
          {
            "direction": "north",
            "steps": 1
          }
        ]
      }'
 ```

## Testing
To run tests, use pytest:
```bash
pytest
