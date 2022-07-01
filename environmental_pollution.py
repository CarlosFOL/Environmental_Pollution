from functools import reduce
from polluting_countries import PollutingCountries

def clasification():
    pass

def average(countries_list):
    result = round(reduce(lambda e_1, e_2: e_1+e_2, countries_list)/len(countries_list),2) # e = element
    return result

def approaches(countries_list):
    emision_co2 = average([x.emision_co2 for x in countries_list])
    mortality_rate = average([x.mortality_rate for x in countries_list])
    life_expectency = average([x.life_expectency for x in countries_list])
    pbi = average([x.pbi for x in countries_list])
    return emision_co2, mortality_rate, life_expectency, pbi

if __name__=='__main__':
    china = PollutingCountries(9889.3, 7.07, 77.1, 14.72)
    usa = PollutingCountries(4457.2, 10.3, 77.28, 20.94)
    india = PollutingCountries(2302.3, 7.3, 69.89, 2.623)
    russia = PollutingCountries(1482.2, 14.6, 71.34, 1.483)
    japan = PollutingCountries(1027.0, 11.1, 84.62, 4.422)
    iran = PollutingCountries(678.2, 4.84, 76.86, 0.1917)
    germany = PollutingCountries(604.9, 11.9, 81.1, 3.806)
    countries_list = [china, usa, india, russia, japan, iran, germany]
    var = clasification(approaches(countries_list))