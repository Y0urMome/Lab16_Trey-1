from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path = Path('sitka_weather_2018_full.csv')
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
    try:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[8])
        low = int(row[9])
    except ValueError as e:
        print(current_date)
    else:
        dates.append(current_date)
        high_temps.append(high)
        low_temps.append(low)

# Graphing processed info

plt.style.use('dark_background')
figure, graph = plt.subplots()

graph.plot(dates, high_temps, color='red')
graph.plot(dates, low_temps, color='blue')
graph.fill_between(dates, high_temps, low_temps, color='lightblue', alpha=0.5)

graph.set_title('Daily Temps for 2018 in Sitka, Alaska', fontsize=24)
graph.set_ylabel('Temperature (F)', fontsize=16)
figure.autofmt_xdate()

plt.show()