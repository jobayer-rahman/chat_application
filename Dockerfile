FROM python:3.11

WORKDIR /code

COPY requirements.txt /code/

RUN pip install -r requirements.txt

COPY . /code/

WORKDIR /code/chatService

CMD [ "./manage.py", "runserver", "0.0.0.0:8000"]
