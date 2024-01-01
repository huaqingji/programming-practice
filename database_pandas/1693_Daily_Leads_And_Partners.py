import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    
    def apply_func(df):

        s = pd.Series(
            data = [df.lead_id.nunique(), df.partner_id.nunique()],
            index = ['unique_leads', 'unique_partners']
        )
        return s

    df = daily_sales.groupby(by=['date_id', 'make_name']).apply(func=apply_func).reset_index()

    return df