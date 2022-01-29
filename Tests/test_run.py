import csv
import itertools
from BenchmarkFinder.utils import getRateAreasByZipcode, getSilverRatesByRateArea, getBenchmarksByZipcode

# TODO substitute zips and plans with sample data that have tricky features, would be easier after
# separating out extract and transform steps

rate_areas_by_zipcode = getRateAreasByZipcode("data/zips.csv")
silver_rates_by_rate_area = getSilverRatesByRateArea("data/plans.csv")


def test_rate_area_filtering():
    """assert ground-truth-determined rate areas for some zipcode"""
    assert rate_areas_by_zipcode["48872"] == {"MI 7", "MI 4", "MI 5"}


def test_silver_plan_filtering():
    """assert ground-truth-determined rates for some rate area"""
    assert silver_rates_by_rate_area["WV 9"] == {278.90, 295.05, 291.76, 295.63}


def test_multiple_rate_area_fail():
    """assert rate is blank for zip 48418, which is split across MI 4 and MI 5"""
    benchmark_rate = getBenchmarksByZipcode("48418", silver_rates_by_rate_area, rate_areas_by_zipcode)
    rate_areas_list = rate_areas_by_zipcode["48418"]
    assert rate_areas_list == {"MI 4", "MI 5"} and benchmark_rate == ""


def test_rate_for_zip():
    """assert ground truth determined rate from some zip"""
    benchmark_rate = getBenchmarksByZipcode("31551", silver_rates_by_rate_area, rate_areas_by_zipcode)
    assert benchmark_rate == "290.60"


def test_too_few_plans():
    """assert rate is blank for zip with only one silver plan"""
    target_zip = "07184"
    benchmark_rate = getBenchmarksByZipcode(target_zip, silver_rates_by_rate_area, rate_areas_by_zipcode)
    rate_areas_set = rate_areas_by_zipcode[target_zip]
    assert len(rate_areas_set) == 1
    rates_set = silver_rates_by_rate_area[rate_areas_set.pop()]
    assert rates_set == {262.65} and benchmark_rate == ""


def test_second_lowest_dupes():
    """assert ground truth rate for zip with duplicate plan prices"""
    benchmark_rate = getBenchmarksByZipcode("52654", silver_rates_by_rate_area, rate_areas_by_zipcode)
    assert benchmark_rate == "242.39"


def test_sample_output():
    """assert ground truth second lowest rate for first ten zipcodes from manual audit"""
    first_ten_manual_audit = {
        "64148": "245.20",
        "67118": "212.35",
        "40813": "",
        "18229": "231.48",
        "51012": "252.76",
        "79168": "243.68",
        "54923": "",
        "67651": "249.44",
        "49448": "221.63",
        "27702": "283.08",
    }
    with open("data/slcsp.csv", mode="r") as slcsp:
        for row in itertools.islice(csv.DictReader(slcsp), 10):
            benchmark_rate = getBenchmarksByZipcode(row["zipcode"], silver_rates_by_rate_area, rate_areas_by_zipcode)
            assert first_ten_manual_audit[row["zipcode"]] == benchmark_rate
