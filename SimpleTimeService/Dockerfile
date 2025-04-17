# Use official Python slim image
FROM python:3.9-slim
RUN useradd -m appuser && \
    mkdir -p /app && \
    chown appuser:appuser /app
WORKDIR /app
COPY requirements.txt app/main.py /app/
RUN pip install -r requirements.txt
USER appuser
EXPOSE 3000
CMD ["python", "/app/main.py"]