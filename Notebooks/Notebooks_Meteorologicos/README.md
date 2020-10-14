# Notebooks Dados Metereológicos

[toc]

## Resumo

​	Nos códigos referentes aos Dados Metereológicos tivemos como objetivo visualizar os dados de temperatura, chuva, radiação solar e velocidade do vento, apresentando o máximo diário e semanal por ano, de 2008 até 2013.  ( Algumas outras informações além dos máximos, também foram apresentadas graficamente para averiguarmos a utilidade delas. Se for desejado, retiro.)  

## Coleta de Dados (INMET)

​	O primeiro passo para alcançar o objetivo foi o de explorar o [site do Instituto Nacional  de Meteorologia (INMET)](https://portal.inmet.gov.br/ "site do INMET") para ver a melhor forma de se obter os dados meteorológicos de João Pessoa no intervalo de tempo do dia 01 de janeiro de 2008 até 31 de dezembro de 2013.



### Caminho escolhido para acessar os dados

​	Ainda em reunião foi comentado como eram coletados os dados anteriormente, então decidi reproduzir o caminho que gerasse esse resultado. Primeiro, acessei na aba dados metereológicos a opção "Banco de Dados Meteorológicos", fui até prosseguir no final da página ao acessar é pedido o email e então prosseguir. O procedimento pode ser visto pelo gif abaixo.



![teste1](imagensdoreadme/teste1.gif)



Após isso é aberto uma página que torna possível a escolha por:

- Tipo de dados:
  - Dados Horários
  - Dados Diários
  - Dados Mensais
- Tipo de estação:
  - Automáticas
  - Convencionais
- Abrangência:
  - País
  - Região



### Detalhes da escolha

​	Foram escolhidos os dados horários para se obter as informações diárias das variáveis e os dados diários para se obter os dados semanais. Ambos os arquivos csv dos dados encontram-se na pasta [Dados/Dados-Meteorologicos](https://github.com/V-kr0pt/previsao-de-demanda/tree/main/Dados/Dados-Metereologicos). 

​	O tipo de estação escolhido foi "Automáticas", a abrangência: região, escolhido nordeste e por fim a estação A320 em João Pessoa. As variáveis disponíveis entre o banco de dados diário e horário são diferentes entre si, como pode se ver nas imagens seguintes:



- Variáveis dos Dados Horários	

<img src="./imagensdoreadme/var_dados_horarios.png" alt="var_dados_horarios" style="zoom: 67%;" />

​	Pode-se ver uma ampla quantidade de variáveis coletadas nos Dados Horários, inclusive a Radiação Global (Radiação Solar) 



- Variáveis dos Dados Diários 

<img src="./imagensdoreadme/var_dados_diarios.png" alt="var_dados_diarios" style="zoom: 67%;" />



​	Quanto as variáveis dos Dados Diários conseguimos perceber que algumas das variáveis presentes nos Dados Horários não estão presentes. 

​	Em ambos foi marcado a opção de selecionar todas as variáveis para download, assim os dados brutos salvos contém a maior gama possível de variáveis. 



## Gráficos

​	Após a coleta dos Dados foram criados gráficos utilizando o Jupyter Notebook. Os códigos foram separados em dois, sendo um para obter os gráficos diários e outro para obter os gráficos semanais. Ambos podem ser acessado no início dessa página.

### Apresentação dos Plots

​	Os gráficos foram divididos para que em cada Figure se encontrasse os plots referentes a variável desejada (Temperatura, Vento, Chuva, Radiação Solar) divididos em subplots que representam os anos.

#### Gráficos Diários

##### Temperatura

![Temperatura](./Plots/Diarios/Temperatura.png)

​	

​	Podemos notar alguns dados faltantes em 2010 e fica explícito que em quase todo o ano de 2012 ocorreu algum problema na mensuração.  Ainda, em 2013 conseguimos reparar alguns dados faltantes próximo ao mês 07, mais precisamente do dia 19/06 até o dia 15/07 (tabela ao fim). 

​	Verificaremos ao longo dos outros  gráficos que esse é um comportamento se repete, ou seja, não é um  problema unicamente na mensuração dessa variável, mas sim em todas.

##### Vento

![Ventos](./Plots/Diarios/Ventos.png)

​	Podemos verificar que os dados faltantes da velocidade do vento  estão em intervalos iguais ou muito próximos dos dados faltantes da  variável temperatura

 ##### Chuvas

![Chuvas](./Plots/Diarios/Chuvas.png)

​	Os anos de 2012, 2010 e 2013 dos gráficos de chuvas, explicitam que nos intervalos em que as outras variáveis apresentam dados faltantes, os dados de chuvas registram precipitação de 0mm. O que torna mais complicado de analisar, visto que podem existir dias em que a  precipitação foi de 0mm e outros em que na verdade foram ocasionados de falhas na medição.

##### Radiação Solar

![Radiacao](./Plots/Diarios/Radiacao.png)

​	Podemos verificar que além dos dados faltantes nos intervalos  mencionados em outras variáveis a radiação apresenta um comportamento  atípico no ano de 2010, entre o mês 06 e mês 10.



#### Gráficos Semanais

##### Temperatura



##### Vento



##### Chuvas



##### Radiação Solar

