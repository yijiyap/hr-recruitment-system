FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY shortlist.py .

EXPOSE 9001

CMD ["python", "shortlist.py"]