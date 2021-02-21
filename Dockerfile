FROM python:3.8.7

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt -i https://pypi.doubanio.com/simple/

EXPOSE 80

CMD gunicorn -c gunicorn.conf main:app