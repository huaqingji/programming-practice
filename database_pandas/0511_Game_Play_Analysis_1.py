import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    
    df = activity.groupby(by='player_id').apply(func=lambda df: df.event_date.min()).to_frame('first_login').reset_index()

    return df