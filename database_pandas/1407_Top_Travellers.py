import pandas as pd

def top_travellers(users: pd.DataFrame, rides: pd.DataFrame) -> pd.DataFrame:
    
    df = pd.merge(
        left=users, right=rides,
        how='left',
        left_on='id', right_on='user_id',
        suffixes=('_left', '_right')
    )

    df = df.groupby(by=['id_left', 'name']).apply(func=lambda df: df.distance.sum()).to_frame('travelled_distance').reset_index()[['name', 'travelled_distance']]

    df.sort_values(by=['travelled_distance', 'name'], ascending=[False, True], inplace=True)

    return df