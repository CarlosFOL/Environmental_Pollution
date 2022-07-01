class PollutingCountries():
    name: str;
    pollution: float;       #percentage
    mortality_rate: int;
    life_expectency: int;
    pbi: float;
    def __init__(self, name, pollution, mortality_rate, life_expectency, pbi):
        self.name = name
        self.pollution = pollution
        self.mortality_rate = mortality_rate
        self.life_expectency = life_expectency
        self.pbi = pbi