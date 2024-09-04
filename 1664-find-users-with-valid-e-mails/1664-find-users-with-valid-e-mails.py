import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    valid_mails = users[users.mail.str.match('^[A-Za-z][A-Za-z0-9_\.\-]*@leetcode(\.com$)')]
    return valid_mails
    