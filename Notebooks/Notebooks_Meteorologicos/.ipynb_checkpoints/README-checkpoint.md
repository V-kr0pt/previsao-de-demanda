# Notebooks Dados Metereológicos

[toc]

## Resumo

​	Nos códigos referentes aos Dados Metereológicos tivemos como objetivo visualizar os dados de temperatura, chuva, radiação solar e velocidade do vento, apresentando o máximo diário e semanal por ano, de 2008 até 2013.  ( Algumas outras informações além dos máximos, também foram apresentadas graficamente para averiguarmos a utilidade delas. Se for desejado, retiro.)  

## Coleta de Dados (INMET)

​	O primeiro passo para alcançar o objetivo foi o de explorar o [site do Instituto Nacional  de Meteorologia (INMET)](https://portal.inmet.gov.br/ "site do INMET") para ver a melhor forma de se obter os dados meteorológicos de João Pessoa no intervalo de tempo do dia 01 de janeiro de 2008 até 31 de dezembro de 2013.



### Caminho escolhido para acessar os dados

​	Ainda em reunião foi comentado como eram coletados os dados anteriormente, então decidi reproduzir o caminho que gerasse esse resultado. Primeiro, acessei na aba dados metereológicos a opção "Banco de Dados Meteorológicos", fui até prosseguir no final da página. Ao acessar é pedido o email e então obtemos acesso à página de seleção dos dados desejados. O procedimento pode ser visto pelo gif abaixo.



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

​	Foram escolhidos os dados horários e a partir deles foram obtidas as informações diárias das variáveis e, junto a isso, os dados diários para se obter as informações referentes as semanas. Ambos os arquivos csv dos dados encontram-se na pasta [Dados/Dados-Meteorologicos](https://github.com/V-kr0pt/previsao-de-demanda/tree/main/Dados/Dados-Metereologicos). 

​	O tipo de estação escolhida foi a opção "Automáticas", a abrangência: "região" e então "nordeste", por fim a estação "A320" que se localiza na cidade de João Pessoa. 

​	Um fato importante destacar é que as variáveis disponíveis entre o banco de dados diário e horário são diferentes entre si, como pode se ver nas imagens seguintes:



- Variáveis dos Dados Horários	

<img src="./imagensdoreadme/var_dados_horarios.png" alt="var_dados_horarios" style="zoom: 67%;" />

​	Pode-se ver uma ampla quantidade de variáveis coletadas nos Dados Horários, inclusive a Radiação Global (Radiação Solar) 



- Variáveis dos Dados Diários 

<img src="./imagensdoreadme/var_dados_diarios.png" alt="var_dados_diarios" style="zoom: 67%;" />



​	Quanto as variáveis dos Dados Diários, conseguimos perceber que algumas das variáveis que estão presentes nos Dados Horários não estão presentes nessa opção. 

​	Em ambos foi marcado a opção de selecionar todas as variáveis para download, assim os dados brutos salvos contém a maior gama possível de variáveis e poderão ser utilizados se desejado. 



## Gráficos

​	Após a coleta dos Dados foram criados gráficos utilizando o Jupyter Notebook. Os códigos foram separados em dois, sendo um para obter os gráficos referentes às informações diárias e outro para obter os gráficos com as informações semanais. Ambos os códigos podem ser acessado no início dessa página.

### Apresentação dos Plots

​	Os gráficos foram divididos para que em cada [Figure](https://matplotlib.org/3.3.2/tutorials/introductory/usage.html#figure) se encontrasse os plots referentes a variável desejada (Temperatura, Vento, Chuva, Radiação Solar) divididos em [subplots](https://matplotlib.org/3.3.2/tutorials/introductory/usage.html#the-object-oriented-interface-and-the-pyplot-interface) que representam os anos.

#### Gráficos Diários

##### Temperatura

![Temperatura](./Plots/Diarios/Temperatura.png)

​	

​	Podemos notar alguns dados faltantes em 2010 e fica explícito que em quase todo o ano de 2012 ocorreu algum problema na mensuração.  Ainda, em 2013 conseguimos reparar alguns dados faltantes próximo ao mês 07, mais precisamente do dia 19/06 até o dia 15/07 (tabela ao fim). 

​	Verificaremos ao longo dos outros  gráficos que esse é um comportamento que se repete, ou seja, não é um problema unicamente na mensuração dessa variável, mas sim um problem na estação A320.

##### Vento

![Ventos](./Plots/Diarios/Ventos.png)

​	Podemos verificar que os dados faltantes da velocidade do vento estão em intervalos iguais ou muito próximos dos dados faltantes da variável temperatura.

 ##### Chuvas

![Chuvas](./Plots/Diarios/Chuvas.png)

​	Os anos de 2012, 2010 e 2013 dos gráficos de chuvas, explicitam que nos intervalos em que as outras variáveis apresentam dados faltantes, os dados de chuvas registram precipitação de 0mm. O que torna mais complicado de analisar, visto que podem existir dias em que a  precipitação foi de 0mm e outros em que na verdade foram ocasionados de falhas na medição.

##### Radiação Solar

![Radiacao](./Plots/Diarios/Radiacao.png)

​	Podemos verificar que além dos dados faltantes nos intervalos  mencionados em outras variáveis a radiação apresenta um comportamento  atípico no ano de 2010, entre o mês 06 e mês 10.



#### Gráficos Semanais

##### Temperatura

![Temperatura](./Plots/Semanais/Temperatura.png)

​	É possível ver o problema de mensuração no ano de 2012. Ainda, em 2013  conseguimos reparar alguns dados faltantes da semana 24 até a semana 27 (Número exato da semana confirmado ao fim).  Verificaremos ao longo dos outros gráficos que esse é um comportamento  que se repete.

##### Vento

![Vento](./Plots/Semanais/Vento.png)

Ano de 2012 apresenta o mesmo erro já observado e no intervalo da semana 24 até semana 27 de 2013 encontram-se no dados faltantes.

##### Chuvas

![Chuva](./Plots/Semanais/Chuva.png)

​	Como visto anteriormente percebemos a anormalidade nos dados  referentes ao ano de 2012 e no intervalo específico entre a semana 24 e a semana 27, porém nesse caso ao invés de serem dados faltantes são registros de 0 mm de pluviosidade

