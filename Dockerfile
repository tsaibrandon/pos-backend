FROM python:3.13-bookworm

# Set working directory inside the container
WORKDIR /

# Install required system dependencies
RUN apt-get update && apt-get install -y curl build-essential

# Install Poetry
RUN pip install poetry

# Add poetry to PATH for the current shell session
ENV PATH="/root/.local/bin:${PATH}"

# Copy the poetry project files (pyproject.toml and poetry.lock)
COPY pyproject.toml poetry.lock* ./

# Install dependencies defined in pyproject.toml using Poetry
RUN poetry install --no-root

# Copy the rest of the application files
COPY . .

# Expose the port for the application
EXPOSE 8000

# Set PYTHONPATH for Alembic to find the app module
ENV PYTHONPATH=/app

# Set the entry point to ensure Poetry's virtual environment is used
RUN chmod +x /start.sh
CMD ["/start.sh"]