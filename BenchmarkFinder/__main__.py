import argparse
from utils import getSilverRatesByRateArea, getRateAreasByZipcode, outputBenchmarks

parser = argparse.ArgumentParser(
    description="BenchmarkFinder calculates the second-lowest cost silver plan for each of a set of target zipcodes."
)

parser.add_argument("-z", "--zipmap", help="Path to csv with mapping of zipcodes to state & rate area")
parser.add_argument("-p", "--plans", help="Path to csv with plan rates for each rate area")
parser.add_argument("-t", "--targets", help="Path to csv with zipcodes for which to output benchmarks")

args = parser.parse_args()

zips_path = args.zipmap if args.zipmap else "data/zips.csv"
plans_path = args.plans if args.plans else "data/plans.csv"
slcsp_path = args.targets if args.targets else "data/slcsp.csv"

if __name__ == "__main__":
    """main entry point"""

    rate_areas_by_zipcode = getRateAreasByZipcode(zips_path)
    silver_rates_by_rate_area = getSilverRatesByRateArea(plans_path)
    outputBenchmarks(slcsp_path, rate_areas_by_zipcode, silver_rates_by_rate_area)
