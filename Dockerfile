FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHON UNBUFFERED 1

WORKDIR /code

COPY requirements.txt /code/

RUN pip install -r requirements.txt

COPY . /code/

COPY entrypoint.sh /code/
ENTRYPOINT [ "sh", "entrypoint.sh" ]
