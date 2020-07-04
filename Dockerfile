FROM python:3.8.3

# WORKDIR /house_price_predict_scratch/src/

# RUN adduser --disabled-password --gecos '' api-user

# ENV FLASK_RUN_HOST 0.0.0.0

ARG PIP_EXTRA_INDEX_URL

WORKDIR /opt/api

ADD ./packages/api /opt/api/
# ADD ./packages/xgboost_model /opt/xgboost_model/
# COPY ./packages/xgboost_model /opt/xgboost_model/
# COPY ./packages/api/ api
# COPY ./packages/xgboost_model/ xgboost_model

# COPY ./packages/xgboost requirements.txt requirements.txt
# COPY ./src/api/run.py run.py

RUN pip install --upgrade pip
# RUN pip install -r xgboost_model/requirements.txt
RUN pip install -r /opt/api/requirements.txt

# RUN chown -R api-user:api-user ./

EXPOSE 5000

ENTRYPOINT [ "python", "/opt/api/run.py" ]