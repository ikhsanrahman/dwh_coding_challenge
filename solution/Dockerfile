FROM python:3.9-slim-buster as dkatalis_test

WORKDIR /apps
COPY . /apps

RUN python3 -m pip install --upgrade pip
RUN pip3 install -r /apps/requirements.txt

CMD ["python3", "./main.py" ]
