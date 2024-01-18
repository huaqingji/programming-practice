import pandas as pd

def project_employees(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    
    df_merge = pd.merge(
        left=project, right=employee,
        how='inner',
        on='employee_id'
    )

    df_max_exp = df_merge.groupby(by='project_id').apply(lambda df: df.experience_years.max()).to_frame('max_exp').reset_index()

    df = pd.merge(
        left=df_merge, right=df_max_exp,
        how='inner',
        left_on=['project_id', 'experience_years'],
        right_on=['project_id', 'max_exp']
    )[['project_id', 'employee_id']]

    return df