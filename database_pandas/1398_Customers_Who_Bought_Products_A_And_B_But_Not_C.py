import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    
    df = pd.merge(
        left=customers, right=orders,
        how='inner',
        left_on='customer_id', right_on='customer_id'
    )

    def filter_func(df):
        return sum(df.product_name == 'A') > 0 and sum(df.product_name == 'B') > 0 and sum(df.product_name == 'C') == 0

    df = df.groupby(by=['customer_id']).filter(filter_func).drop_duplicates(subset=['customer_id'])

    df = df[['customer_id', 'customer_name']].sort_values(by=['customer_id'])

    return df