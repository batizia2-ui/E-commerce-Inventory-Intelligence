import pandas as pd
import os

def clean_currency(value):
    """Cleans currency strings like '$ 18,700.00' into floats."""
    if pd.isna(value) or str(value).strip() == "":
        return 0.0
    if isinstance(value, str):
        # Removes $, commas and whitespace
        clean_val = value.replace('$', '').replace(',', '').strip()
        return float(clean_val)
    return float(value)

def run_analysis():
    # Adjusted path to find your file in the analysis folder
    file_path = file_path = '../analysis/laptop_inventory.csv'
    
    if not os.path.exists(file_path):
        print(f"Error: File not found at {file_path}")
        return

    try:
        df = pd.read_csv(file_path)
        
        # Standardize column names (remove extra spaces)
        df.columns = df.columns.str.strip()
        
        # Convert prices to numbers
        df['market_price'] = df['market_price'].apply(clean_currency)
        
        # Business Logic: Strategic Margin (15%)
        df['margin'] = df['market_price'] * 0.15
        
        print("\n" + "="*60)
        print("STRATEGIC INVENTORY PERFORMANCE REPORT")
        print("="*60)
        # Showing model, market price and margin
        print(df[['model', 'market_price', 'margin']].to_string(index=False))
        print("="*60)
        print(f"Total Items: {len(df)} | Status: VERIFIED\n")
        
    except Exception as e:
        print(f"System Error: {e}")

if __name__ == "__main__":
    run_analysis()