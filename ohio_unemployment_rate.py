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
graph.set_title('Unemployment Rates for Ohio (by Month): 1976-2022', fontsize=20)
graph.set_ylabel('Unemployment Rate (%)', fontsize=16)
graph.set_xlabel('Dates', fontsize=16)
graph.tick_params(axis='y', labelsize=12)
graph.xaxis.set_major_locator(mdates.YearLocator(2))  # tick every 2 years
graph.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
graph.yaxis.set_major_locator(mtick.MultipleLocator(1))
start_date = datetime(1975, 1, 1)
end_date = datetime(2023, 1, 1)
graph.set_xlim(start_date, end_date)
graph.grid(which='major', axis='y', color='white', linestyle='--', linewidth=0.4,alpha=0.3)
figure.autofmt_xdate()

plt.show()