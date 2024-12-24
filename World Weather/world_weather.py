import pandas as pd

df = pd.read_csv('C:/Users/Tharika Kavindi/Desktop/World Weather/GlobalWeatherRepository.csv')

print(df.head())
print(df.info())

# Check for missing values
print(df.isnull().sum())

# Drop rows or fill missing values
df = df.dropna()  # or df.fillna(value)
df['last_updated'] = pd.to_datetime(df['last_updated'])
print(df.describe())

import matplotlib.pyplot as plt

# Average temperature per country
avg_temp = df.groupby('country')['temperature_celsius'].mean()

# Plot
avg_temp.sort_values().plot(kind='bar', figsize=(10, 6), color='skyblue')
plt.title("Average Temperature by Country")
plt.xlabel("Country")
plt.ylabel("Temperature (°C)")
plt.show()

import seaborn as sns

# Select numerical columns
numeric_cols = ['temperature_celsius', 'humidity', 'pressure_mb', 'wind_kph', 'uv_index']

# Correlation heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(df[numeric_cols].corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()

plt.figure(figsize=(8, 5))
sns.scatterplot(x='humidity', y='temperature_celsius', data=df, hue='country', alpha=0.7)
plt.title("Humidity vs Temperature")
plt.xlabel("Humidity (%)")
plt.ylabel("Temperature (°C)")
plt.show()

air_quality = df.groupby('country')['air_quality_us-epa-index'].mean()

air_quality.plot(kind='bar', figsize=(12, 6), color='green')
plt.title("Average Air Quality Index by Country (US EPA)")
plt.xlabel("Country")
plt.ylabel("Air Quality Index")
plt.show()

# Group by date and calculate daily average temperature
df['date'] = df['last_updated'].dt.date
daily_temp = df.groupby('date')['temperature_celsius'].mean()

# Plot daily trends
plt.figure(figsize=(12, 6))
plt.plot(daily_temp, color='red')
plt.title("Daily Average Temperature Trend")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.show()

df['sunrise'] = pd.to_datetime(df['sunrise'], format='%H:%M:%S').dt.time
df['sunset'] = pd.to_datetime(df['sunset'], format='%H:%M:%S').dt.time

print(df[['location_name', 'sunrise', 'sunset']].head())

df.to_csv("cleaned_weather_data.csv", index=False)
