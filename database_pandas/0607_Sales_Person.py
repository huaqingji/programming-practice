import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    
    df_ord = pd.merge(
        left=orders,
        right=company[company.name == 'RED'],
        how='inner',
        left_on='com_id', right_on='com_id'
    )[['order_id', 'sales_id']]

    df = pd.merge(
        left=sales_person, right=df_ord,
        how='left',
        left_on='sales_id', right_on='sales_id'
    )

    df = df[df.order_id.isnull()][['name']]
    return df