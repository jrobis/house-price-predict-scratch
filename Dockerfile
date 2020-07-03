FROM python:3.8.3

# WORKDIR /house_price_predict_scratch/src/

# RUN adduser --disabled-password --gecos '' api-user

# ENV FLASK_RUN_HOST 0.0.0.0

ARG PIP_EXTRA_INDEX_URL

COPY ./packages/api/ api
COPY ./packages/xgboost_model/ xgboost_model

# COPY ./packages/xgboost requirements.txt requirements.txt
# COPY ./src/api/run.py run.py

RUN pip install --upgrade pip
# RUN pip install -r xgboost_model/requirements.txt
RUN pip install -r api/requirements.txt

# RUN chown -R api-user:api-user ./

EXPOSE 5000

ENTRYPOINT [ "python", "api/run.py" ]