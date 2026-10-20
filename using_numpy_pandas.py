import numpy as np
import pandas as pd

d1 = {
    'A' : [1, 2, np.nan, 4],
    'B' : [5, np.nan, 7, 8],
    'C': [9, None, None, 12]
}
df = pd.DataFrame(d1)
print("missing data is:\n",df.isna())

df_filled = df.fillna(value=0)
print("after filling missing data: \n",df_filled)

d2 = {
    'name' : ['arun','bob','cat','bob'],
    'age' : [20,25,30,25]
}
df = pd.DataFrame(d2)
df_no_duplicates = df.drop_duplicates() #subset = 'name' -- if want to specify column
print("after deleting duplicates: \n",df_no_duplicates)

#-----------------transformation & normalization
d3= {'score': [10,200,300,250]}
df = pd.DataFrame(d3)
df['log_transformed'] = np.log10(df['score'])
df['normalised'] = (df['score']-df['score'].min())/(df['score'].max()-df['score'].min())
print(df)

#mergig, concatinating
df1 = pd.DataFrame({
    'id' : [1,2,3],
    'name' : ['ant', 'bat', 'cat']})
df2 = pd.DataFrame({
    'id' : [1,2,4],
    'size' : [2, 70, 100]})
merged_df = pd.merge(df1,df2, on ='id') #we can also merge using index
print("\nmerged df is: \n",merged_df)

df3 = pd.DataFrame({
    'name' : ['raj', 'ben', 'ten'],
    'age' : [20,30,20]
})
df4 = pd.DataFrame({
    'name' : ['ellen', 'dan'],
    'age' : [45,35]    
})
concat_df = pd.concat([df3,df4])
print("\nconcatinated df is: \n",concat_df)

#applying functions....
df = pd.DataFrame({
    'A' : [1,2,3],
    'B' : [4,5,6]
})
result_df = df.applymap(lambda x: x*2)
print(df)
print("after applying function is:\n",result_df)

#----------------Data visualisation-----------------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'day' : ['MON', 'TUE', 'WED', 'THU', 'FRI'],
    'temperature' : [25, 27, 20, 30, 25]
}
df = pd.DataFrame(data)
df.plot(x = 'day', y = 'temperature', kind = 'bar', color= 'green')
plt.title('temperature trend of week')
plt.xlabel('week of the day')
plt.ylabel('temperature in degrees')
plt.show()

#------multiple subplots on same figure
fig, axs = plt.subplots(2, 2)  # 2x2 grid of subplots

# Plot on each subplot
axs[0, 0].plot([1, 2, 3], [1, 4, 9])
axs[0, 0].set_title('Plot 1')

axs[0, 1].plot([1, 2, 3], [1, 2, 3])
axs[0, 1].set_title('Plot 2')

axs[1, 0].plot([1, 2, 3], [1, 0, 1])
axs[1, 0].set_title('Plot 3')

axs[1, 1].plot([1, 2, 3], [3, 2, 1])
axs[1, 1].set_title('Plot 4')

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plots
plt.show()

#-----seaborn-----------statastical visualization
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Sample data
data1 = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [5, 4, 3, 2, 1],
    'category': ['A', 'B', 'A', 'B', 'A']
})

# Create a scatter plot
sns.scatterplot(data=data1, x='x', y='y', hue='category')

# Show the plot
plt.show()


# Sample data
data2 = pd.DataFrame({
    'category': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B'],
    'value': [10, 20, 15, 25, 10, 30, 15, 20]
})

# Create a categorical plot
sns.catplot(data=data2, x='category', y='value', kind='bar')

# Show the plot
plt.show()

#-----------basic datetime module----------------
import datetime

# Current date and time
now = datetime.datetime.now()
print("Current date and time:", now)

# Specific date and time
specific_date = datetime.datetime(2025, 2, 14, 21, 30)
print("Specific date and time:", specific_date)

# Date arithmetic
today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)
print("Tomorrow's date:", tomorrow)

# Difference between dates
date1 = datetime.date(2025, 2, 14)
date2 = datetime.date(2025, 3, 1)
delta = date2 - date1
print("Days between dates:", delta.days)

# Formatting dates
date_str = "2025-02-14"
date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
print("Parsed date object:", date_obj)

formatted_date_str = date_obj.strftime("%B %d, %Y")
print("Formatted date string:", formatted_date_str)

# Current time
current_time = datetime.datetime.now().time()
print("Current time:", current_time)

# Specific time
specific_time = datetime.time(21, 30, 0)
print("Specific time:", specific_time)

#------------regular expressionfor data cleaning
import re

# Sample data
data = [
    'John Doe: 123-456-7890',
    'Jane Smith: (123) 456-7890',
    'Jim Brown: 123.456.7890',
    'Jake White: 1234567890'
]

# Define a regex pattern to match different phone number formats
pattern = re.compile(r'\D')

# Clean the phone numbers
cleaned_data = [re.sub(pattern, '', entry) for entry in data]

print(cleaned_data)