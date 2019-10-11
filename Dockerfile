FROM python:3

RUN apt-get update && apt-get install -y --no-install-recommends \
    texlive \
    texlive-latex-extra \
    dvipng \
    latexmk \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /code
VOLUME /code
