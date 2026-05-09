# Unemployment Analysis with Python

# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv("Unemployment_Rate_upto_11_2020.csv")

# Display first 5 rows
print("First 5 Rows:")
print(data.head())

# Dataset information
print("\nDataset Info:")
print(data.info())

# Check missing values
print("\nMissing Values:")
print(data.isnull().sum())

# Rename columns for easy access
data.columns = ['States', 'Date', 'Frequency',
                'Estimated Unemployment Rate',
                'Estimated Employed',
                'Estimated Labour Participation Rate',
                'Region', 'Longitude', 'Latitude']

# Convert date column
data['Date'] = pd.to_datetime(data['Date'])

# Display statistical summary
print("\nStatistical Summary:")
print(data.describe())

# Plot unemployment rate
plt.figure(figsize=(12,6))
sns.lineplot(x='Date',
             y='Estimated Unemployment Rate',
             data=data)

plt.title("Unemployment Rate Over Time")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate")
plt.xticks(rotation=45)
plt.show()

# Covid-19 impact analysis
covid_data = data[data['Date'] >= '2020-03-01']

plt.figure(figsize=(12,6))
sns.barplot(x='Region',
            y='Estimated Unemployment Rate',
            data=covid_data)

plt.title("Region-wise Unemployment During Covid-19")
plt.xticks(rotation=45)
plt.show()

# Average unemployment rate by region
avg_unemployment = data.groupby('Region')[
    'Estimated Unemployment Rate'].mean()

print("\nAverage Unemployment Rate by Region:")
print(avg_unemployment)
