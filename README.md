# tesseract-prediciton-web
## How to run
```
docker build -t mytess .
docker run -it --rm -p 5000:5000 mytess
```

## How to test with running a docker container
```
```

## How to run `tesseract` command inside a docker container
```
docker run -it --rm --entrypoint bash mytess
```

* Run the `test.sh` inside the docker container
```
./test.sh
```

The result will be 
```
Estimating resolution as 456
Japanese language
Estimating resolution as 622
日本語
```

* Run `python3 hello.py` inside the docker container, the result will be
```
日本語
```

