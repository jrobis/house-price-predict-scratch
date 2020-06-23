FROM python:3.8.3

# WORKDIR /house_price_predict_scratch/src/

# RUN adduser --disabled-password --gecos '' api-user

# ENV FLASK_RUN_HOST 0.0.0.0

ADD ./src/api/ api
ADD ./src/xgboost_model xgboost_model

COPY requirements.txt requirements.txt
COPY ./src/api/run.py run.py

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# RUN chown -R api-user:api-user ./

EXPOSE 5000

ENTRYPOINT [ "python", "run.py" ]