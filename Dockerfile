FROM python:3.8

RUN apt-get update && apt-get install -y tesseract-ocr libtesseract-dev tesseract-ocr-jpn

RUN mkdir -p /home/app/
WORKDIR /home/app/
COPY . .

RUN pip3 install -r requirements.txt
RUN ./test.sh
RUN python3 hello.py

CMD python3 web.py

