FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

EXPOSE 8050
CMD ["gunicorn", "--workers=1", "--bind=0.0.0.0:8050", "main:server"]