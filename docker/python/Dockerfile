FROM python:3.13

RUN apt-get update -y && apt-get upgrade -y

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN pip install uv

RUN uv sync

COPY . .

ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app
