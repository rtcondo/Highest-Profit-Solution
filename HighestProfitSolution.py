#Ryan Congdon
#SADA Highest Profit Challenge

import pandas as pd
df = pd.read_csv('data.csv')

#Drop statement to remove all of the non-numeric values or remove values equal to not applicable
df.drop(df[df['Profit (in millions)'] == "N.A." ].index, inplace = True)

#Save modified data as json file
df.to_json('data2.json')

#print amount of rows for table two
index = df.index
datatworows = len(index)

#df = df.sort_values(['Profit (in millions)'], ascending=False, inplace=False)
df = df.sort_values(by = 'Profit (in millions)', ascending=False)


#Count all rows in initial CSV
import csv
with open('C:\\Users\\rtc31\\Desktop\\Sada Solution\\data.csv') as x:
    data = csv.reader(x)
    rows = 0
    for row in data:
        if row != "\n":
            rows += 1
            
#part 3, print top 20 profits
df1 = df.head(20)
print(df1)
 
print('Answer One: ',rows)
print('Answer Two: ',datatworows)