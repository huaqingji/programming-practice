import pandas as pd

def sellers_with_no_sales(customer: pd.DataFrame, orders: pd.DataFrame, seller: pd.DataFrame) -> pd.DataFrame:
    
    df = pd.merge(
        left=seller,
        right=orders[orders.sale_date.dt.year == 2020],
        how='left',
        left_on='seller_id',
        right_on='seller_id'
    )

    df = df[df.order_id.isnull()][['seller_name']]
    df.sort_values(by='seller_name', ascending=True, inplace=True)

    return df