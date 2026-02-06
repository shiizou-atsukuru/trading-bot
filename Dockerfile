FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . . 

RUN mkdir -p /app/logs

CMD ["streamlit", "run", "ui.py", "--server.port=8501", "--server.address=0.0.0.0"]