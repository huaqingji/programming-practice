import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    
    if len(orders) == 0:
        return pd.DataFrame(columns=['customer_number'])

    df = orders.groupby(by='customer_number').apply(func=lambda df: len(df)).to_frame('cnt').reset_index()

    df = df.sort_values(by='cnt', ascending=False).head(1)[['customer_number']]

    return df