import matplotlib.pyplot as plt

# Plotting the overall increase in energy consumption for all categories
plt.figure(figsize=(12, 8))

for column in df.columns[1:]:
    plt.plot(df['YearHalf'], df[column], marker='o', label=column)

plt.title('Energy Consumption Trends (2015H1 - 2023H2)')
plt.xlabel('YearHalf')
plt.ylabel('Energy Consumption (KWH)')
plt.xticks(rotation=45)
plt.legend(title='Consumption Category')
plt.grid(True)
plt.tight_layout()

# Show the plot
plt.show()