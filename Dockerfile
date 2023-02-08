FROM python:3.10

WORKDIR /code

COPY requirements.txt requirements.txt

COPY . .

RUN pip3 install -r requirements.txt

CMD [ "tail","-f",".logs" ]


