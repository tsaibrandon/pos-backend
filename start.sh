#!/bin/bash

# Run migrations using Poetry's virtual environment
poetry run alembic upgrade head

# Start FastAPI server (accessible only on localhost)
exec poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
