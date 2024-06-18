FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY candidates.py .

EXPOSE 9002

CMD ["python", "candidates.py"]