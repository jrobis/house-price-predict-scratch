FROM python:3.8.3

WORKDIR /opt/api

COPY ./packages/api/ /opt/api/

RUN pip install --upgrade pip
RUN pip install -r /opt/api/requirements.txt

EXPOSE 5000

CMD [ "bash", "./run.sh" ]