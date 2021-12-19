FROM ubuntu as downloader

RUN apt update \
    && apt install -y wget \
    && wget https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.ja.300.bin

FROM python:3.9-slim-buster

WORKDIR /myapp

COPY main.py .

RUN pip install gensim flask

COPY --from=downloader cc.ja.300.bin ./

EXPOSE 5000

CMD python main.py