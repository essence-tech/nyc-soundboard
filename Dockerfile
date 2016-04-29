FROM python:3.5

WORKDIR /sb

ADD requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "app.py"]
