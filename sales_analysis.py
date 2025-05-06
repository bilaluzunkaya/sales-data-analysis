import pandas as pd
import matplotlib.pyplot as plt

# Sample: Load dataset
df = pd.read_csv("sales_data.csv")

# Analyze total sales by month
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Month'] = df['Order Date'].dt.month
monthly_sales = df.groupby('Month').sum()['Sales']

# Plot results
monthly_sales.plot(kind='bar', title='Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.tight_layout()
plt.show()
