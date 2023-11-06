# API.md

## Simple Calculator API

This API provides basic mathematical operations. It is built using Flask and can be run locally or in a Docker container.

### `POST /add`

Adds two numbers together.

**Request Body:**

- `a`: The first number (required).
- `b`: The second number (required).

**Response Body:**

- `result`: The sum of `a` and `b`.

**Example:**

Request:

```
{
    "a": 5,
    "b": 3
}
```

Response:

```
{
    "result": 8
}
```

### POST /subtract
Subtracts the second number from the first.

**Request Body:**

- `a`: The first number (required).
- `b`: The second number (required).

**Response Body:**

- `result`: The result of `a - b`.

**Example:**


Request:
```
{
    "a": 5,
    "b": 3
}
```
Response:
```
{
    "result": 2
}
```