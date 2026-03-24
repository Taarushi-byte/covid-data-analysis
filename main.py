import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("owid-covid-data.csv")

# Filter India data
india_df = df[df['location'] == 'India']

# Convert date column
india_df['date'] = pd.to_datetime(india_df['date'])

# Select needed columns
india_df = india_df[['date', 'total_cases', 'total_deaths']]

# Drop missing values
india_df = india_df.dropna()

# Create plot
plt.figure(figsize=(12,6))

plt.plot(india_df['date'], india_df['total_cases'], label="Total Cases")
plt.plot(india_df['date'], india_df['total_deaths'], label="Total Deaths")

# Labels & title
plt.title("COVID-19 Trend in India")
plt.xlabel("Date")
plt.ylabel("Count")

plt.legend()
plt.grid()

# Save image (IMPORTANT)
plt.savefig("covid_india_trend.png")

# Show graph
plt.show()