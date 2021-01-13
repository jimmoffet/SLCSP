import csv
import pytest
from run import *

#TODO substitute zips and plans with curated sample data that has tricky features
with open('data/zips.csv', mode='r') as zips:
    rate_areas_by_zipcode = collections.defaultdict(set)
    _ = {rate_areas_by_zipcode[row["zipcode"]].add(row["state"]+" "+row["rate_area"]) for row in csv.DictReader(zips)}

with open('data/plans.csv', mode='r') as plans:
    silver_rates_by_rate_area = collections.defaultdict(set)
    _ = {silver_rates_by_rate_area[row["state"]+" "+row["rate_area"]].add(float(row["rate"])) for row in csv.DictReader(plans) if row["metal_level"] == "Silver"}

def test_rate_area_filtering():
    """assert ground truth determined rate areas for some zipcode"""
    assert rate_areas_by_zipcode["48872"] == {'MI 7', 'MI 4', 'MI 5'}

def test_silver_plan_filtering():
    """assert ground truth determined count of rates for some rate area"""
    assert silver_rates_by_rate_area["WV 9"] == {278.90, 295.05, 291.76, 295.63}

def test_multiple_rate_area_fail():
    """assert rate is blank for zip 48418, which is split across MI 4 and MI 5"""
    benchmark = getBenchmark("48418", silver_rates_by_rate_area, rate_areas_by_zipcode)
    assert benchmark[2] == {'MI 4', 'MI 5'} and benchmark[0] == ""

def test_rate_for_zip():
    """assert ground truth determined rate from some zip"""
    benchmark = getBenchmark("31551", silver_rates_by_rate_area, rate_areas_by_zipcode)
    assert benchmark[0] == '290.60'

def test_too_few_plans():
    """assert rate is blank for zip with only one silver plan"""
    benchmark = getBenchmark("07184", silver_rates_by_rate_area, rate_areas_by_zipcode)
    assert benchmark[1] == {262.65} and benchmark[0] == ''

def test_second_lowest_dupes():
    """assert rate ground truth rate for zip with duplicate plan prices"""
    benchmark = getBenchmark("52654", silver_rates_by_rate_area, rate_areas_by_zipcode)
    assert benchmark[0] == '242.39'
