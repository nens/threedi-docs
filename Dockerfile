FROM python:3

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpaper1 \
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
