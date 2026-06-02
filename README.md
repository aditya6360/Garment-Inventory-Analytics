# Garment Inventory Analytics 👕👖

This project analyzes garment inventory data, cleanses missing values, and prepares it for reporting and business intelligence. It simulates a retail inventory environment using Python and SQLite.

## Project Overview
- **Data Cleaning**: Handled missing `Stock_Qty` and imputed missing `Price_INR` values using category averages via Pandas.
- **Data Pipeline**: Cleaned data exported into a ready-to-use CSV file (`cleaned_garment_data.csv`).
- **Database Integration**: Managed inventory data using an SQLite database (`garment_db.sqlite`), using custom SQL queries to extract insights.

## Technologies Used
- **Python** (Pandas)
- **SQL** (SQLite)
- **Power BI** (For Dashboarding - *Add your Power BI screenshot here*)

## Files Included
- `garment_analytics.py`: Python script for data loading, cleaning, and transformation.
- `garment_data.csv.csv`: Raw inventory data.
- `cleaned_garment_data.csv`: Processed data ready for visualization.
- `garment_db.sqlite`: Database file storing the inventory.
- `sql_queries.py`: SQL scripts for analysis.

## How to Run
```bash
python garment_analytics.py
```
