FROM sphinxdoc/sphinx-latexpdf

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
