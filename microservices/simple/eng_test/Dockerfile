FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY eng_test.py .

EXPOSE 5004

CMD ["python", "eng_test.py"]