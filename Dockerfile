FROM python:3

RUN apt-get update && apt-get install -y \
    texlive \
    texlive-latex-extra \
    dvipng \
    latexmk

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /code
VOLUME /code
