FROM python:3
WORKDIR /usr/src/app

COPY . .

EXPOSE 3000

RUN pip install pipenv

RUN pipenv install

RUN pipenv run python manage.py createsuperuser

RUN pipenv run python manage.py migrate

CMD [ "pipenv", "run", "python", "runserver", "3000" ]