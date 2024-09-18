import pandas as pd

def find_cities(cities: pd.DataFrame) -> pd.DataFrame:
    return cities.sort_values(["state", "city"]).groupby("state", as_index=False).agg(cities=('city', ", ".join))