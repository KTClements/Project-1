import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = "Crime_Data_from_2020_to_Present.csv"
data = pd.read_csv(file_path)

# Preview the dataset
print(data.head())

# Angle 1: Crime Trends Over Time
# Convert the 'DATE OCC' column to datetime
data['DATE OCC'] = pd.to_datetime(data['DATE OCC'], format='%m/%d/%Y %I:%M:%S %p')

# Group by Year-Month to calculate the number of crimes per month
data['YearMonth'] = data['DATE OCC'].dt.to_period('M')
crime_trends = data.groupby('YearMonth').size()

# Plotting Crime Trends Over Time
plt.figure(figsize=(10, 6))
plt.plot(crime_trends.index.astype(str), crime_trends.values, marker='o', linestyle='-', color='b')
plt.title('Crime Trends Over Time in Los Angeles (2020-Present)')
plt.xlabel('Month')
plt.ylabel('Number of Incidents')
plt.xticks(rotation=90)
plt.grid(True)
plt.tight_layout()
plt.show()

# Angle 2: Geographical Distribution of Crime
# Group the data by 'AREA NAME' to get the number of incidents per area
geo_distribution = data.groupby('AREA NAME').size()

# Plotting Geographical Distribution of Crime
plt.figure(figsize=(10, 6))
geo_distribution.sort_values(ascending=False).plot(kind='bar', color='green')
plt.title('Geographical Distribution of Crime in Los Angeles')
plt.xlabel('Area Name')
plt.ylabel('Number of Incidents')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Angle 3: Types of Crimes and Their Frequency
# Group the data by 'Crm Cd Desc' to get the frequency of each crime type
crime_types = data['Crm Cd Desc'].value_counts()

# Plotting Types of Crimes and Their Frequency
plt.figure(figsize=(10, 6))
crime_types[:10].plot(kind='bar', color='red')  # Show the top 10 crime types
plt.title('Top 10 Crime Types in Los Angeles')
plt.xlabel('Crime Type')
plt.ylabel('Number of Incidents')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Save the analysis results to CSV files for further reference
crime_trends.to_csv('crime_trends.csv')
geo_distribution.to_csv('geo_distribution.csv')
crime_types.to_csv('crime_types.csv')