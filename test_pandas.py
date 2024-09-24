import pandas as pd

def rank_columns(df):
    # Filter rows where index starts with 'D'
    filtered_df = df[df.index.str.startswith('D')]
    # Rank the columns A, B, and C
    return filtered_df[['A', 'B', 'C']].rank()
