FROM python:3.7-slim-buster

WORKDIR /apps
COPY . /apps
RUN /app/requirements.txt

CMD ["./main.py" ]
ENTRYPOINT ["python"]