# COMMENTS

## To run with docker

Ensure that you have the Docker daemon installed. https://www.docker.com/products/docker-desktop

Clone repo and run from root:

`docker build . -t slcsp`
`docker run slcsp python run.py`

Run tests with Docker:

`docker build . -t slcsp`
`docker run slcsp pytest .` (don't forget the period at the end!)

## To run without docker

Clone repo and run from root (using a virtual environment is recommended, tested with python 3.6):
`pip install --no-cache-dir -r requirements.txt`
`python run.py`

Run tests (also from root, after running `pip install` above):
`pytest .`

## Notes

I've included notes.txt to give some insight into my process. I wrote the notes doc (most of it, anyway) before getting started. I didn't actually do proper test-driven dev, given the time constraint, and everything I planned didn't actually get tested. Nonetheless, perhaps it's interesting as an artifact. For some reason, I thought it might be weird to import a less-common library like nose, and use a less-common technique, like test generators, but that's where my head was at.
