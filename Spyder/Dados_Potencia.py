# -*- coding: utf-8 -*-

import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
#import matplotlib.dates as mpl_dates

path = '/home/kr0pt/Documents/Pesquisa/Codes/Dados/Dados_JPS_12B1(01_01_2008-0h0m--31_12_2013-23h45m).csv'
df_bruto = pd.read_csv(path, sep=';')

df_bruto.drop('Unnamed: 6', inplace=True, axis=1)


#Criando um novo dataframe para que as modificações desejadas sejam feitas

df = pd.DataFrame(columns=['Tempo','Potencia']) 

#Adicionando todas as datas do DF, modificados para o "formato datetime", a uma lista chamada tempo
#len(df_bruto.index) retorna a quantidade de linhas do df_bruto

tempo = []

for i in  range(len(df_bruto.index)):
    
   tempo.append(dt.datetime(df_bruto['ANO'].iloc[i], 
                            df_bruto['MES'].iloc[i], 
                            df_bruto['DIA'].iloc[i],
                            df_bruto['HORA'].iloc[i],
                            df_bruto['MINUTO'].iloc[i]))

#a coluna Tempo é formada pela lista tempo

df['Tempo'] = tempo 

#No dataframe bruto temos a potência na coluna coluna JPS_12B1 
#dada por uma string que representa um número e utiliza ',' como notação. Devemos alterar ',' -> ''
#além disso vamos tornar a string em um float

df['Potencia'] = df_bruto['JPS_12B1'].str.replace(',','.').astype(float) * 10**14    


df_maxpot_dia = pd.DataFrame(columns=['Dia','Potencia Maxima']) 

#O método .dt.date retorna um datetime ano-mês-dia, ou seja retira as horas e minutos dos nossos dados
#A função set() retorna essa lista de datetimes sem repetições, visto que cada dia só terá uma pôt. máxima
#A função sorted() organiza a lista sem repetições de forma crescente

df_maxpot_dia['Dia'] = sorted(set(df['Tempo'].dt.date))   

quantidade_de_dias = len(df_maxpot_dia.index)

for linha in range(quantidade_de_dias):
    df_maxpot_dia.loc[linha, 'Potencia Maxima'] = \
        df.loc[df['Tempo'].dt.date == df_maxpot_dia['Dia'][linha]]['Potencia'].max()


# 3 - Criando um novo dataframe com as potências máximas de cada semana

df_maxpot_semana = pd.DataFrame(columns=['Semana','Potencia Maxima']) 


# No dataframe os dados começam a contar do dia 1 de janeiro de 2008, terça-feira, 
# porém a primeira semana só deve ser contabilizada a partir do primeiro domingo do mês (6 de janeiro)

#tanto os primeros 5 dias quanto os últimos 3 dias devem ser ignorados?
semanas = (df_maxpot_dia['Dia'].count()-5)//7   

#criando a coluna com referente a semana 
df_maxpot_semana['Semana'] = [s for s in range(semanas)]

for linha in range(semanas):
    df_maxpot_semana.loc[linha,'Potencia Maxima'] = \
        df_maxpot_dia.iloc[5+7*linha:12+7*linha]['Potencia Maxima'].max()
    




#Gráficos 

#plot da potência máxima dos dia

plt.style.use('seaborn')


plt.plot(df_maxpot_dia['Dia'], df_maxpot_dia['Potencia Maxima']) 

plt.xlim(df_maxpot_dia['Dia'][0], df_maxpot_dia['Dia'][df_maxpot_dia['Dia'].index[-1]])

plt.title('Potência máxima diária')
plt.xlabel('dias')
plt.ylabel('Potência Máxima')

# plt.gcf().autofmt_xdate()
# date_format = mpl_dates.DateFormatter('%d %')

plt.grid(True)
plt.show()

#plot da semana  
plt.plot(df_maxpot_semana['Semana'][0], df_maxpot_semana['Potencia Maxima'])

plt.xlim(df_maxpot_semana['Semana'][0], df_maxpot_semana['Semana'][df_maxpot_semana['Semana'].index[-1]])

plt.title('Potência máxima semanal')
plt.xlabel('semanas')
plt.ylabel('Potência Máxima ')

plt.grid(True)
plt.show()



# # Create figure and plot space
#fig1, ax = plt.subplots(figsize=(12, 12))

# ax.plot(df_maxpot_semana.Semana, df_maxpot_semana['Potencia Maxima'])

# # Set title and labels for axes
#ax.set(xlabel="Dias",
#ylabel="Potência Máxima (W)",
#title="Potência máxima diária")



# date_form = mdates.DateFormatter("%y-%m-%d")
# ax.xaxis.set_major_formatter(date_form)

# fig1.show()

