from datetime import datetime
from functools import reduce
from polluting_countries import PollutingCountries
import pytz
from typing import Dict, List, Tuple

def report(func):
    def wrapper(*args, **kwargs) -> str:
        lima_pytz = pytz.timezone("America/Lima")
        lima_time = datetime.now(lima_pytz).strftime("%d/%m/%Y ,%H:%M:%S")
        univ_time = datetime.utcnow()
        print(f"""Lima, Peru: {lima_time}
Universal time: {univ_time}""")
        print("By calculating the results...")
        print(f"""
----------------------------------------------------------------
CO2 EMISSIONS IN COUNTRIES VS OTHERS FACTORS

Countries with...
High CO2 emissions and high GDP: {func(*args, **kwargs)[0].intersection(func(*args, **kwargs)[6])}
High GDP and low CO2 emissions: {func(*args, **kwargs)[6].intersection(func(*args, **kwargs)[2])}
High mortality rate and high CO2 emissions: {func(*args, **kwargs)[2].intersection(func(*args, **kwargs)[0])}
-----------------------------------------------------------------
""")
        print("Finished :)")
    return wrapper

def cleaning_data(data_sets: List[set[str]]) -> List[set[str]]:
    for i in data_sets:
        i.discard(None)
    return data_sets

def high_or_low(country: object, avg: Tuple[float], approach: str, type: str) -> str:
    approaches_dict: Dict[str, List[object, int]] = {
        "e": [country.emision_co2, 0],
        "m": [country.mortality_rate, 1],
        "l": [country.life_expectency, 2],
        "p": [country.gdp, 3]
    }
    for k, v in approaches_dict.items():
        if k == approach:
            if type == "h":
                if v[0] >= avg[v[1]]:
                    return country.name
            elif type == "l":
                if v[0] < avg[v[1]]:
                    return country.name

@report
def clasification(avg: Tuple[float], list: List[object]) -> List[set[str]]:
    high_emision, low_emision = set(), set()
    high_mortality, low_mortality = set(), set()
    high_life, low_life= set(), set()
    high_gdp, low_gdp = set(), set()
    for i in  list:
        high_emision.add(high_or_low(i, avg, "e", "h")), low_emision.add(high_or_low(i, avg, "e", "l"))
        high_mortality.add(high_or_low(i, avg, "m", "h")), low_mortality.add(high_or_low(i, avg, "m", "l"))
        high_life.add(high_or_low(i, avg, "l", "h")), low_life.add(high_or_low(i, avg, "l", "l"))
        high_gdp.add(high_or_low(i, avg, "p", "h")), low_gdp.add(high_or_low(i, avg, "p", "l"))
    data_set: List[set(str)] = [
        high_emision, low_emision,
        high_mortality, low_mortality, 
        high_life, low_life, 
        high_gdp, low_gdp
        ]
    return cleaning_data(data_set)

def average(list: List[float]) -> float:
    result: float = round(reduce(lambda e_1, e_2: e_1+e_2, list)/len(list),2) # e = element
    return result

def approaches(countries_list: List[object]) -> Tuple[float]:
    emision_co2: float = average([x.emision_co2 for x in countries_list])
    mortality_rate: float = average([x.mortality_rate for x in countries_list])
    life_expectency: float = average([x.life_expectency for x in countries_list])
    gdp: float = average([x.gdp for x in countries_list])
    return emision_co2, mortality_rate, life_expectency, gdp

if __name__=='__main__':
    china: object = PollutingCountries("China",9889.3, 7.07, 77.1, 14.72)
    usa: object = PollutingCountries("USA",4457.2, 10.3, 77.28, 20.94)
    india: object = PollutingCountries("India",2302.3, 7.3, 69.89, 2.623)
    russia: object = PollutingCountries("Russia",1482.2, 14.6, 71.34, 1.483)
    japan: object = PollutingCountries("Japan",1027.0, 11.1, 84.62, 4.422)
    iran: object = PollutingCountries("Iran",678.2, 4.84, 76.86, 0.1917)
    germany: object = PollutingCountries("Germany",604.9, 11.9, 81.1, 3.806)
    countries_list: List[object] = [china, usa, india, russia, japan, iran, germany]
    clasification(approaches(countries_list), countries_list)