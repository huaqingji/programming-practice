import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    
    if len(employee) == 0:
        return pd.DataFrame(columns=['Department', 'Employee', 'Salary'])

    df_highest_salary = employee.groupby(by='departmentId').apply(func=lambda df: df.salary.max()).to_frame('highest_salary').reset_index()

    df_emp = pd.merge(
        left=employee,
        right=df_highest_salary,
        how='inner',
        left_on=['departmentId', 'salary'],
        right_on=['departmentId', 'highest_salary']
    )[['departmentId', 'name', 'salary']].rename(columns={'name': 'Employee', 'salary': 'Salary'})

    df = pd.merge(
        left=df_emp, right=department,
        how='inner',
        left_on='departmentId', right_on='id'
    )[['name', 'Employee', 'Salary']].rename(columns={'name': 'Department'})

    return df