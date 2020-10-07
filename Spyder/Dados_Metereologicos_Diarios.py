#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 17:24:29 2020

Esse código está sendo desenvolvido para fazer uma avaliação dos dados de:
    
    -Temperatura;
    -Chuva;
    -Radiação Solar;
    -Velocidade do vento.
 
O caminho para alcançar o objetivo será feito da seguinte forma:
    
    - Dividir em um dataframe para cada variável;
    - Dividir esse dataframe em outros por ano;
    - Pegar unicamente os máximos diários;
    
     
    - Juntar todos por ano.

@author: kr0pt
"""


import pandas as pd


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
                  'VENTO, DIRECAO HORARIA (gr)(° (gr))',
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

df['PRECIPITACAO TOTAL, HORARIO(mm)'] = df['PRECIPITACAO TOTAL, HORARIO(mm)'].str.replace(',','.').astype(float)
df['RADIACAO GLOBAL(Kj/m²)'] = df['RADIACAO GLOBAL(Kj/m²)'].str.replace(',','.').astype(float)
df['TEMPERATURA DO AR - BULBO SECO, HORARIA(°C)'] = df['TEMPERATURA DO AR - BULBO SECO, HORARIA(°C)'].str.replace(',','.').astype(float)
df['VENTO, RAJADA MAXIMA(m/s)'] = df['VENTO, RAJADA MAXIMA(m/s)'].str.replace(',','.').astype(float)
df['VENTO, VELOCIDADE HORARIA(m/s)' ] = df['VENTO, VELOCIDADE HORARIA(m/s)'].str.replace(',','.').astype(float)


# Temperatura
df_temp = df['TEMPERATURA DO AR - BULBO SECO, HORARIA(°C)'].resample('D').max()

# Chuvas
df_chuva = df['PRECIPITACAO TOTAL, HORARIO(mm)'].resample('D').max()

#Vento
df_vento = df[['VENTO, DIRECAO HORARIA (gr)(° (gr))', 'VENTO, RAJADA MAXIMA(m/s)', 'VENTO, VELOCIDADE HORARIA(m/s)' ]].resample('D').max()

#Radiação Solar
df_rads = df['RADIACAO GLOBAL(Kj/m²)'].resample('D').max()