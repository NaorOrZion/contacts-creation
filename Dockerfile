FROM python:3.7-alpine
WORKDIR /app
COPY requirements.txt requirements.txt
###RUN apk update && apk add build-base
###RUN apk add gcc
RUN python3 -m pip install -r requirements.txt
COPY . .
CMD ["python3", "main.py"]
