# Projeto: Análise e Visualização de Ações com yFinance e mplfinance

## Descrição
Este projeto permite que o usuário insira o ticker de uma ação e visualize um gráfico de candlestick do intervalo de tempo desejado. O script usa as bibliotecas yfinance para obter dados financeiros e mplfinance para gerar um gráfico que mostra as variações de preço ao longo do período. Além disso, o gráfico é salvo como uma imagem em formato PNG para fácil acesso posterior.

## Funcionalidades
- Entrada do usuário para definir o ticker da ação.
- Coleta automática dos dados históricos de preço da ação do intervalo de tempo selecionado.
- Plotagem de um gráfico de candlestick utilizando a biblioteca mplfinance.
- Salvamento do gráfico gerado em um arquivo PNG.

## Requisitos
* Python 3.x
* Bibliotecas Python:
  * yfinance
  * mplfinance
  * pandas

Você pode instalar os requisitos executando:
```bash
pip install yfinance mplfinance pandas
```

## Como Usar 
1. Clone este repositório para sua máquina local.
2. Certifique-se de que todas as bibliotecas necessárias estão instaladas.
3. Execute o script com o comando:
```bash
python preco-da-acao.py
```
4. Insira o ticker da ação que deseja analisar quando solicitado (ex.: PETR4.SA para Petrobras ou AAPL para Apple). O próprio código faz a alteração para letras maiúsculas, não é preciso se preocupar.
5. O gráfico de candlestick será exibido e também salvo no arquivo grafico_ticker_data.png.

## Estrutura do Código
1. **Obtenção dos Dados**: O código solicita ao usuário o ticker da ação e obtém os dados históricos do intervalo de dias selecionado usando a biblioteca yfinance.
2. **Visualização do DataFrame**: O DataFrame contendo os dados da ação pode ser visualizado para comparação com o gráfico ou obtenção de outras informações necessárias.
3. **Preparação dos Dados***: Os dados são preparados para serem utilizados pela biblioteca mplfinance, com a definição do índice como a coluna 'Date'.
4. **Plotagem do Gráfico***: Um gráfico de candlestick é gerado para mostrar a variação dos preços da ação ao longo do período selecionado.
5. **Salvar o Gráfico***: O gráfico também é salvo em um arquivo PNG com o nome grafico_ticker_data.png.

## Personalização
- **Período dos Dados**: Você pode alterar o período para obter dados de outros intervalos, modificando o parâmetro period em data = yf.Ticker(ticker).history(period="1mo"). Exemplos: "1d", "5d", "1y".
- **Estilo do Gráfico**: O estilo do gráfico pode ser alterado mudando o parâmetro style na função mpf.plot(). Por exemplo, pode-se usar 'yahoo', 'default' ou 'nightclouds' para diferentes aparências.
- **Exibir Volume**: Para incluir o volume das transações no gráfico, mude volume=False para volume=True.

## Exemplo de Saída
O gráfico gerado mostrará as variações diárias de preço da ação, com candles verdes indicando alta e candles vermelhos indicando baixa.
O arquivo de saída será salvo no mesmo diretório com um nome específico para o ticker e a data de geração.

## Observações
Certifique-se de que o ticker inserido é válido e corresponde ao formato esperado pela biblioteca yfinance. Por exemplo, tickers da B3 (Bolsa de Valores do Brasil) geralmente têm a extensão ".SA".
A biblioteca yfinance depende da disponibilidade dos dados do Yahoo Finance, portanto, erros podem ocorrer se o serviço estiver indisponível.

## Licença
Este projeto é de uso livre e pode ser modificado conforme necessário.
