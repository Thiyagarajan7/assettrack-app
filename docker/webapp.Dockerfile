FROM 192.168.3.236/assettrack/base:latest

WORKDIR /app
COPY . .

CMD ["uvicorn", "webapp.app:app", "--host", "0.0.0.0", "--port", "8000"]
