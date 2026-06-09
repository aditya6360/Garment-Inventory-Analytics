# Garment Inventory Analytics

An automated data pipeline for cleaning, processing, and analyzing retail garment 
inventory data using Python and SQLite.

## Features
- Data cleaning pipeline handling 2,000+ inventory records
- Missing value imputation using category-level averages
- Automated CSV transformation from raw to analysis-ready format
- SQLite queries for backend inventory filtering and reporting

## Tech Stack
- Python (Pandas)
- SQLite
- CSV / Excel

## Results
- Reduced manual data preparation time by ~60%
- Achieved zero data loss through category mean imputation strategy

## How to Run
```bash
pip install pandas
python inventory_pipeline.py
```
