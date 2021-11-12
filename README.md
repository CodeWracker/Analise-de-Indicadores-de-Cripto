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

# Referências

## Conteúdo

Sobre o NVT - [Link](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbktYS1I3ZjdLbGFFaWJHLUhnZXdjNHNBNWY0UXxBQ3Jtc0tta2VNVk5MMFE4cGRFMENSX2V4QVd6b1hpV1EzRWNKSGgyX0NLNnJNSENKZE5FSHdESU55QUExeDZwdFlxT21mLTdmNnAxQzlvS2taZ2dYMEZSQmplUFdYRWkwM1JzZzJFMjZFbDl3V0F4RjY2OTNXVQ&q=https%3A%2F%2Fwww.forbes.com%2Fsites%2Fwwoo%2F2017%2F09%2F29%2Fis-bitcoin-in-a-bubble-check-the-nvt-ratio%2F%3Fsh%3D128e90f56a23)

Sobre o NVTS - [Link](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbDBjcHhDZUV1NGduTHVubmJaZzJaM2VkSDJZZ3xBQ3Jtc0trTW1RbFVYNlZlbEtLbTYwN28zR3NvQmxXcjI1elNrS180d0h2NmdWeE1fVnNaamF4Z3FqS1RzZ0lSSWlVMVRTMkZYSWh0cE5PLVlHSzhfajlVVzktR1UwZ0p6M1JPV0lJWXM1MzBjS285NHpuRC1HQQ&q=https%3A%2F%2Fmedium.com%2Fcryptolab%2Fhttps-medium-com-kalichkin-rethinking-nvt-ratio-2cf810df0ab0)

Canal Benjamin Cowen (Precificação de Risco) - [Link](https://www.youtube.com/channel/UCRvqjQPSeaWn-uEx-w0XOIg)

Artigo Sobre Piso de Liquidez Para o Bitcoin - [Link](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbmV5WV91eVVKOHNGY3JPaEk1OUdiSlFOa014Z3xBQ3Jtc0trRExuVi1YSHhiZFZhRGFPV053LWEwWjROMlJjRGQzRi1Sam9qT3dWeVUwVGhJUTNTNDNmM19TaHlNOVhuRFp1NFh6SThRV0FhaWN0MXBSVXA2Sl90eXE0Ql9FWHNCamVZdGcxUnpIOWhpNlphUk1JQQ&q=https%3A%2F%2Fwww.blockwareintelligence.com%2Fp%2Fblockware-intelligence-newsletter-93f)

Valuation Criptoativos via Teoria de Rede - [Link](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbjYxeW92NDZnM2hVZnV5U1ZFYU1SX1ZlQlBId3xBQ3Jtc0ttb3pxUThQWUJIalloSzNldEhWR04xdlVfdWxjZERqX0ptaUVGY0xmeDlZbUVxUFplNmxmclFIVzNEcTdOUEJqUTRYQ0gtMGNDVHFrV0NQVlpqb0t6ZmxVS0dsbmdrRnExSDBvMmFXVm9odFdoQi10QQ&q=https%3A%2F%2Fwww.aeaweb.org%2Fconference%2F2018%2Fpreliminary%2Fpaper%2FtsFKfa85)

Modelo Stock to Flow - [Link](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqazQ5OEJGV2tqVDgzUjJjYzlzMTJMeU1CYjRDd3xBQ3Jtc0ttYXZ0Y2p0RDFpamRLT0liNFNab2xQZ3dobGpqa29kYl9FbHN3OHZ0OVdoT2NlY3gwcjNRdkpyR3BOX0otdU9zMkFIcXRjeGpSLXVfQU5BSXg3SE1PR1FsZ1ZVQzVZOXliSmRpbm5DTWEyZGR3UGJtOA&q=https%3A%2F%2Fmedium.com%2F%40100trillionUSD%2Fmodeling-bitcoins-value-with-scarcity-91fa0fc03e25)

## Gráficos

Gráfico NVTS BTC Gratuito - [Link](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqa0hrNkY3ei1wSVRmRHdJREZwWlRjOWVYZHYxQXxBQ3Jtc0ttdXNzOHhpYnliR3hmbnlxWEFwQ1lMRjNCMGllbkQxQ2V0SzQtT3NfSm1zR2NuWEpNODBWcWNKb19iQ3g5Yl9wSEMzbnBPNXUwVWlHZU1WOTFJblZaQm83RUFfWlhMWnkzWDZHc093RXpHSTV1Q2FUYw&q=http%3A%2F%2Fcharts.woobull.com%2Fbitcoin-nvt-signal%2F)

Gráfico NVT BTC Gratuito - [Link](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbkZGclR1MFhXd2JpMElVNmlKSXhXWGlkaWFHQXxBQ3Jtc0trZ25ydGlic0dsTlBEc3QxcVNrMFExTTRza2RJcWdlU3A3Rm1DTnJ1Sm9zcVVjTW9FaFJ1N0xhdXJSaHRaclVzMzJjbzdtZklETmY3bllGYW1YZldUSm9tSFlOV0w5SXYyT3Q3YWFXdDJkUTJrTUN4TQ&q=http%3A%2F%2Fcharts.woobull.com%2Fbitcoin-nvt-ratio%2F)
