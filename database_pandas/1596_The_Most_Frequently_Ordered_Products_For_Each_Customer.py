import pandas as pd

def most_frequently_products(customers: pd.DataFrame, orders: pd.DataFrame, products: pd.DataFrame) -> pd.DataFrame:
    
    df = pd.merge(
        left=orders,
        right=products,
        how='inner',
        left_on='product_id',
        right_on='product_id'
    )

    df_freq = df.groupby(by=['customer_id', 'product_id', 'product_name']).apply(
        lambda df: len(df)).to_frame('freq').reset_index()

    df_freq_max = df_freq.groupby(by=['customer_id']).apply(
        lambda df: df.freq.max()).to_frame('max').reset_index()

    df = pd.merge(
        left=df_freq,
        right=df_freq_max,
        how='inner',
        left_on=['customer_id', 'freq'],
        right_on=['customer_id', 'max']       
    )[['customer_id', 'product_id', 'product_name']]

    return df