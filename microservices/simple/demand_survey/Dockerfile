FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY demand_survey.py .

EXPOSE 5003

CMD ["python", "demand_survey.py"]