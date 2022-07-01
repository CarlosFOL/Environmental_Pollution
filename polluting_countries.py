class PollutingCountries():
    name: str;
    emision_co2: float;       #million tons
    mortality_rate: float;    #decimal percentage
    life_expectency: float;
    pbi: float;               #billion USD
    def __init__(self, name, emision_co2, mortality_rate, life_expectency, pbi):
        self.name = name
        self.emision_co2 = emision_co2
        self.mortality_rate = mortality_rate
        self.life_expectency = life_expectency
        self.pbi = pbi