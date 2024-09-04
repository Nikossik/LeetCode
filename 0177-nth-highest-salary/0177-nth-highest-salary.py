import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    if N <= 0:
        return pd.DataFrame({'getNthHighestSalary({})'.format(N): [None]})
    uniq = employee.salary.drop_duplicates()
    sorted_sal = uniq.sort_values(ascending=False)
    if N > len(sorted_sal):
        return pd.DataFrame({'getNthHighestSalary({})'.format(N): [None]})
    nth = sorted_sal.iloc[N-1]
    return pd.DataFrame({'getNthHighestSalary({})'.format(N): [nth]})