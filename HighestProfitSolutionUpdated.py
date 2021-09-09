#Ryan Congdon
#SADA Highest Profit Challenge

import pandas as pd
df = pd.read_csv('data.csv')

#Calculate length of index for original data.csv and assign to 'datarows'
index = df.index
datarows = len(index)

#Drop statement to remove all of the non-numeric values or remove values equal to not applicable
df.drop(df[df['Profit (in millions)'] == "N.A." ].index, inplace = True)

#Save modified data as json file
df.to_json('data2.json')

#Calculate the length of index after removing non-numeric values and assign to 'datatworows'
index2 = df.index
datatworows = len(index2)

#Open new json file created containing only numeric profit types
df = pd.read_json('data2.json')
#Sort statment to sort rows greatest to least by Profit
df = df.sort_values(by = 'Profit (in millions)', ascending=False)
            
#part 3 - print first 20 values after sorting rows greatest to least by Profit
df1 = df.head(20)
print(df1)
 
#Print statements to return answer 1 and answer 2
print('Answer One: ',datarows)
print('Answer Two:',datatworows)
