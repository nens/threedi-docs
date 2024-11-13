FROM sphinxdoc/sphinx-latexpdf:8.0.2
# Pin the docker tag to use Python 3.12 to work
# around PyPi sub-dependencies with no 3.13 wheels

# ARG DEBIAN_FRONTEND=noninteractive
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     texlive \
#     texlive-latex-recommended \
#     texlive-latex-extra \
#     texlive-fonts-recommended \
#     tex-gyre \
#     dvipng \
#     cm-super \
#     latexmk \
#     && apt-get clean \
#     && rm -rf /var/lib/apt/lists/*
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /code
