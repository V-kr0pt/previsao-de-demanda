#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 17:24:29 2020

Esse código está sendo desenvolvido para fazer uma avaliação dos dados de:
    
    -Temperatura;
    -Chuva;
    -Velocidade do vento;
    -Radiação Solar.
    
 
O caminho para alcançar o objetivo será feito da seguinte forma:
    
    - Dividir em um dataframe para cada variável;
    - Dividir esse dataframe em outros por ano;
    - Pegar unicamente os máximos diários;
    - Fazer gráficos que permitam analisar a integridade dos dados. 
     
    

@author: kr0pt
"""


import pandas as pd
import matplotlib.pyplot as plt


# -- Construção de um dataframe com as colunas que representam as variáveis --

#caminho do arquivo csv
path='/home/kr0pt/Documents/Pesquisa/Codes_notgit/Dados/Dados-Metereologicos/Horarios/dados_A320_H_A_2008-01-01_2013-12-31.csv' 


#importando o arquivo csv como um Dataframe

df = pd.read_csv(path, 
                 header=9, #linha do cabeçalho
                 sep=';',  #separador
                 usecols= #colunas
                 ['Data Medicao', 
                  'Hora Medicao', 
                  'PRECIPITACAO TOTAL, HORARIO(mm)',
                  'RADIACAO GLOBAL(Kj/m²)',
                  'TEMPERATURA DO AR - BULBO SECO, HORARIA(°C)',
                  'TEMPERATURA MINIMA NA HORA ANT. (AUT)(°C)',
                  'TEMPERATURA MAXIMA NA HORA ANT. (AUT)(°C)',
                  'VENTO, RAJADA MAXIMA(m/s)',
                  'VENTO, VELOCIDADE HORARIA(m/s)' ]
                 )




#ajustando as horas de medição para se tornarem um padrão reconhecido pelo datetime

df['Hora Medicao'] = (df['Hora Medicao']//100).astype(str)+':'+'00' 


#concatenando a hora com a data de medição e retirando a coluna das horas

df['Data Medicao'] = df['Data Medicao'] + ' ' + df['Hora Medicao'].astype(str)
df.drop('Hora Medicao', axis=1, inplace=True)


#transformando os valores da coluna em datetime

df['Data Medicao'] = pd.to_datetime(df['Data Medicao'])

#transformando a coluna das datas nos índices do dataframe

df.set_index('Data Medicao', inplace=True)


#transformando os dados de string para float


df['PRECIPITACAO TOTAL, HORARIO(mm)'] = \
    df['PRECIPITACAO TOTAL, HORARIO(mm)'].str.replace(',','.').astype(float)


df['RADIACAO GLOBAL(Kj/m²)'] = \
    df['RADIACAO GLOBAL(Kj/m²)'].str.replace(',','.').astype(float)


df['TEMPERATURA DO AR - BULBO SECO, HORARIA(°C)'] =\
    df['TEMPERATURA DO AR - BULBO SECO, HORARIA(°C)'].str.replace(',','.').astype(float)
    
df['TEMPERATURA MINIMA NA HORA ANT. (AUT)(°C)'] =\
    df['TEMPERATURA MINIMA NA HORA ANT. (AUT)(°C)'].str.replace(',','.').astype(float)
    
df['TEMPERATURA MAXIMA NA HORA ANT. (AUT)(°C)'] =\
    df['TEMPERATURA MAXIMA NA HORA ANT. (AUT)(°C)'].str.replace(',','.').astype(float)


df['VENTO, RAJADA MAXIMA(m/s)'] = \
    df['VENTO, RAJADA MAXIMA(m/s)'].str.replace(',','.').astype(float)


df['VENTO, VELOCIDADE HORARIA(m/s)' ] =\
    df['VENTO, VELOCIDADE HORARIA(m/s)'].str.replace(',','.').astype(float)


# - Temperatura -

df_temp = pd.DataFrame(columns=
                       ['TEMPERATURA DO AR - BULBO SECO, DIARIA(°C)',
                        'TEMPERATURA MINIMA DIARIA (°C)',
                        'TEMPERATURA MAXIMA DIARIA (°C)'
                           ]
                       )

#A temperatura do ar diária será a média das temperaturas horárias

df_temp['TEMPERATURA DO AR - BULBO SECO, DIARIA(°C)'] =\
    df['TEMPERATURA DO AR - BULBO SECO, HORARIA(°C)'].resample('D').mean()

#A temperatura mínima diária será a menor temperatura horária

df_temp['TEMPERATURA MINIMA DIARIA (°C)'] =\
    df['TEMPERATURA MINIMA NA HORA ANT. (AUT)(°C)'].resample('D').min()

#A temperatura máxima diária será a maior temperatura horária

df_temp['TEMPERATURA MAXIMA DIARIA (°C)'] =\
    df['TEMPERATURA MAXIMA NA HORA ANT. (AUT)(°C)'].resample('D').max()


# - Chuvas - 


#Criando o dataframe dos índices de chuva com o nome da coluna desejada
df_chuvas = pd.DataFrame(columns=['PRECIPITACAO TOTAL, HORARIO(mm)'])

#A coluna Precipitação total diária é a soma das precipitações horárias
df_chuva = df['PRECIPITACAO TOTAL, HORARIO(mm)'].resample('D').sum()




# - Velocidade do Vento -

#Criando o dataframe das velocidades do vento com o nome da coluna desejada
df_vento = pd.DataFrame(columns=
                        ['VENTO, VELOCIDADE DIÁRIA (m/s)',
                         'VENTO, RAJADA MAXIMA DIARIA (m/s)']
                        )

#A velocidade diária do vento será a média das velocidades horárias
df_vento['VENTO, VELOCIDADE DIÁRIA (m/s)' ] =\
    df['VENTO, VELOCIDADE HORARIA(m/s)'].resample('D').mean()

#A rajada máxima diária será a máxima rajada horária
df_vento['VENTO, RAJADA MAXIMA DIARIA (m/s)'] =\
    df['VENTO, RAJADA MAXIMA(m/s)'].resample('D').max()



# - Radiação Solar -

#A radiação solar diária será a média das radiações soláres horárias
df_rads = df['RADIACAO GLOBAL(Kj/m²)'].resample('D').mean()



# -- Divisão dos dataframes diários para cada ano --

#dividindo os dados da temperatura por anos
df_temp_08 = df_temp.loc[df_temp.index.year == 2008]
df_temp_09 = df_temp.loc[df_temp.index.year == 2009]
df_temp_10 = df_temp.loc[df_temp.index.year == 2010]
df_temp_11 = df_temp.loc[df_temp.index.year == 2011]
df_temp_12 = df_temp.loc[df_temp.index.year == 2012]
df_temp_13 = df_temp.loc[df_temp.index.year == 2013]


#dividindo os dados da chuva por anos
df_chuva_08 = df_chuva.loc[df_chuva.index.year == 2008]
df_chuva_09 = df_chuva.loc[df_chuva.index.year == 2009]
df_chuva_10 = df_chuva.loc[df_chuva.index.year == 2010]
df_chuva_11 = df_chuva.loc[df_chuva.index.year == 2011]
df_chuva_12 = df_chuva.loc[df_chuva.index.year == 2012]
df_chuva_13 = df_chuva.loc[df_chuva.index.year == 2013]


#dividindo os dados do vento por anos
df_vento_08 = df_vento.loc[df_vento.index.year == 2008]
df_vento_09 = df_vento.loc[df_vento.index.year == 2009]
df_vento_10 = df_vento.loc[df_vento.index.year == 2010]
df_vento_11 = df_vento.loc[df_vento.index.year == 2011]
df_vento_12 = df_vento.loc[df_vento.index.year == 2012]
df_vento_13 = df_vento.loc[df_vento.index.year == 2013]


#dividindo os dados da radiação solar por anos
df_rads_08 = df_rads.loc[df_rads.index.year == 2008]
df_rads_09 = df_rads.loc[df_rads.index.year == 2009]
df_rads_10 = df_rads.loc[df_rads.index.year == 2010]
df_rads_11 = df_rads.loc[df_rads.index.year == 2011]
df_rads_12 = df_rads.loc[df_rads.index.year == 2012]
df_rads_13 = df_rads.loc[df_rads.index.year == 2013]






# -- Gráficos por variável --

#Gráfico das temperaturas
fig1, f1_axes = plt.subplots(ncols=2, nrows=3, constrained_layout=True, figsize=(20,15))

fig1.suptitle('Temperaturas dos anos ao longo dos dias',size=30)

f1_axes[0,0].plot(df_temp_08)
f1_axes[0,0].set_title('Ano de 2008')

f1_axes[0,1].plot(df_temp_09)
f1_axes[0,1].set_title('Ano de 2009')

f1_axes[1,0].plot(df_temp_10)
f1_axes[1,0].set_title('Ano de 2010')
           
f1_axes[1,1].plot(df_temp_11)
f1_axes[1,1].set_title('Ano de 2011')

f1_axes[2,0].plot(df_temp_12)
f1_axes[2,0].set_title('Ano de 2012')

f1_axes[2,1].plot(df_temp_13)
f1_axes[2,1].set_title('Ano de 2013')



#Gráfico das chuvas
fig2, f2_axes = plt.subplots(nrows=3, ncols=2, constrained_layout=True, figsize=(20,15))

fig2.suptitle('Chuvas dos anos ao longo dos dias',size=30)

f2_axes[0,0].plot(df_chuva_08)
f2_axes[0,0].set_title('Ano de 2008')

f2_axes[0,1].plot(df_chuva_09)
f2_axes[0,1].set_title('Ano de 2009')

f2_axes[1,0].plot(df_chuva_10)
f2_axes[1,0].set_title('Ano de 2010')
           
f2_axes[1,1].plot(df_chuva_11)
f2_axes[1,1].set_title('Ano de 2011')

f2_axes[2,0].plot(df_chuva_12)
f2_axes[2,0].set_title('Ano de 2012')

f2_axes[2,1].plot(df_chuva_13)
f2_axes[2,1].set_title('Ano de 2013')


#Gráficos da velocidade do vento
fig3, f3_axes = plt.subplots(nrows=3, ncols=2, constrained_layout=True, figsize=(20,15))

fig3.suptitle('Velocidade dos ventos nos anos ao longo dos dias',size=30)

f3_axes[0,0].plot(df_vento_08)
f3_axes[0,0].set_title('Ano de 2008')

f3_axes[0,1].plot(df_vento_09)
f3_axes[0,1].set_title('Ano de 2009')

f3_axes[1,0].plot(df_vento_10)
f3_axes[1,0].set_title('Ano de 2010')
           
f3_axes[1,1].plot(df_vento_11)
f3_axes[1,1].set_title('Ano de 2011')

f3_axes[2,0].plot(df_vento_12)
f3_axes[2,0].set_title('Ano de 2012')

f3_axes[2,1].plot(df_vento_13)
f3_axes[2,1].set_title('Ano de 2013')

#Gráficos da radiação solar 
fig4, f4_axes = plt.subplots(nrows=3, ncols=2, constrained_layout=True, figsize=(20,15))


f4_axes[0,0].plot(df_rads_08)
f4_axes[0,0].set_title('Ano de 2008')

f4_axes[0,1].plot(df_rads_09)
f4_axes[0,1].set_title('Ano de 2009')

f4_axes[1,0].plot(df_rads_10)
f4_axes[1,0].set_title('Ano de 2010')
           
f4_axes[1,1].plot(df_rads_11)
f4_axes[1,1].set_title('Ano de 2011')

f4_axes[2,0].plot(df_rads_12)
f4_axes[2,0].set_title('Ano de 2012')

f4_axes[2,1].plot(df_rads_13)
f4_axes[2,1].set_title('Ano de 2013')




