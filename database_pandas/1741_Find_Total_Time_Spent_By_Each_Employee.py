import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    
    df = employees.groupby(by=['emp_id', 'event_day']).apply(func=lambda df: (df.out_time - df.in_time).sum()).to_frame('total_time').reset_index()

    df.rename(columns={'event_day': 'day'}, inplace=True)
    return df[['day', 'emp_id', 'total_time']]