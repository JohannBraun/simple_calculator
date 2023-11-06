# Simple Calculator Project

This project is a simple calculator library developed to familiarize with development habits including project creation, testing, documentation, version control, API development, and containerization.

## Project Structure

The project is structured into several directories:

- `simple_calculator`: Contains the main logic of the calculator.
- `tests`: Contains test cases for the calculator functions.
- `docs`: Contains documentation for the project.
- `examples`: Contains example scripts demonstrating how to use the calculator.

## Project Setup

The project was set up using a bash script that creates the directory structure, initializes a Git repository, and creates a Python virtual environment.

## Version Control

Git is used for version control. All changes are committed to the Git repository.

## Testing

Tests are written using the `unittest` module in Python. They are located in the `tests` directory and can be run using the `unittest` command.

## Documentation

Documentation is written in markdown and is located in the `docs` directory. It includes a description of the project and details on how to use the calculator functions.

## API Development

The calculator functions are exposed as an API using the Flask web framework. The API includes routes for addition and subtraction.

## Containerization

The entire project is containerized using Docker. The Dockerfile specifies how to build the Docker image, which includes the Python runtime, the project code, and its dependencies.

## Usage

To use the calculator library, import the `add` and `subtract` functions from the `simple_calculator.calculator` module.

To use the API, send a POST request to the `/add` or `/subtract` routes with a JSON body that includes the numbers to be added or subtracted.

You can use Postman for this or simple curl commands as following:

```curl -X POST -H "Content-Type: application/json" -d '{"a":5, "b":3}' http://localhost:5000/add``` for addition or

```curl -X POST -H "Content-Type: application/json" -d '{"a":5, "b":3}' http://localhost:5000/subtract``` for substraction.


To run the Docker container, build the Docker image using the Dockerfile and then run the image in a Docker container.

## Future Work

Future work on this project could include adding more mathematical operations, improving the API, and enhancing the Docker setup.