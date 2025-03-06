import pandas as pd
import matplotlib.pyplot as plt

csv_file_path = 'Messi_Ronaldo.csv'

# Read data from CSV
data = pd.read_csv(csv_file_path)

# Sort DataFrame by 'Year' column in ascending order
data = data.sort_values(by='Year')

# Plotting the time series line chart
plt.figure(figsize=(20, 6))
plt.plot(data['Year'], data['Messi Goals'], marker='o', linestyle='-', color='b', label='Messi Goals')
plt.plot(data['Year'], data['Ronaldo Goals'], marker='o', linestyle='-', color='r', label='Ronaldo Goals')

# Adding labels and title
plt.xlabel('Year')
plt.ylabel('Values')
plt.title('Time Series Line Chart - Goals')

# Adding legend
plt.legend()

# Rotate x-axis labels
plt.xticks(rotation=45)

# Display the plot
plt.grid(True)
plt.show()
