import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    
    df = actor_director.groupby(by=['actor_id', 'director_id']).filter(func=lambda df: len(df) >= 3)

    df = df[['actor_id', 'director_id']].drop_duplicates()

    return df