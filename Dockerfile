FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends \
      git \
      build-essential \
      curl \
      openssh-client \
      ca-certificates \
 && rm -rf /var/lib/apt/lists/*

# Reconfigure Git to use HTTPS instead of SSH to resolve submodules issue.
RUN git config --global url."https://github.com/".insteadOf "git@github.com:" \
 && pip install --upgrade pip \
 && pip install --no-cache-dir poetry

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false && poetry install

COPY main.py ./
COPY .env ./
COPY app/ ./app/

RUN adduser --disabled-password --gecos '' appuser \
 && chown -R appuser:appuser /app
USER appuser

CMD ["python", "main.py"]
