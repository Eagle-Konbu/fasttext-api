FROM ubuntu as downloader

RUN apt update \
    && apt install -y wget gzip \
    && wget https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.ja.300.bin.gz \
    && gzip -d cc.ja.300.bin.gz

FROM python:3.9-slim-buster

WORKDIR /myapp

COPY main.py requirements.txt ./

RUN pip install requirements.txt

COPY --from=downloader cc.ja.300.bin ./

EXPOSE 5000

CMD python main.py