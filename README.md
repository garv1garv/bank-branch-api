# Bank Branch GraphQL API

This repository contains a GraphQL API server built with Python to query bank and branch data. It is designed to be fast, easy to set up locally, and strictly follows the required GraphQL schema structure.

> **Note to Evaluators:** Please note that this submission is delayed by 3 days due to my mid-semester university exams. I appreciate your understanding and consideration!

## Live API Endpoint (Hosted on Render)
The API is successfully deployed and hosted on **Render**. You can test the live GraphQL endpoint and run the sample query directly in the browser here:

👉 **https://bank-branch-api.onrender.com/gql**

*(Note: Since this is hosted on a free Render instance, the server may go to sleep after 15 minutes of inactivity. The very first request might take 30-60 seconds to wake the server up, but subsequent requests will be instant!)*

## Methodology Used

To solve this problem and build a robust API, I used the following tech stack and methodology:

1. **Web Framework (FastAPI):** I chose FastAPI as the core web framework because of its high performance, native asynchronous support, and clean developer experience.
2. **GraphQL Implementation (Strawberry):** I used the Strawberry GraphQL library to build the schema. To perfectly match the sample query provided in the assignment, I implemented a Relay-style pagination structure utilizing `edges` and `nodes`.
3. **Database & ORM (SQLite + SQLAlchemy):** For ease of setup and testing, the application uses a lightweight SQLite database. I used SQLAlchemy to define the `Bank` and `Branch` models with a one-to-many relationship. 
4. **Data Ingestion:** The application is programmed to automatically read the provided `bank_branches.csv` file and populate the SQLite database the very first time the server boots up. This eliminates the need for manual database configuration for anyone testing the code.
5. **Testing (Pytest):** I wrote automated test cases using `pytest` and FastAPI's `TestClient` to send the exact GraphQL query requested and validate that the JSON response structure is 100% correct.

## Time Taken

* It took me approximately **3.5 hours** to design, code, test, and write the documentation for this solution. 

## Prerequisites
* Python 3.8+
* `bank_branches.csv` placed in the root directory of this project.

## How to Run Locally

**1. Clone the repository and navigate into it.**

**2. Create and activate a virtual environment (recommended):**

On Windows:
```bash
python -m venv venv
.\venv\Scripts\activate
```

On Mac/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

**3. Install the dependencies:**
```bash
pip install -r requirements.txt
```

**4. Start the server:**
```bash
uvicorn main:app --reload
```
*(Note: On the first run, the server will take a few seconds to parse the CSV and build the local SQLite database. Subsequent restarts will be instant.)*

**5. Access the API:**
Open your browser and navigate to the GraphQL Playground at:
👉 **http://127.0.0.1:8000/gql**

## How to Test

To run the automated test suite and verify the GraphQL endpoint returns the correct structure, simply run:

```bash
pytest
```
