import pandas as pd

def accepted_candidates(candidates: pd.DataFrame, rounds: pd.DataFrame) -> pd.DataFrame:
    rounds = rounds.groupby(by='interview_id', as_index=False)['score'].sum()

    table = candidates.merge(rounds, on='interview_id', how='outer')
    table = table[
        (table['years_of_exp'] >= 2) & (table['score'] > 15)
        ]
    
    return table[['candidate_id']]

    