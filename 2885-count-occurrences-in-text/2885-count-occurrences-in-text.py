import pandas as pd

def count_occurrences(files: pd.DataFrame) -> pd.DataFrame:
    bullcount = files['content'].str.contains(r'\sbull\s').sum()
    bearcount = files['content'].str.contains(r'\sbear\s').sum()
    return pd.DataFrame({'word':['bull', 'bear'], 'count':[bullcount, bearcount]})