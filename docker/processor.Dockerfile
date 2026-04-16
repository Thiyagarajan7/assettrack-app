FROM 192.168.3.236/assettrack/base:latest

WORKDIR /app
COPY . .

CMD ["python", "processor/app.py"]
