#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 10:35:10 2020

Esse código está sendo criado com a função de obter os dataframes semanais 
para fazer a avaliação dos dados de :
    
    - Temperatura;
    - Chuva;
    - Radiação Solar;
    - Velocidade do vento.

O caminho para alcançar o objetivo será feito da seguinte forma:
    
    - Construir um dataframe com as colunas que representam as variáveis 
      desejadas;  
    - Dividir em dataframes para cada variável contendo os dados semanais;
    - Dividir os dataframes por ano.

@author: kr0pt
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# -- Construção de um dataframe com as colunas que representam as variáveis --

#caminho do arquivo csv
file_path = Path(
    '../Dados/Dados-Metereologicos/Diarios/' +\
        'dados_A320_D_A_2008-01-01_2013-12-31.csv'
    )

df = pd.read_csv(file_path,
                 header=9,
                 sep=';', 
                 usecols=
                 ['Data Medicao',
                  'PRECIPITACAO TOTAL, DIARIO (AUT)(mm)',
                  'TEMPERATURA MEDIA, DIARIA (AUT)(°C)',
                  'TEMPERATURA MAXIMA, DIARIA (AUT)(°C)',
                  'TEMPERATURA MINIMA, DIARIA (AUT)(°C)',
                  'VENTO, RAJADA MAXIMA DIARIA (AUT)(m/s)',
                  'VENTO, VELOCIDADE MEDIA DIARIA (AUT)(m/s)' ]
                 
                 )

#transformando a coluna Data Medicao para o formato Datetime

df['Data Medicao'] = pd.to_datetime(df['Data Medicao'])


#transformando a coluna Data Medicao em índices

df.set_index('Data Medicao', inplace=True)

#transformando os dados numéricos de str para float

df['PRECIPITACAO TOTAL, DIARIO (AUT)(mm)'] =\
    df['PRECIPITACAO TOTAL, DIARIO (AUT)(mm)'].str.replace(',','.').astype(float)

df['TEMPERATURA MAXIMA, DIARIA (AUT)(°C)'] =\
    df['TEMPERATURA MAXIMA, DIARIA (AUT)(°C)'].str.replace(',','.').astype(float)

df['TEMPERATURA MEDIA, DIARIA (AUT)(°C)'] =\
    df['TEMPERATURA MEDIA, DIARIA (AUT)(°C)'].str.replace(',','.').astype(float)
    
df['TEMPERATURA MINIMA, DIARIA (AUT)(°C)'] =\
    df[ 'TEMPERATURA MINIMA, DIARIA (AUT)(°C)'].str.replace(',','.').astype(float)
    
df['VENTO, RAJADA MAXIMA DIARIA (AUT)(m/s)'] =\
    df['VENTO, RAJADA MAXIMA DIARIA (AUT)(m/s)'].str.replace(',','.').astype(float)
    
df[ 'VENTO, VELOCIDADE MEDIA DIARIA (AUT)(m/s)'] =\
    df[ 'VENTO, VELOCIDADE MEDIA DIARIA (AUT)(m/s)'].str.replace(',','.').astype(float)
    
    


# -- Divisão em dataframes para cada variável contendo os dados semanais --   

# - Temperatura -

#Criando o dataframe das temperaturas com as colunas desejadas
df_temp = pd.DataFrame(columns = 
                       ['TEMPERATURA MEDIA SEMANAL (°C)',
                        'TEMPERATURA MAXIMA SEMANAL (°C)',
                        'TEMPERATURA MINIMA SEMANAL (°C)' ] 
                       )

#Coluna média semanal é a média das temperaturas médias diárias
df_temp['TEMPERATURA MEDIA SEMANAL (°C)']=\
    df['TEMPERATURA MEDIA, DIARIA (AUT)(°C)'].resample('W-SUN').mean()

#Coluna máxima semanal é o valor máximo das temperaturas máximas diárias    
df_temp['TEMPERATURA MAXIMA SEMANAL (°C)']=\
    df['TEMPERATURA MAXIMA, DIARIA (AUT)(°C)'].resample('W-SUN').max()
    
#Coluna mínima semanal é o valor mínimo das temperaturas mínimas diárias 
df_temp['TEMPERATURA MINIMA SEMANAL (°C)']=\
    df['TEMPERATURA MINIMA, DIARIA (AUT)(°C)'].resample('W-SUN').max()


# - Chuva -

#Criando o dataframe dos dados de precipitação total
df_chuva = pd.DataFrame(columns=['PRECIPITACAO TOTAL, SEMANAL (mm)'])

#Coluna precipitação semanal é a soma das precipitações diárias
df_chuva['PRECIPITACAO TOTAL, SEMANAL (mm)'] =\
    df['PRECIPITACAO TOTAL, DIARIO (AUT)(mm)'].resample('W-SUN').sum()


# - Velocidade do Vento -

#Criando o dataframe dos dados do vento
df_vento = pd.DataFrame(columns=
                        ['VENTO, RAJADA MAXIMA SEMANAL (m/s)',
                         'VENTO, VELOCIDADE MEDIA SEMANAL (m/s)']
                        )

#Rajada Max. Semanal será o valor máximo das rajadas diárias
df_vento['VENTO, RAJADA MAXIMA SEMANAL (m/s)'] =\
    df['VENTO, RAJADA MAXIMA DIARIA (AUT)(m/s)'].resample('W-SUN').max()

#Velocidade média semanal será a média das velocidades médias diárias
df_vento['VENTO, VELOCIDADE MEDIA SEMANAL (m/s)'] =\
    df['VENTO, VELOCIDADE MEDIA DIARIA (AUT)(m/s)'].resample('W-SUN').mean()



# -- Divisão dos dataframes semanais para cada ano --

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

# -- Transformando os índices semanais de cada ano --

#Temperatura
df_temp_08.reset_index(inplace=True, drop=True)
df_temp_09.reset_index(inplace=True, drop=True)
df_temp_10.reset_index(inplace=True, drop=True) 
df_temp_11.reset_index(inplace=True, drop=True)
df_temp_12.reset_index(inplace=True, drop=True)
df_temp_13.reset_index(inplace=True, drop=True)

#Chuva
df_chuva_08.reset_index(inplace=True, drop=True)
df_chuva_09.reset_index(inplace=True, drop=True) 
df_chuva_10.reset_index(inplace=True, drop=True)
df_chuva_11.reset_index(inplace=True, drop=True)
df_chuva_12.reset_index(inplace=True, drop=True)
df_chuva_13.reset_index(inplace=True, drop=True)

#Vento

df_vento_08.reset_index(inplace=True, drop=True)
df_vento_09.reset_index(inplace=True, drop=True)
df_vento_10.reset_index(inplace=True, drop=True)
df_vento_11.reset_index(inplace=True, drop=True)
df_vento_12.reset_index(inplace=True, drop=True)
df_vento_13.reset_index(inplace=True, drop=True)


# -- Gráficos por variável --

#plotar gráficos temperatura:
    
fig1, f1_axes = plt.subplots(ncols=2, nrows=3, constrained_layout=True)

fig1.suptitle('Temperaturas dos anos ao longo das semanas',size=17)

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
fig2, f2_axes = plt.subplots(nrows=3, ncols=2, constrained_layout=True)

fig2.suptitle('Chuvas dos anos ao longo das semanas',size=17)

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
fig3, f3_axes = plt.subplots(nrows=3, ncols=2, constrained_layout=True)

fig3.suptitle('Velocidade dos ventos nos anos ao longo das semanas',size=17)

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
















