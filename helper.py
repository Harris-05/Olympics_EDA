import pandas as pd

def medal_tally(df, year, country):
    flag = 0
    medal_df = df.drop_duplicates(subset=['Team','NOC','Games','Year','City','Sport','Event','Medal'])
    
    if year == "Overall" and country == "Overall":
        temp = medal_df
    if year == "Overall" and country != "Overall":
        flag = 1
        temp = medal_df[medal_df['region'] == country]
    if year != "Overall" and country == "Overall":
        temp = medal_df[medal_df['Year'] == int(year)] 
    if year != "Overall" and country != "Overall":
        
        temp = medal_df[(medal_df['region'] == country) & (medal_df['Year'] == int(year))]

    if flag == 1:
        
        temp = temp.groupby('Year').sum()[['Gold','Silver','Bronze']].sort_values('Year', ascending=False).reset_index()
        temp['Total'] = temp['Gold'] + temp['Silver'] + temp['Bronze']
    else:
        
        temp = temp.groupby('region').sum()[['Gold','Silver','Bronze']]
        temp['Total'] = temp['Gold'] + temp['Silver'] + temp['Bronze']
        temp=temp.sort_values('Total',ascending=False).reset_index()
        
    

    return temp