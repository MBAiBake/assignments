from load_csv_lib import load_csv

features = {}
features["area"] = load_csv("world_factbook/geography/area.csv")
features["population"] = load_csv("world_factbook/people_and_society/population.csv")
features["median age"] = load_csv("world_factbook/people_and_society/median_age.csv")
features["life expectancy"] = load_csv("world_factbook/people_and_society/life_expectancy_at_birth.csv")
features["gdp"] = load_csv("world_factbook/economy/real_gdp_purchasing_power_parity.csv")

def test_us_pop_rank():
    assert features["population"]["united states"][0] == "3", "US population rank test"

def test_chile_life_exp_val():
    assert features["life expectancy"]["chile"][1] == "79.57", "Chile life expectancy value test"
    
def test_sa_area_val():
    assert features["area"]["south africa"][1] == "1,219,090", "South Africa area value test"

def test_median_age_dict_size():
    assert len(features["median age"]) == 226, "Median Age dictionary size test"

def test_china_gdp_rank():
    assert features["gdp"]["china"][0] == "1", "China gdp rank test"   
