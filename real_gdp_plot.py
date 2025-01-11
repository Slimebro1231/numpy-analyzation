import pandas as pd
import matplotlib.pyplot as plt

# Read the GDP data file and skip the first line
gdp_file_path = 'gdpdata.txt'  
gdp_data = pd.read_csv(gdp_file_path, delimiter='\t', skiprows=0)

# Extract relevant columns for Real and Nominal GDP and Population
real_gdp = gdp_data['NGDPRSAXDCCAQ']  # Real GDP
nominal_gdp = gdp_data['NGDPSAXDCCAQ']  # Nominal GDP
population = gdp_data['POPTOTCAA647NWDB']  # Population
years = pd.to_datetime(gdp_data['observation_date']).dt.year  # Convert observation_date to year

# Calculate growth rates for each year
real_gdp_growth = real_gdp.pct_change() * 100  # Percentage change for Real GDP
nominal_gdp_growth = nominal_gdp.pct_change() * 100  # Percentage change for Nominal GDP
population_growth = population.pct_change() * 100  # Percentage change for Population

# Print yearly growth rates
print("Yearly Growth Rates:")
for year, rg, ng, pg in zip(years[1:], real_gdp_growth[1:], nominal_gdp_growth[1:], population_growth[1:]):
    print(f"Year: {year}, Real GDP Growth: {rg:.2f}%, Nominal GDP Growth: {ng:.2f}%, Population Growth: {pg:.2f}%")

# Get and print growth rates for 2015
real_gdp_growth_2015 = real_gdp_growth[years == 2015].values[0]
nominal_gdp_growth_2015 = nominal_gdp_growth[years == 2015].values[0]

print(f"\nReal GDP Growth Rate in 2015: {real_gdp_growth_2015:.2f}%")
print(f"Nominal GDP Growth Rate in 2015: {nominal_gdp_growth_2015:.2f}%")

# Plotting Real GDP
plt.figure(figsize=(8, 6))
plt.plot(years, real_gdp, marker='o', markersize=4, linestyle='-', linewidth=1.5, color='black', label='Real GDP')

# Add grid, title, labels, and legend
plt.title('Real GDP Over Time in Canada (2003-2023)', fontsize=14, pad=10)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Real GDP (Millions CAD)', fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.grid(visible=True, which='major', linestyle='--', linewidth=0.5, alpha=0.7)
plt.legend(fontsize=10, loc='best', frameon=False)

# Remove extra padding and make the layout tight
plt.tight_layout()

# Save the figure in a high-resolution format (useful for academic papers)
plt.savefig('real_gdp_plot.png', dpi=300, bbox_inches='tight')

# Show the plot
plt.show()