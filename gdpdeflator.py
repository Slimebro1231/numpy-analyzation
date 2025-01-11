import pandas as pd
import matplotlib.pyplot as plt

# Read the GDP data file
gdp_file_path = 'gdpdata2.txt'
gdp_data = pd.read_csv(gdp_file_path, delimiter='\t', skiprows=0)

# Extract relevant columns for Nominal GDP, Real GDP, and years
nominal_gdp = gdp_data['NGDPSAXDCCAQ']  # Nominal GDP
real_gdp = gdp_data['NGDPRSAXDCCAQ']  # Real GDP
gdp_data['observation_date'] = pd.to_datetime(gdp_data['observation_date'])  # Ensure observation_date is datetime
years = gdp_data['observation_date'].dt.year  # Convert observation_date to year

# Calculate GDP Deflator
gdp_data['GDP_Deflator'] = (nominal_gdp / real_gdp) * 100
print("Calculated GDP Deflator for each year.")

# Calculate the GDP deflator for the year 2000
gdp_deflator_2000 = gdp_data.loc[years == 2000, 'GDP_Deflator'].values[0]
print(f"GDP Deflator for year 2000: {gdp_deflator_2000:.2f}")

# Recalculate Real GDP at constant 2000 prices
gdp_data['Real_GDP_2000_Prices'] = nominal_gdp * (gdp_deflator_2000 / gdp_data['GDP_Deflator'])
print("Recalculated Real GDP at constant 2000 prices.")

# Extract numbers for the final calculation for 2010
nominal_gdp_2010 = gdp_data.loc[years == 2010, 'NGDPSAXDCCAQ'].values[0]
real_gdp_2010 = gdp_data.loc[years == 2010, 'NGDPRSAXDCCAQ'].values[0]
gdp_deflator_2010 = gdp_data.loc[years == 2010, 'GDP_Deflator'].values[0]
real_gdp_2000_2010 = gdp_data.loc[years == 2010, 'Real_GDP_2000_Prices'].values[0]

# Print details for 2010
print(f"Nominal GDP in 2010: {nominal_gdp_2010:.2f} million CAD")
print(f"Real GDP in 2010 (Original): {real_gdp_2010:.2f} million CAD")
print(f"GDP Deflator in 2010: {gdp_deflator_2010:.2f}")
print(f"Real GDP in 2010 at constant 2000 prices: {real_gdp_2000_2010:.2f} million CAD")

# Plot the main GDP series
plt.figure(figsize=(12, 8))
plt.plot(years, nominal_gdp, label='Nominal GDP', linestyle='-', marker='o', color='red')
plt.plot(years, real_gdp, label='Real GDP (Original Base Year)', linestyle='-', marker='o', color='blue')
plt.plot(years, gdp_data['Real_GDP_2000_Prices'], label='Real GDP (Constant 2000 Prices)', linestyle='--', marker='s', color='green')

# Label differences at each point for Real GDP (Constant 2000 Prices)
for i, year in enumerate(years):
    if i % 3 == 0:  # Label every third year to avoid clutter
        plt.text(year, gdp_data['Real_GDP_2000_Prices'].iloc[i] + 1000, 
                 f"{gdp_data['Real_GDP_2000_Prices'].iloc[i]:.2f}", fontsize=8, color='darkgreen', ha='center')

plt.title('Nominal vs Real GDP: Original Base Year and Constant 2000 Prices', fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('GDP (Millions CAD)', fontsize=14)
plt.legend(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.savefig('gdp_comparison_plot_corrected.png', dpi=300, bbox_inches='tight')
plt.show()
