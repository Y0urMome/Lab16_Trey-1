# Displaying a graph for unemployment rate in Ohio from 1976-2022
# Trey Blue
# 05/04/2025

"""
Plot Ohio unemployment rates (monthly) from a CSV file, with proper date formatting,
grids, and visual styling using matplotlib.

Reads data from 'OHUR.csv' and visualizes monthly unemployment trends from 1976 to 2022.
"""

from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.ticker as mtick
import matplotlib.dates as mdates

# Read and split CSV file into lines
path = Path('OHUR.csv')
lines = path.read_text(encoding='utf-8').splitlines()

# Parse CSV lines using the csv module
reader = csv.reader(lines)
header_row = next(reader)  # Skip header

# Uncomment this block to inspect the CSV column headers and their indices
"""
for index, col_title in enumerate(header_row):
    print(f'{index} {col_title}, ', end='')
print()
"""

# Lists to store parsed date and unemployment rate data
dates = []
unemployment_rates = []

# Extract dates and unemployment rates from each row in the CSV
for row in reader:
    try:
        current_date = datetime.strptime(row[0], '%Y-%m-%d')  # Parse date string
        unemployment_rate = float(row[1])  # Convert rate to float
    except ValueError as e:
        print(current_date)  # Show problematic date if parsing fails
    else:
        dates.append(current_date)
        unemployment_rates.append(unemployment_rate)

# -----------------------
# Visualization Section
# -----------------------

# Use a dark theme for the plot
plt.style.use('dark_background')
figure, graph = plt.subplots()

# Plot the unemployment rate over time
graph.plot(dates, unemployment_rates, color='white')

# Add titles and labels
graph.set_title('Unemployment Rates for Ohio (by Month): 1976–2022', fontsize=20)
graph.set_ylabel('Unemployment Rate (%)', fontsize=16)
graph.set_xlabel('Date', fontsize=16)

# Format tick labels
graph.tick_params(axis='y', labelsize=12)
graph.yaxis.set_major_locator(mtick.MultipleLocator(1))  # Y-axis ticks every 1%

# Format x-axis to show a tick every 2 years, with 4-digit year labels
graph.xaxis.set_major_locator(mdates.YearLocator(2))
graph.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))

# Set x-axis bounds to include full desired date range
start_date = datetime(1975, 1, 1)
end_date = datetime(2023, 1, 1)
graph.set_xlim(start_date, end_date)

# Add light horizontal gridlines for better readability
graph.grid(
    which='major',
    axis='y',
    color='white',
    linestyle='--',
    linewidth=0.4,
    alpha=0.3
)

# Automatically rotate date labels for readability
figure.autofmt_xdate()

# Display the graph
plt.show()
