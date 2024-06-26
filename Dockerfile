FROM python:3.4

ENV APP_HOME/ app

WORKDIR $APP_HOME

COPY requirements.txt .

RUN python -m pip install -r requirements.txt

COPY . /app

EXPOSE 8000

ENTRYPOINT [ "python", "main.py" ]