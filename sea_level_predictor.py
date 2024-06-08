import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Import data
df = pd.read_csv('epa-sea-level.csv')

# Create scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Original Data')

# Create first line of best fit for the entire dataset
slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
years_extended = pd.Series([i for i in range(1880, 2051)])
sea_level_pred = intercept + slope * years_extended
plt.plot(years_extended, sea_level_pred, 'r', label='Best Fit Line 1880-2050')

# Create second line of best fit using data from 2000 onwards
df_recent = df[df['Year'] >= 2000]
slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
years_recent = pd.Series([i for i in range(2000, 2051)])
sea_level_pred_recent = intercept_recent + slope_recent * years_recent
plt.plot(years_recent, sea_level_pred_recent, 'g', label='Best Fit Line 2000-2050')

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')
plt.legend()

# Save and show the plot
plt.savefig('sea_level_plot.png')
plt.show()
