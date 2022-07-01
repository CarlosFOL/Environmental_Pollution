from functools import reduce
from polluting_countries import PollutingCountries

def high_or_low(country, avg, approach, type):
    approaches_dict = {
        "e": country.emision_co2,
        "m": country.mortality_rate,
        "l": country.life_expectency,
        "p": country.pbi
    }
    for k, v in approaches_dict.items():
        if k == approach:
            if type == "h":
                if v >= avg:
                    return country.name
            elif type == "l":
                if v < avg:
                    return country.name

def clasification(avg, list):
    high_emision, low_emision = set(), set()
    high_mortality, low_mortality = set(), set()
    high_life, low_life= set(), set()
    high_pbi, low_pbi = set(), set()
    for i in  list:
        high_emision.add(high_or_low(i, avg[0], "e", "h")), low_emision.add(high_or_low(i, avg[0], "e", "l"))
        high_mortality.add(high_or_low(i, avg[1], "m", "h")), low_mortality.add(high_or_low(i, avg[1], "m", "l"))
        high_life.add(high_or_low(i, avg[2], "l", "h")), low_life.add(high_or_low(i, avg[2], "l", "l"))
        high_pbi.add(high_or_low(i, avg[3], "p", "h")), low_pbi.add(high_or_low(i, avg[3], "p", "l"))
    data_set = [
        high_emision, low_emision,
        high_mortality, low_mortality, 
        high_life, low_life, 
        high_pbi, low_pbi
        ]
    return data_set

def average(list):
    result = round(reduce(lambda e_1, e_2: e_1+e_2, list)/len(list),2) # e = element
    return result

def approaches(countries_list):
    emision_co2 = average([x.emision_co2 for x in countries_list])
    mortality_rate = average([x.mortality_rate for x in countries_list])
    life_expectency = average([x.life_expectency for x in countries_list])
    pbi = average([x.pbi for x in countries_list])
    return emision_co2, mortality_rate, life_expectency, pbi

if __name__=='__main__':
    china = PollutingCountries("China",9889.3, 7.07, 77.1, 14.72)
    usa = PollutingCountries("USA",4457.2, 10.3, 77.28, 20.94)
    india = PollutingCountries("India",2302.3, 7.3, 69.89, 2.623)
    russia = PollutingCountries("Russia",1482.2, 14.6, 71.34, 1.483)
    japan = PollutingCountries("Japan",1027.0, 11.1, 84.62, 4.422)
    iran = PollutingCountries("Iran",678.2, 4.84, 76.86, 0.1917)
    germany = PollutingCountries("Germany",604.9, 11.9, 81.1, 3.806)
    countries_list = [china, usa, india, russia, japan, iran, germany]
    answer = clasification(approaches(countries_list), countries_list)
    for i in answer:
        print(i)