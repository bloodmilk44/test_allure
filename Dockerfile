# first stage
FROM python:latest AS builder

ARG run_env
ENV env $run_env

RUN mkdir -p /home
WORKDIR /home/space_x_api_autotest

COPY . .

RUN pip install --root-user-action=ignore -r requirements.txt

CMD pytest -m "$env" -v /home/space_x_api_autotest/test/test_roadster.py