import pandas as pd

data={
    'name':['bibin','shri','srujan'],
    'mark':[80,99,95]
}

df=pd.DataFrame(data)
print(df)
print('__________________________')
print(df['name'])
print('__________________________')

s=pd.Series(data)
print(s)
print('__________________________')
print(s[0])
print('__________________________')


df.index=['s1','s2','s3']
print(df)
print('__________________________')

print(df.iloc[0])
print('__________________________')

print(df.loc['s1'])
print('__________________________')
print(df.loc[(df.mark>90)])
print('__________________________')


df2=pd.read_csv('..\..\..\..\..\Downloads\industry.csv')
print(df2)


