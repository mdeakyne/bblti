FROM python:3.8

COPY Pipfile

RUN pip install pipenv
RUN pipenv install