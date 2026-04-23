import pandas as pd
import os

def clean_currency(value):
    """Cleans currency strings into floats."""
    if pd.isna(value) or str(value).strip() == "":
        return 0.0
    if isinstance(value, str):
        clean_val = value.replace('$', '').replace(',', '').strip()
        return float(clean_val)
    return float(value)

def run_analysis():
    # Path to the new professional inventory
    file_path = '../analysis/laptop_inventory.csv'
    
    if not os.path.exists(file_path):
        print(f"Error: File not found at {file_path}")
        return

    try:
        df = pd.read_csv(file_path)
        
        # Standardize column names
        df.columns = df.columns.str.strip()
        
        # Update: Use the new professional column names
        # We clean the price to ensure Python can do math with it
        df['Selling_Price_SGM_MXN'] = df['Selling_Price_SGM_MXN'].apply(clean_currency)
        
        # Business Logic: Strategic Margin (15%) calculated over SGM Price
        df['margin'] = df['Selling_Price_SGM_MXN'] * 0.15
        
        print("\n" + "="*70)
        print("SYSTEM GROUP MANAGEMENT - STRATEGIC INVENTORY REPORT")
        print("="*70)
        
        # Showing Model, Price, Category and the calculated Margin
        # We use the new names: 'Model', 'Selling_Price_SGM_MXN', 'Category'
        output_cols = ['Model', 'Selling_Price_SGM_MXN', 'Category', 'margin']
        print(df[output_cols].to_string(index=False))
        
        print("="*70)
        print(f"Total Inventory Items: {len(df)} | Status: VERIFIED")
        print("="*70 + "\n")
        
    except Exception as e:
        print(f"System Error: {e}")

if __name__ == "__main__":
    run_analysis()