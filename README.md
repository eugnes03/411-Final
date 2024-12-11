# 411-Final

Loan Qualification System

## Introduction

This project is a loan qualification system that determines if a user is qualified for a loan based on their credit score, monthly debt, monthly income, and desired loan amount. The system will prompt the user to enter their information and will output whether they are qualified for the loan, and well get their credit score, monthly income etc from Plaid API.

We set up a sandbox environment for the Plaid API, and we will be using the sandbox environment to get the user's information. The user will be prompted to enter their information, and the system will use the Plaid API to get the user's information.

So we have the requirements for a loan from "Bank of America" (tentative), and we cross reference using our backend to check whether a person is qualified for the loan. If not, we display what the difference for qualifications are.

We create a frontend where users can login, and then also check using this information. We structure the requests in JSON format, and we will be using Flask to handle the requests.

## Technologies

API Calls needs to be included through Plaid API.

In addition, this project needs to include flask and python.

We also set up a database with user information, specifically user logins and passwords. We will be using SQLite for this project.

## Installation Guide


To install the necessary libraries, you can use the following command:

```bash
pip install -r requirements.txt
```
Then you can run the app by running the following command:

```bash
./run_docker.sh
```

Then check the docker container by running the following command:

```bash
docker ps
```

Then you can run the following command to check the logs:

```bash
docker logs <container_id>
```


## Usage

To use the app, you can go to the following URL:

```bash
http://localhost:5000/
```

You can then enter your information and the system will determine if you are qualified for the loan.

At the same time, these requests can work for API requests as well.

## Routes

Here’s a translated version of the route documentation you can copy into a README file:

---

## Route Documentation Example

### Route: `/create-account`

- **Request Type:** POST
- **Purpose:** Creates a new user account with a username and password.

#### Request Body:
- `username` (String): User's chosen username.
- `password` (String): User's chosen password.

#### Response Format: JSON

**Success Response Example:**
- **Code:** 200
- **Content:**
  ```json
  {
    "message": "Account created successfully"
  }
  ```

#### Example Request:
```json
{
  "username": "newuser123",
  "password": "securepassword"
}
```

#### Example Response:
```json
{
  "message": "Account created successfully",
  "status": "200"
}
```

---

### Route: `/login`


- **Request Type:** POST

- **Purpose:** Logs a user in with their username and password.

#### Request Body:

- `username` (String): User's username.
- `password` (String): User's password.

#### Response Format: JSON

**Success Response Example:**

- **Code:** 200

- **Content:**

  ```json
  {
    "message": "Login successful"
  }
  ```
Here’s a translated version of your code as route documentation for a README file:

---

## Route Documentation

### 1. **Create Link Token**
- **Route:** `/create_link_token`
- **Request Type:** POST
- **Purpose:** Creates a new Plaid Link Token for initiating user connections.

#### Request Body:
_None_

#### Response Format: JSON
**Success Response Example:**
- **Code:** 200
- **Content:**
  ```json
  {
    "link_token": "your_generated_link_token"
  }
  ```

**Error Response Example:**
- **Code:** 500
- **Content:**
  ```json
  {
    "error": "Error message here"
  }
  ```

---

### 2. **Exchange Public Token**
- **Route:** `/exchange_public_token`
- **Request Type:** POST
- **Purpose:** Exchanges a public token for an access token.

#### Request Body:
- `public_token` (String): Public token received from Plaid Link.

#### Response Format: JSON
**Success Response Example:**
- **Code:** 200
- **Content:**
  ```json
  {
    "access_token": "your_access_token"
  }
  ```

**Error Response Example:**
- **Code:** 500
- **Content:**
  ```json
  {
    "error": "Error message here"
  }
  ```

---

### 3. **Fetch Transactions**
- **Route:** `/transactions`
- **Request Type:** GET
- **Purpose:** Retrieves transactions for a given access token.

#### Query Parameters:
- `access_token` (String): Access token to authenticate the request.

#### Response Format: JSON
**Success Response Example:**
- **Code:** 200
- **Content:**
  ```json
  {
    "transactions": [
      {
        "transaction_id": "12345",
        "amount": 100,
        "date": "2023-01-01"
      }
    ]
  }
  ```

**Error Response Example:**
- **Code:** 500
- **Content:**
  ```json
  {
    "error": "Error message here"
  }
  ```

---

### 4. **Fetch Income**
- **Route:** `/fetch_income`
- **Request Type:** GET
- **Purpose:** Fetches income information for a given access token.

#### Query Parameters:
- `access_token` (String): Access token to authenticate the request.

#### Response Format: JSON
**Success Response Example:**
- **Code:** 200
- **Content:**
  ```json
  {
    "income": { "income_data": "data here" }
  }
  ```

**Error Response Example:**
- **Code:** 500
- **Content:**
  ```json
  {
    "error": "Error message here"
  }
  ```

---

### 5. **Fetch Liabilities**
- **Route:** `/fetch_liabilities`
- **Request Type:** GET
- **Purpose:** Fetches liabilities for a given access token.

#### Query Parameters:
- `access_token` (String): Access token to authenticate the request.

#### Response Format: JSON
**Success Response Example:**
- **Code:** 200
- **Content:**
  ```json
  {
    "liabilities": { "liabilities_data": "data here" }
  }
  ```

**Error Response Example:**
- **Code:** 500
- **Content:**
  ```json
  {
    "error": "Error message here"
  }
  ```

---

### 6. **Simulate Credit Score**
- **Route:** `/simulate_credit_score`
- **Request Type:** GET
- **Purpose:** Simulates a credit score based on fetched income and liabilities.

#### Query Parameters:
- `access_token` (String): Access token to authenticate the request.

#### Response Format: JSON
**Success Response Example:**
- **Code:** 200
- **Content:**
  ```json
  {
    "credit_score": 750
  }
  ```

**Error Response Example:**
- **Code:** 500
- **Content:**
  ```json
  {
    "error": "Error message here"
  }
  ```

---
Here’s the translated version of your code as route documentation for a README file:

---

## Route Documentation

### 1. **Index**
- **Route:** `/index`
- **Request Type:** GET, POST
- **Purpose:** Renders the index page.

#### Response:
- Renders `index.html`.

---

### 2. **Create Account**
- **Route:** `/create-account`
- **Request Type:** GET, POST
- **Purpose:** Renders a form to create a new user account or processes the account creation logic.

#### Request Body (for POST):
- `username` (String): Chosen username of the user.
- `email` (String): Email address of the user.
- `password` (String): Chosen password.
- `confirm-password` (String): Re-entry of the password for confirmation.

#### Response:
- Renders `create-account.html` with messages (success or error):
  - **Error Messages:**
    - "All fields are required."
    - "Passwords do not match."
    - "Username already exists."
    - "Email already exists."
    - "An error occurred. Please try again."
  - **Success Message:**
    - "Account created! Username: {username}, Email: {email}"

---

### 3. **Update Password**
- **Route:** `/update-password`
- **Request Type:** GET, POST
- **Purpose:** Renders a form to update a user's password or processes the password update logic.

#### Request Body (for POST):
- `username` (String): Username of the user.
- `email` (String): Email address of the user.
- `password` (String): New password.

#### Response:
- Renders `update-password.html` with messages (success or error):
  - **Error Messages:**
    - "All fields are required."
    - "User not found. Please check the username or email."
    - "An error occurred while updating the password."
  - **Success Response:**
    - Redirects to `/login` upon successful password update.

---

### 4. **Login**
- **Route:** `/login`
- **Request Type:** GET, POST
- **Purpose:** Renders a login form or processes user login.

#### Request Body (for POST):
- `username` (String): Username of the user.
- `password` (String): Password of the user.

#### Response:
- Renders `login.html` with messages (success or error):
  - **Error Messages:**
    - "All fields are required."
    - "Invalid username or password."
  - **Success Message:**
    - "Welcome back, {username}!"
    - Redirects to `/index` upon successful login.

---







## Contributors

This project was created by:
Ananiya Kinfe
Eugen Nesbakken
Nuo Chen
