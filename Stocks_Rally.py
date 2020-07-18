import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import numpy as np
import pandas_datareader as wb


df = pd.read_excel(r'C:\Users\jpbar\OneDrive\Área de Trabalho\South_Sea.xlsx')
df.drop(columns=['Date'],inplace=True)
df= df.fillna(method='ffill')
df['South Sea Company']= df['South Sea Company'][0: df['South Sea Company'].idxmax()]

df_tesla= wb.get_data_yahoo('TSLA')[['Adj Close']] #Baixando tesla
df_tesla.sort_index(ascending=True,inplace=True)
df_tesla.reset_index(inplace=True)
df_tesla.drop(columns=['Date'],inplace=True)
df_tesla.drop(df_tesla.index[0:970],inplace=True)
df_tesla.reset_index(inplace=True)

df_cisco= wb.get_data_yahoo('CSCO', start='1997-04-11',end='2000-03-24')[['Adj Close']] #Baixando tesla
df_cisco.sort_index(ascending=True,inplace=True)
df_cisco.reset_index(inplace=True)
df_cisco.drop(columns=['Date'],inplace=True)
df_cisco.drop(df_cisco.index[0:375],inplace=True)
df_cisco.reset_index(inplace=True)

df_btc= wb.get_data_yahoo('BTC-USD', start='2017-05-03',end='2017-12-10')[['Adj Close']] #Baixando tesla
df_btc.sort_index(ascending=True,inplace=True)
df_btc.reset_index(inplace=True)
df_btc.drop(columns=['Date'],inplace=True)
#df_btc.drop(df_cisco.index[0:375],inplace=True)
#df_btc.reset_index(inplace=True)






df = pd.concat([df['South Sea Company'],df_tesla['Adj Close'],df_cisco['Adj Close'],df_btc['Adj Close']],keys=['South Sea Company','TESLA','CISCO','BITCOIN'],axis=1)

df = df/ df.iloc[0] * 100

plt.style.use(['seaborn-bright'])
plt.plot(df['South Sea Company'], label= 'South Sea Company')
plt.plot(df['TESLA'], label= 'TESLA')
plt.plot(df['CISCO'], label= 'CISCO')
plt.plot(df['BITCOIN'], label= 'BITCOIN', )
plt.legend(loc='upper left')

plt.show()