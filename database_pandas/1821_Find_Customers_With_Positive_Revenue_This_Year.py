import pandas as pd

def find_customers(customers: pd.DataFrame) -> pd.DataFrame:
    
    df = customers[(customers.year == 2021) & (customers.revenue > 0)][['customer_id']]

    return df