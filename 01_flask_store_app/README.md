# This is simple store flask application

## Prerequisites

* Python 3.10+
* Docker (optional)

## APIs

1. Create a store (POST /store)
2. Create an item in store (POST /store/<name>/item)
3. Get a store (GET /store/<name>)
4. Get an items in store (GET /store/<name>/item)

## How to Run

```bash
docker-compose up -d
```

## How to Stop

```bash
docker-compose down
```

## How to Build

```bash
docker-compose build app
```

## How to Access the application

### Running as docker container

```bash
curl http://localhost:6000/store

```

### Running without docker

```bash
curl http://localhost:5000/store
```

## How to Run without docker

```bash
python -m venv .venv source .venv/bin/activate # On Windows use .venv\Scripts\activate
pip install flask
flask run
```

## Play & Test with rest clients

*  Insomnia
*  Postman