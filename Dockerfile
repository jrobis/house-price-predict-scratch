FROM python:3.8.3

ARG PIP_EXTRA_INDEX_URL

WORKDIR /opt/api

COPY ./packages/api/ /opt/api/

RUN pip install --upgrade pip
RUN pip install -r /opt/api/requirements.txt

EXPOSE 5000

ENTRYPOINT [ "python", "/opt/api/run.py" ]