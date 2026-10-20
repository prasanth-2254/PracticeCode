import pandas as pd
"""
d1 = {
    'name' : ['raj', 'ravi', 'ben'],
    'age' : [20,30,40],
    'country' : ['USA','UK','India']
}
df1 = pd.DataFrame(d1)
print(df1)

d2 = [
    ['raj', 25],
    ['ben', 30],
    ['ron', 25]
]
df = pd.DataFrame(d2,columns=['name','age'])
print(df)

age_column = df['age'] #indexing, selection
print(age_column)


df.loc[len(df)] = ['Dave',25] #adding data
print(df)

df = df[df['name']!='raj'] #removing data
print(df)

df.loc[df['name']=='ben','age'] = 26 #updating data
print("\n after updating age: \n",df)

print(df.isna()) #missing data --displays true if any empty cell

print('\nsorting, filtering, grouping')
sorted_data = df1.sort_values(by= 'name') #sorting
print(sorted_data)

filtered_data = df[df['age']>25] #filtering
print(filtered_data)
"""
d3 = {
    'name' : ['Hen', 'Ben', 'Don'],
    'salary' : [40000, 60000, 70000],
    'department' : ['DE','DA','DE']
}
df = pd.DataFrame(d3)
print(df)
grouped_data = df.groupby('department')['salary'].mean()
print(grouped_data)

"""
#import , export data 
df.to_csv('data.csv',index = False) #df stored to csv file
print("DataFrame exported to 'data.csv'")

df = pd.read_csv('data.csv') #
print('imported dataFrame is: ')
print(df.head()) #displays first 5 rows

import pandas as pd # passing col names externally
salesDF = pd.read_csv("C:/Users/prasanth.mukkamala/Downloads/salesdata.csv",delimiter=",",names=['ProductName','QuantitySold','ProfitMargin','Area'])
print(salesDF)

#-------------------------time series-----------------------------
d4 = {
    'date' : ['2025-01-01', '2025-01-02', '2025-01-03', '2025-01-05', '2025-01-04'],
    'values' : [10,20,40,17,22]
}
df =pd.DataFrame(d4)
df['date'] = pd.to_datetime(df['date'])

df.set_index('date',inplace = True)
df.sort_index(inplace=True)
print(df)

monthly_df = df.resample('ME').mean()  #shows 31 days -- january
print(monthly_df)

#working with dates, times in pandas
d5 = {
    'date':['2025-01-01','2025-01-02'],
    'values':[20,40]
}
df = pd.DataFrame(d5)
df['date'] = pd.to_datetime(df['date'])
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day
print(df) #to see dd, mm, yy

#time series analysis & manipulation
d6 = {
    'date' : pd.date_range(start='2025-01-01', periods=5, freq='D'),
    'values' : [10,20,30,40,50]
}
df = pd.DataFrame(d6)
#df.set_index('date',inplace = True)
print(df)
"""