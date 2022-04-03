#!/bin/bash

[ ! -d "env/" ] && python3 -m venv ./env
source env/bin/activate
python -m pip install --upgrade pip
pip3 install -r requirements.txt
scrapy runspider quipoquiz_spider.py -O out/extract.json