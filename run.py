import csv
import sys
import collections
# TODO: Pandas...

def getBenchmark(zipcode, silver_rates_by_rate_area, rate_areas_by_zipcode):
    rate_area = list(rate_areas_by_zipcode[zipcode])[0]
    if len( rate_areas_by_zipcode[zipcode] ) == 1 and rate_area in silver_rates_by_rate_area:
        if len( silver_rates_by_rate_area[rate_area] ) >= 2:
            sorted_rates = sorted(silver_rates_by_rate_area[rate_area])
            return ("{:.2f}".format(sorted_rates[1]), silver_rates_by_rate_area[rate_area], rate_areas_by_zipcode[zipcode])
    return ("", silver_rates_by_rate_area[rate_area], rate_areas_by_zipcode[zipcode])

if __name__ == '__main__':
    """main entry point"""

    with open('data/zips.csv', mode='r') as zips:
        rate_areas_by_zipcode = collections.defaultdict(set)
        _ = {rate_areas_by_zipcode[row["zipcode"]].add(row["state"]+" "+row["rate_area"]) for row in csv.DictReader(zips)}

    with open('data/plans.csv', mode='r') as plans:
        silver_rates_by_rate_area = collections.defaultdict(set)
        _ = {silver_rates_by_rate_area[row["state"]+" "+row["rate_area"]].add(float(row["rate"])) for row in csv.DictReader(plans) if row["metal_level"] == "Silver"}

    with open('data/slcsp.csv', mode='r') as slcsp:
        for row in csv.DictReader(slcsp):
            sys.stdout.write(f'{row["zipcode"]},{getBenchmark(row["zipcode"], silver_rates_by_rate_area, rate_areas_by_zipcode)[0]}\n')
