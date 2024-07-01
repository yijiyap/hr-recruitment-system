FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY sharepoint.py .

EXPOSE 5001

CMD ["python", "sharepoint.py"]