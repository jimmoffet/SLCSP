import csv
import sys
import collections
import logging
import traceback

log = logging.getLogger(__name__)


def getSilverRatesByRateArea(plans_path: str):
    """
    ARGS: str: path to csv with plan rates for each rate area
    RETURNS: dict: sets of silver plan rates by rate area
    """
    try:
        with open(plans_path, mode="r") as plans:
            silver_rates_by_rate_area = collections.defaultdict(set)
            for row in csv.DictReader(plans):
                if row["metal_level"] == "Silver":
                    state_rate_label = row["state"] + " " + row["rate_area"]
                    silver_rates_by_rate_area[state_rate_label].add(float(row["rate"]))
    except Exception as e:
        log.error("getRateAreasByZipcode() unexpected error %s, with trace: %s", e, traceback.format_exc())
        raise e
    return silver_rates_by_rate_area


def getRateAreasByZipcode(zips_path: str):
    """
    ARGS: str: zips_path - path to csv with zipcodes, states and rate areas
    RETURNS: dict: sets of rate areas by zipcode
    """
    try:
        with open(zips_path, mode="r") as zips:
            rate_areas_by_zipcode = collections.defaultdict(set)
            for row in csv.DictReader(zips):
                rate_areas_by_zipcode[row["zipcode"]].add(row["state"] + " " + row["rate_area"])
    except Exception as e:
        log.error("getRateAreasByZipcode() unexpected error %s, with trace: %s", e, traceback.format_exc())
        raise e
    return rate_areas_by_zipcode


def getBenchmarksByZipcode(zipcode: str, silver_rates_by_rate_area: dict, rate_areas_by_zipcode: dict):
    """
    ARGS:
        str: zipcode
        dict: sets of silver plan rates by rate area
        dict: sets of rate areas by zipcode
    RETURNS: str: benchmark rate
    """
    try:
        rate_area = list(rate_areas_by_zipcode[zipcode])[0]
        rate_output = ""
        if len(rate_areas_by_zipcode[zipcode]) == 1 and rate_area in silver_rates_by_rate_area:
            if len(silver_rates_by_rate_area[rate_area]) >= 2:
                sorted_rates = sorted(silver_rates_by_rate_area[rate_area])
                rate_output = "{:.2f}".format(sorted_rates[1])
    except Exception as e:
        log.error("getBenchmarksByZipcode() unexpected error %s, with trace: %s", e, traceback.format_exc())
        raise e
    return rate_output


def outputBenchmarks(slcsp_path: str, rate_areas_by_zipcode: dict, silver_rates_by_rate_area: dict):
    """
    ARGS:
        str: zipcode
        dict: sets of silver plan rates by rate area
        dict: sets of rate areas by zipcode
    RETURNS: None
    For each target zipcode, writes zipcode and benchmark rate to stdout
    """
    try:
        with open(slcsp_path, mode="r") as slcsp:
            for row in csv.DictReader(slcsp):
                rate = getBenchmarksByZipcode(row["zipcode"], silver_rates_by_rate_area, rate_areas_by_zipcode)
                sys.stdout.write(f'{row["zipcode"]},{rate}\n')
    except Exception as e:
        log.error("outputBenchmarks() unexpected error %s, with trace: %s", e, traceback.format_exc())
        raise e
    return
