import pandas as pd
import numpy as np


def add_columns(n,f,df):
    df['date_of_issue']=pd.to_datetime(df['date_of_issue'],format='%d-%m-%Y')
    df['date_of_return']=df['date_of_issue']+pd.Timedelta(days=n)
    today=pd.to_datetime('today')
    df['days_overdue']=(today-df['date_of_return'])
    df['days_overdue']=df['days_overdue'].map(lambda x: str(x)[:-20])
    df['fine_amount']=df['days_overdue'].map(lambda x: int(x)*f)
    df['fine_amount'] = np.where(df['return_status'] == 'yes', 0, df['fine_amount'])
    return df

def search_month(month,df):
    df2=df[df['date_of_issue'].dt.strftime('%m') == month]

    if len(df2)==0:
        return 'Data not found for the given month'

    return df2


def ontime_returns(df):
    df2=df[df['return_status'] == 'yes']

    if len(df2)==0:
        return 'Data not found'

    return df2


def pending_returns(df):
    df2=df[df['return_status'] == 'no']

    if len(df2)==0:
        return 'Data not found'

    return df2

def user_data(user,df):
    df2=df[['student_reg_no','student_name','days_overdue','fine_amount']][df['student_name']==user]

    if len(df2)==0:
        return 'User not found'
    
    return df2

df=pd.read_csv('library_man\Book.csv')


n=int(input('enter the no of days book allocated : '))
f=int(input('Fine per day : '))
print('___________________________________________________')

df=add_columns(n,f,df)

df.to_csv('library_man\sample2.csv',index=False)

action=int(input('Enter 1 to display the entire data \nEnter 2 to display the data based on month \nEnter 3 to display all ontime returns \nEnter 4 to display all pending returns\nEnter 5 to display amount and days overdue based on user \n:'))

if action==1:
    print(df)

elif action==2:
    month=input('Enter month in %m format : ')
    df2=search_month(month,df)
    print(df2)

elif action==3:
    print(ontime_returns(df))


elif action==4:
    print(pending_returns(df))

elif action==5:
    user=input('Enter user name : ')
    print(user_data(user,df))

else:
    print('invalid input')