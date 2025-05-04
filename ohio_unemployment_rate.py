from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.ticker as mtick
import matplotlib.dates as mdates

path = Path('OHUR.csv')
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

"""
for index, col_title in enumerate(header_row):
    print(f'{index} {col_title}, ', end='')
print()
"""

# Processing info from file

dates = []
unemployment_rates = []

for row in reader:
    try:
        current_date = datetime.strptime(row[0], '%Y-%m-%d')
        unemployment_rate = float(row[1])
    except ValueError as e:
        print(current_date)
    else:
        dates.append(current_date)
        unemployment_rates.append(unemployment_rate)

# Graphing processed info

plt.style.use('dark_background')
figure, graph = plt.subplots()


graph.plot(dates, unemployment_rates, color='white')


plt.show()