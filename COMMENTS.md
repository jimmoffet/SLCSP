# COMMENTS

BenchmarkFinder calculates the benchmark rate (the second lowest cost silver plan) for set of target zip codes.

## Usage

```
usage: BenchmarkFinder [-h] [-z ZIPMAP] [-p PLANS] [-t TARGETS]

BenchmarkFinder calculates the second-lowest cost silver plan for each of a
set of target zipcodes.

optional arguments:
  -h, --help            show this help message and exit
  -z ZIPMAP, --zipmap ZIPMAP
                        Path to csv with mapping of zipcodes to state & rate
                        area
  -p PLANS, --plans PLANS
                        Path to csv with plan rates for each rate area
  -t TARGETS, --targets TARGETS
                        Path to csv with zipcodes for which to output
                        benchmarks
```

## Run with docker

Clone repo and run from root:

```
docker build . -t slcsp_container
docker run slcsp_container python BenchmarkFinder
```

Run tests:

```
docker build . -t slcsp_container
docker run slcsp_container pytest .
```

## Run without docker

Clone repo and run from root (using a virtual environment is recommended, tested with python 3.9):

```
pip install --no-cache-dir -r requirements.txt
python BenchmarkFinder
```

Run tests:

```
pytest .
```

## Notes

I used google sheets to quickly explore the data and validate my understanding of the task. Producing a sample result manually was helpful: https://docs.google.com/spreadsheets/d/10J8u-pMhguTqqX8l1N0yOkqvkb6FzbzpIbaxiZv4LwE/edit?usp=sharing
