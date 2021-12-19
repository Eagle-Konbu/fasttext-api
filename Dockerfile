FROM ubuntu as downloader

RUN apt update \
    && apt install -y wget \
    && wget https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.ja.300.vec.gz

FROM python:3.9-slim-buster

WORKDIR /myapp

COPY . .

RUN pip install gensim flask

COPY --from=downloader cc.ja.300.vec.gz ./

EXPOSE 5000

CMD python main.py