import pandas as pd

# Simulating the data as the URL can't be accessed directly
data = {
    'YearHalf': ['2015H1', '2015H2', '2016H1', '2016H2', '2017H1', '2017H2', '2018H1', '2018H2', 
                 '2019H1', '2019H2', '2020H1', '2020H2', '2021H1', '2021H2', '2022H1', '2022H2', 
                 '2023H1', '2023H2'],
    'Consumption_1': [3000, 3200, 3100, 3300, 3400, 3500, 3550, 3600, 3650, 3700, 3750, 3800, 3850, 3900, 3950, 4000, 4050, 4100],
    'Consumption_2': [2000, 2100, 2200, 2300, 2400, 2450, 2500, 2550, 2600, 2650, 2700, 2750, 2800, 2850, 2900, 2950, 3000, 3050],
    'Consumption_3': [4000, 4200, 4300, 4400, 4500, 4600, 4650, 4700, 4750, 4800, 4850, 4900, 4950, 5000, 5050, 5100, 5150, 5200],
    'Consumption_4': [1500, 1600, 1700, 1800, 1900, 1950, 2000, 2050, 2100, 2150, 2200, 2250, 2300, 2350, 2400, 2450, 2500, 2550],
    'Consumption_5': [1000, 1100, 1200, 1300, 1400, 1450, 1500, 1550, 1600, 1650, 1700, 1750, 1800, 1850, 1900, 1950, 2000, 2050]
}

df = pd.DataFrame(data)
df