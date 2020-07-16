import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date
import datetime as dt
from pandas_datareader import data as wb

df = pd.DataFrame()
resultado = pd.DataFrame()
observation_size = 252
peso= [0.375,0.625]

df = pd.read_excel(r'C:\Users\jpbar\OneDrive\Área de Trabalho\fundos_quant.xlsx' )


df = df.set_index('Data')
df['IBOVESPA'] = wb.get_data_yahoo('^BVSP',start='2000-01-01' , end= str(date.today()), interval='d')['Adj Close']

#Ordeno da mais antiga para a mais nova data
df = df.sort_values(by='Data')



#Combinando fundos
#df_aux= df[['FIM Sigma','FIM Darius']].dropna()
#df_aux["Darius + Sigma"]= np.dot((df[['FIM Sigma','FIM Darius']].dropna() / df[['FIM Sigma','FIM Darius']].dropna().iloc[0]),peso)
#df["Darius + Sigma"] = df_aux["Darius + Sigma"]


#df_aux_ = df[['FIM KADIMA','FIM Darius']].dropna()
#df_aux_["Kadima + Darius"]= np.dot((df[['FIM KADIMA','FIM Darius']].dropna() / df[['FIM KADIMA','FIM Darius']].dropna().iloc[0]),peso)
#df["Kadima + Darius"] = df_aux_["Kadima + Darius"]


for t in df:
    df['return ' + t] = df[t].values[-1] / df[t]
    df['n_days ' + t] = np.arange(df.shape[0])[::-1]
    df['return ' + (t)] = df['return ' + t] ** (observation_size / df['n_days '+ t]) - 1
    resultado[t] = df['return ' + (t)] * 100

print(resultado)
# Plotando o gráfico

cutoff = df.shape[0]-(observation_size)


start = resultado.index.searchsorted(dt.datetime(2015, 11, 1))
for t  in df.columns[5:]:
    try:
            plt.plot( resultado[(t)][start:int(cutoff)], linewidth=1.3,label=t)
    except:
        pass


plt.ylabel("Retorno em " + str(round(observation_size,0)) + " dias úteis")
plt.grid()
plt.legend()
plt.show()



