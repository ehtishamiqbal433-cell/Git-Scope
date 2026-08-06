FROM python:3.12-slim

RUN apt-get update && apt-get install -y --no-install-recommends git && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir pytest pytest-cov click

RUN python3 cli/main.py install

ENTRYPOINT ["python3", "cli/main.py"]
CMD ["scan"]
