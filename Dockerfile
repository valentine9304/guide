FROM python:3.11-slim

WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000

CMD ["sh", "-c", "alembic upgrade head && python seed.py && uvicorn src.main:app --host 0.0.0.0 --port 8000"]