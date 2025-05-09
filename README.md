# restaurant pos

### development setup (using python3.13)
```sh
curl -sSL https://install.python-poetry.org | python3 -
poetry install
```

### when developing
- make sure IDE uses python interpreter associated with poetry environment

### when making changes (run in root directory)
```sh
poetry run isort . && poetry run black . && poetry run flake8 . && poetry run mypy .
```

### to run the server ([docker](https://www.docker.com/) needed):

```sh
docker-compose up --build
```

### to view api documentation:
1. ensure server is running locally
2. go to `http://0.0.0.0:8000/docs`