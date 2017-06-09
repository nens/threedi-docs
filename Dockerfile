FROM python:3

COPY requirements.txt ./
RUN apt-get update && apt-get install -y \
    texlive \
    texlive-latex-extra \
    dvipng \
    latexmk

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /code
VOLUME /code