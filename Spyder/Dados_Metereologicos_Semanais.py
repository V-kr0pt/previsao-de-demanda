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
    - Dividir em dataframes para cada variável contendo os máximos semanais;
    - Dividir os dataframes de máx. semanal por ano.

@author: kr0pt
"""

import pandas as pd


# -- Construção de um dataframe com as colunas que representam as variáveis --

path = '/home/kr0pt/Documents/Pesquisa/Codes_notgit/Dados/Dados-Metereologicos/Diarios/dados_A320_D_A_2008-01-01_2013-12-31.csv'
df = pd.read_csv(path, ';', 
                 header=9,
                 usecols=
                 ['Data Medicao',
                  'PRECIPITACAO TOTAL, DIARIO (AUT)(mm)',
                  'TEMPERATURA MEDIA, DIARIA (AUT)(°C)',
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

df['TEMPERATURA MEDIA, DIARIA (AUT)(°C)'] =\
    df['TEMPERATURA MEDIA, DIARIA (AUT)(°C)'].str.replace(',','.').astype(float)
    
df['TEMPERATURA MINIMA, DIARIA (AUT)(°C)'] =\
    df[ 'TEMPERATURA MINIMA, DIARIA (AUT)(°C)'].str.replace(',','.').astype(float)
    
df['VENTO, RAJADA MAXIMA DIARIA (AUT)(m/s)'] =\
    df['VENTO, RAJADA MAXIMA DIARIA (AUT)(m/s)'].str.replace(',','.').astype(float)
    
df[ 'VENTO, VELOCIDADE MEDIA DIARIA (AUT)(m/s)'] =\
    df[ 'VENTO, VELOCIDADE MEDIA DIARIA (AUT)(m/s)'].str.replace(',','.').astype(float)
    
    
# -- Divisão em dataframes para cada variável contendo os máximos semanais --   
    
    