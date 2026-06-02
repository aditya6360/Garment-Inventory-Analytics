import pandas as pd
import sqlite3

df = pd.read_csv('cleaned_garment_data.csv')

conn = sqlite3.connect('garment_db.sqlite')

df.to_sql('garments', conn, if_exists='replace', index=False)
 
print("Data base are ready...")

query1 = """
SELECT Category, SUM(Price_INR * Sales_Last_Month) As Total_Revenue
FROM garments
GROUP BY Category
ORDER BY Total_Revenue DESC;
"""
print("1. Which category has the most income")
print(pd.read_sql(query1, conn))
print("-" * 50)

query2 = """
SELECT Brand_Style, Category, Stock_Qty
FROM garments
WHERE Stock_Qty < 20;
"""

print("2. (Low Stock Alert)")
print(pd.read_sql(query2, conn))
print("-" * 50)

query3 = """
SELECT Brand_Style, Category, Sales_Last_Month
FROM garments
ORDER BY Sales_Last_Month DESC
LIMIT 1;
"""
print("3. This month best seller")
print(pd.read_sql(query3, conn))

conn.close()
