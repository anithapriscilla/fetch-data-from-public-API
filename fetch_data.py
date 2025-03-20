import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Load the dataset
url = "https://raw.githubusercontent.com/novrian6/dataanalysis-dataset/master/WHO-COVID-19-global-data.csv"
df = pd.read_csv(url, delimiter=';')
# Display the first few rows
print(df.head())
# Convert 'Date_reported' to datetime format
df['Date_reported'] = pd.to_datetime(df['Date_reported'], format='%d/%m/%Y')
# Plot cumulative cases over time for a specific country
df_country = df[df['Country'] == 'Italy']
plt.figure(figsize=(12, 6))
plt.plot(df_country['Date_reported'], df_country['Cumulative_cases'], marker='o', linestyle='-', color='b', label='Cumulative Cases')
plt.xlabel('Date')
plt.ylabel('Cumulative Cases')
plt.title('Cumulative COVID-19 Cases in Italy')
plt.legend()
plt.grid(True)
plt.show()

