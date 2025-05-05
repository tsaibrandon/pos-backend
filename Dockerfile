FROM python:3.13-bookworm
WORKDIR /app
RUN apt-get update && apt-get install -y curl build-essential

ENV PATH="/root/.cargo/bin:${PATH}"
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
