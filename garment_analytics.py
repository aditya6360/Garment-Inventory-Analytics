import pandas as pd

print("डेटा लोड हो रहा है...")
df = pd.read_csv('garment_data.csv.csv')


df.columns = df.columns.str.strip()
df['Category'] = df['Category'].str.strip()

print("Orignal data ---")
print(df)


df['Stock_Qty'] = df['Stock_Qty'].fillna(0)


df['Price_INR'] = df['Price_INR'].fillna(df.groupby('Category')['Price_INR'].transform('mean'))


df['Price_INR'] = df['Price_INR'].fillna(df['Price_INR'].mean())

print(" (Cleaned Data) ---")
print(df)


df.to_csv('cleaned_garment_data.csv', index=False)
print("Conrats data are cleaned 'cleaned_garment_data.csv' ")