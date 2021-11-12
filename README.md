# Analise-de-Indicadores-de-Cripto
Um repositório para explorar alguns indicadores derivados do fluxo de caixa das moedas e, eventualmente, criar um bot para trading com os achados

## Métodos

Os métodos utilizados aqui serão o NVT, RiskManagement e Stock2Flow. Contudo, nem todos possuo as fórmulas, portanto, um dos objetivos deste projeto é elaborar uma forma de calcular estas métricas de forma simples.

### NVT (Network Value to Transactions Ratio)
Um **NVT** muito alto pode indicar que uma correção está próxima, pois indica que o valor está muito especulativo
<p align="center" >
  <img src="https://user-images.githubusercontent.com/42501669/141523926-8a774e49-4c5f-433c-9b12-1c4b727162a4.png" height="400px" width="auto"/>
  </br>
  <img src="https://user-images.githubusercontent.com/42501669/141524899-8dedfdfa-03e5-467b-8840-280e47fdd335.png" height="50px" width="auto"/>
</p>

Onde:
- MA28 -> Média móvel de 28 dias
- NV -> Valor da rede em dólar
- TV -> Volume de transações em dólar

#### Gráfico gerado por mim
Ainda não fiz 😁

### Stock2Flow
Isso serve para conseguir um preço "justo" da moeda
<p align="center" >
  <img src="https://user-images.githubusercontent.com/42501669/141525446-de1524e5-0bb2-479c-bc65-0f1ae57d9847.png" height="50px" width="auto"/>
  </br>
  <img src="https://user-images.githubusercontent.com/42501669/141525506-05b93f3f-a784-4378-aa5e-409e98598a3e.png" height="50px" width="auto"/>
</p>


### RiskManagement (Método Cowen)

Este indicador é um pouco mais complicado de se reproduzir, pois o Cowen não disponibiliza a fórmula que ele usa, somente isso é mostrado em seus videos:

<img src="https://user-images.githubusercontent.com/42501669/141526697-ff47c64b-6d1e-43a3-9b97-d03193cbfedc.png" height="50px" width="auto"/>


Contudo, se trata de um método capaz de quantizar o risco em entrar em alguma moeda em determinado momento

<p align="center">
  
<img src="https://user-images.githubusercontent.com/42501669/141526756-1202c2a8-a8e8-4d14-99b4-f3dc497430d9.png" height="400px" width="auto"/>
  </p>

Ele também comenta em seu video que utiliza uma média móvel dos ultimos 50 dias para fazer as contas

<img src="https://user-images.githubusercontent.com/42501669/141526834-4562a422-8b17-4c96-ad28-ede5b52123b6.png" height="40px" width="auto"/>


Segundo ele, o ideal seria comprar com riscos de 0~0.4 e vender quando sobe de 0.5 e com certeza se livrar quando está acima de 0.7

Existe um repositório que tentou aplicar este método. Tentarei esmiuçar seu funcionamento e o descreverei aqui.


# A estratégia do bot

A idéia é pegar os 3 modelos e mesclar eles para obter uma forma de identificar quando COMPRAR, VENDER ou SEGURAR

O que poderia ser feito:
- Fazer um bot pra fazer trade seguindo a previsão de cada um dos 3 modelos (NVT,S2F e RiskMan) e mostra como se sai
- Depois faz uma rede neural perceptron que apenas altera o peso das previsões para fazer as operações
- Faz uma rede neural densa e treina ela com deep learning para aprender a maximizar os lucros e além das previsões dos 3 modelos incluir uns dados da moeda, pra ela poder ver em qual confiar mais dependendo da situação.
- E claro, para poder ter uma base de comparação executar 3 simulações:
    - Uma de alguém que investiu tudo no inicio do período de treino
    - Uma que a pessoa investe periodicamente o mesmo valor
    - Alguém que minerou a moeda pelo periodo de treino

Desta forma podemos avaliar o quão bom é cada modelo e  quão bem a rede se sai em analisar seus resultados para tomar uma decisão

Talvez dê, inclusive, para tentar técnica menos sofisticadas de IA como lógica nebulosa e SVM para poder fazer a classificação da ação a ser tomada 

**OU MELHOR AINDA FAZ TODOS E COLOCA ELES COMO AGENTES DE UM "GRUPO DE TRADING" PARA TERMOS UM MODELO MULTIAGENTE QUE DECIDE O QUE FAZER**


