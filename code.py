# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
data = pd.read_csv(path)
#print(data.columns)
#Code starts here
data.rename({'Total':'Total_Medals'},axis=1,inplace=True)
print(data.columns)
print(data.head())


# --------------
#Code starts here






data['Better_Event'] = np.where(data['Total_Summer']>data['Total_Winter'],'Summer','Winter')
data['Better_Event'] =np.where(data['Total_Summer'] ==data['Total_Winter'],'Both',data['Better_Event'])

print(data.head())
better = pd.DataFrame(data['Better_Event'].value_counts())
better.reset_index(inplace=True)
print(better)
print(better.index)
print(better.columns)
better_event = better[better['Better_Event'] == (better['Better_Event'].max())]['index'].value_counts()


better_event ='Summer'
print(better_event)


# --------------
#Code starts here
print(data.columns)


top_countries = pd.DataFrame(data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']])
#print(top_countries.shape)
top_countries.drop(top_countries.tail(1).index,inplace=True)
#print(top_countries.tail())
def top_ten(top_countries,column_name):
    country_list = []
    top10 = top_countries.nlargest(10,column_name)
    country_list = list(top10['Country_Name'])
    return country_list

top_10_summer = top_ten(top_countries,'Total_Summer')
top_10_winter = top_ten(top_countries,'Total_Winter')
top_10 = top_ten(top_countries,'Total_Medals')

print(top_10_summer)
print(top_10_winter)
print(top_10)
common_10 = top_10_summer+top_10_winter+top_10
common = []
for x in common_10:
    if common_10.count(x) == 3:
        if x not in common:
           common.append(x)
print(common)




# --------------
#Code starts here
summer_df = data[data['Country_Name'].isin(top_10_summer)]
#print(summer_df.head())
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df =data[data['Country_Name'].isin(top_10)]

plt.bar(summer_df['Country_Name'],summer_df['Total_Summer'])
plt.bar(winter_df['Country_Name'],winter_df['Total_Summer'])
plt.bar(top_df['Country_Name'],top_df['Total_Summer'])


# --------------
#Code starts here
print(summer_df.head(2))
summer_df['Golden_Ratio'] = summer_df['Gold_Summer']/summer_df['Total_Summer']
winter_df['Golden_Ratio'] = winter_df['Gold_Winter']/winter_df['Total_Winter']
top_df['Golden_Ratio'] = top_df['Gold_Total']/top_df['Total_Medals']
#print(summer_df.head())
summer_max_ratio = summer_df['Golden_Ratio'].max()
print(summer_max_ratio)
summer_country_gold  = summer_df.loc[summer_df['Golden_Ratio'].idxmax(),'Country_Name']
print(summer_country_gold)
winter_max_ratio = winter_df['Golden_Ratio'].max()
print(winter_max_ratio)
winter_country_gold = winter_df.loc[winter_df['Golden_Ratio'].idxmax(),'Country_Name']
print(winter_country_gold)
top_max_ratio = top_df['Golden_Ratio'].max()
print(top_max_ratio)
top_country_gold = top_df.loc[top_df['Golden_Ratio'].idxmax(),'Country_Name']
print(top_country_gold)



# --------------
#Code starts here
data_1 = data
data_1.drop(data_1.tail(1).index,inplace=True)
#print(data_1.tail(2))


data_1['Total_Points'] = 3*(data_1['Gold_Total']) +  2*(data_1['Silver_Total']) + (data_1['Bronze_Total'])
#print(data_1['Total_Points'])
most_points = data_1['Total_Points'].max()
print(most_points)
best_country = data_1.loc[data_1['Total_Points'].idxmax(),'Country_Name']
print(best_country)



# --------------
#Code starts here

best = data[data['Country_Name'] == best_country]
#best.head()
best = best[['Gold_Total','Silver_Total','Bronze_Total']]
best.plot.bar()
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)


