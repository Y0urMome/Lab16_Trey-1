from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path = Path('sitka_weather_07-2018_simple.csv')
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# for index, col_title in enumerate(header_row):
#     print(f'{index} {col_title}, ', end='')
# print()

# Processing info from file

dates = []
high_temps = []
low_temps = []

for row in reader:
    high = int(row[5])
    low = int(row[6])
    high_temps.append(high)
    low_temps.append(low)

# Graphing processed info

plt.style.use('dark_background')
figure, graph = plt.subplots()

graph.plot(high_temps, color='red')

plt.show()