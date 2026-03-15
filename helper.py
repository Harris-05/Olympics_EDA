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

def most_successful(df, country):
    temp_df = df.dropna(subset=['Medal'])
    temp_df = temp_df[temp_df['region'] == country]
    
    counts = temp_df['Name'].value_counts().reset_index().head(15)
    counts.columns = ['Name', 'Medals'] 
    
    x = counts.merge(df, on='Name', how='left')[['Name', 'Medals', 'Sport']].drop_duplicates('Name')
    
    return x

def yearwise_medal(df, country):
    temp_df = df.dropna(subset=['Medal'])
    
    temp_df = temp_df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])

    temp_df = temp_df[temp_df['region'] == country]
    final_df = temp_df.groupby('Year').count()['Medal'].reset_index()
    
    final_df = final_df.sort_values('Year', ascending=True)
    
    return final_df