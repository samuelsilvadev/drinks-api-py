# Drinks Storage

Simple API to manage drinks. 🤷‍♀️

## Overview

Nothing much to say 😅

## Installation

1. Clone the repository:

```shell
git clone https://github.com/samuelsilvadev/drinks-api-py.git
```

2. Navigate to the project directory:

```shell
cd drinks-api-py
```

3. Create and activate a virtual environment:

```shell
python -m venv venv
source venv/bin/activate # On Unix-like systems
venv\Scripts\activate # On Windows
```

4. Install dependencies:

```shell
pip install -r requirements.txt
```

## Usage

1. Start the Flask server:

```shell
flask run
```

2. The API should now be accessible at `http://localhost:5000`.

## Endpoints

- `GET /drinks`:
  - Description: Retrieve a list of drinks.
  - Parameters: None.
  - Response: JSON array of drinks objects.

- `GET /drinks/:id`:
  - Description: Retrieve a unique drink.
  - Parameters: id.
  - Response: JSON dictionary of a drink.

- `POST /drinks`:
  - Description: Create a new drink.
  - Parameters: JSON object representing a drink.
  - Response: JSON dictionary of the created drink.

- `DELETE /drinks/:id`:
  - Description: Delete a drink.
  - Parameters: id.
  - Response: None.

## Contact

- samuelsilvawb@gmail.com
- [X](https://twitter.com/samuelsilvadev)