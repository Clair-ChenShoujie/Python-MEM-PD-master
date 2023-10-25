import pandas as pd

data = pd.read_excel('2023test1/B1/attachment1.xlsx')

# Assuming data is a pandas DataFrame
cities = sorted(list(set(data['Receiving city'].unique()) | set(data['Delivering city'].unique())))

df1 = data.groupby(['Date Y/M/D', 'Delivering city'])['Express delivery quantity (PCS)'].sum().reset_index()
df2 = data.groupby(['Date Y/M/D', 'Receiving city'])['Express delivery quantity (PCS)'].sum().reset_index()

# Rename the columns for merging
df1.rename(columns={'Delivering city': 'City', 'Express delivery quantity (PCS)': 'Delivery Quantity'}, inplace=True)
df2.rename(columns={'Receiving city': 'City', 'Express delivery quantity (PCS)': 'Receiving Quantity'}, inplace=True)

# Merge the two dataframes on Date and City
merged_df = pd.merge(df1, df2, on=['Date Y/M/D', 'City'], how='outer')
merged_df.fillna(0, inplace=True)

# Sum the Delivery and Receiving Quantities to get total quantity
merged_df['Total Quantity'] = merged_df['Delivery Quantity'] + merged_df['Receiving Quantity']

# Save the dataframe to an excel file
merged_df.to_excel('2023test1/B1/Q1时间序列.xlsx', index=False)