import numpy as np
import pandas as pd

df=pd.read_csv('Olympic_EDA/athlete_events.csv')
region_df=pd.read_csv('Olympic_EDA/noc_regions.csv')

df=df[df['Season']=='Summer']

df=df.merge(region_df,on='NOC',how='left')
df.drop_duplicates(inplace=True)

df=pd.concat([df,pd.get_dummies(df['Medal'])],axis=1)
print(df[['NOC','Gold','Silver','Bronze']].head(25))

medal_df=df.drop_duplicates(subset=['Team','NOC','Games','Year','City','Sport','Event','Medal'])
print(medal_df.groupby('NOC').sum()[['Gold','Silver','Bronze']].sort_values('Gold',ascending=False).reset_index().head(25))

def fetch_medal(year,country):
    flag=0
    if year=="Overall"and country=="Overall":
        temp= medal_df
    if year=="Overall"and country!="Overall":
        temp=medal_df[medal_df['region']==country]
    if year!="Overall"and country=="Overall":
        flag=1
        temp= medal_df[medal_df['year']==int(year)]
    if year !="Overall"and country!="Overall":
        temp= medal_df[medal_df['region']==country & medal_df['year']==int(year)]

    if flag==1:
        temp=temp.groupby['Year'].sum()[['Gold','Silver','Bronze']].sort_values('Year',ascending=False).reset_index()
    else:
        temp=temp.groupby['region'].sum()[['Gold','Silver','Bronze']]
    temp['Total']=temp['Gold']+temp['Silver']+temp['Bronze']

