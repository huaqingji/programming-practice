import pandas as pd

def highest_grade(enrollments: pd.DataFrame) -> pd.DataFrame:
    
    def apply_func(df):
        s = df.sort_values(by=['grade', 'course_id'], ascending=[False, True]).iloc[0]
        return s

    df = enrollments.groupby(by=['student_id']).apply(apply_func).reset_index(drop=True)

    df.sort_values(by=['student_id'], inplace=True)

    return df