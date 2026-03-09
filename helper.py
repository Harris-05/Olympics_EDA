import pandas as pd


def medal_tally(df):
    medal_df=df.drop_duplicates(subset=['Team','NOC','Games','Year','City','Sport','Event','Medal'])
    medal_df=medal_df.groupby('region').sum()[['Gold','Silver','Bronze']].sort_values('Gold',ascending=False).reset_index()
    medal_df['total']=medal_df['Gold']+medal_df['Silver']+medal_df['Bronze']
    medal_df=medal_df.sort_values('total',ascending=False)
    return medal_df
