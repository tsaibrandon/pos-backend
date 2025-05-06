# restaurant pos

### development setup (using python3.13)
```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### when making changes (run in root directory)
```sh
isort . && black . && flake8 . && mypy .
```

### to run the server ([docker](https://www.docker.com/) needed):

```sh
docker-compose up --build
```

### to view api documentation:
1. ensure server is running locally
2. go to `http://0.0.0.0:8000/docs`