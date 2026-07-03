# python-internship-task-4-
# Flask REST API - User Management

## Project Overview

This project is a simple REST API developed using **Python** and **Flask**. The API performs basic CRUD (Create, Read, Update, Delete) operations on user data stored in an in-memory list. It demonstrates the fundamentals of REST API development and HTTP methods.

---

## Objective

* Build a REST API using Flask.
* Implement GET, POST, PUT, and DELETE endpoints.
* Store user data in memory (without a database).
* Test the API using Postman or cURL.

---

## Technologies Used

* Python 3.x
* Flask
* Postman (for API testing)

---

## Project Structure

```text
Flask_REST_API/
│
├── app.py
├── requirements.txt
└── README.md
```

---

## Installation

### 1. Clone or Download the Project

Download the project files or clone the repository.

### 2. Install Flask

```bash
pip install flask
```

Or install all dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Application

Run the following command in the terminal:

```bash
python app.py
```

The Flask development server starts at:

```text
http://127.0.0.1:5000/
```

---

## API Endpoints

### 1. Get All Users

**Method:** GET

**Endpoint**

```text
/users
```

**Response**

Returns a list of all users.

---

### 2. Get User by ID

**Method:** GET

**Endpoint**

```text
/users/<id>
```

Example:

```text
/users/1
```

Returns the details of the specified user.

---

### 3. Add a New User

**Method:** POST

**Endpoint**

```text
/users
```

**Request Body**

```json
{
    "name": "Anjali",
    "age": 20
}
```

**Response**

```json
{
    "message": "User added successfully",
    "user": {
        "id": 3,
        "name": "Anjali",
        "age": 20
    }
}
```

---

### 4. Update an Existing User

**Method:** PUT

**Endpoint**

```text
/users/<id>
```

Example:

```text
/users/1
```

**Request Body**

```json
{
    "name": "Rakshita",
    "age": 22
}
```

Updates the specified user's information.

---

### 5. Delete a User

**Method:** DELETE

**Endpoint**

```text
/users/<id>
```

Example:

```text
/users/2
```

Deletes the specified user.

---

## HTTP Status Codes Used

| Status Code | Meaning                                 |
| ----------- | --------------------------------------- |
| 200         | OK - Request successful                 |
| 201         | Created - Resource created successfully |
| 404         | Not Found - User does not exist         |

---

## Testing the API

The API can be tested using:

* Postman
* cURL
* Thunder Client (VS Code Extension)

### Example cURL Commands

Get all users:

```bash
curl http://127.0.0.1:5000/users
```

Add a user:

```bash
curl -X POST http://127.0.0.1:5000/users ^
-H "Content-Type: application/json" ^
-d "{\"name\":\"Anjali\",\"age\":20}"
```

---

## Key Concepts

* Flask
* REST API
* CRUD Operations
* HTTP Methods (GET, POST, PUT, DELETE)
* JSON
* Routes
* Request and Response
* HTTP Status Codes

---

## Future Enhancements

* Integrate a database such as MySQL or SQLite.
* Add input validation.
* Implement user authentication.
* Improve error handling.
* Add logging and API documentation.

---

## Learning Outcomes

After completing this project, you will understand:

* How to build REST APIs using Flask.
* How Flask routes work.
* How to process client requests.
* How to send JSON responses.
* How to implement CRUD operations.
* How to test APIs using Postman or cURL.

---

## Author

**Rakshita**

REST API using Python and Flask as part of a hands-on learning project.
