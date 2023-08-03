FROM python:3.8

WORKDIR /jokeapp

COPY requirements.txt /jokeapp/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /jokeapp/

EXPOSE 8001

CMD ["python", "jokeapp.py"]