import yfinance as yf
import mplfinance as mpf
import pandas as pd
from datetime import datetime

# Obtenção de dados
ticker = input('Escreva o ticker da ação que deseja: ').upper()
data = yf.Ticker(ticker).history(period="1mo")

# Configuração para visualização dos dados como um dataframe
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
print(data)

# Preparar o DataFrame para mplfinance
data.reset_index(inplace=True)
data.set_index('Date', inplace=True)

# Plotar o gráfico de candlestick
mpf.plot(data, type='candle', style='charles', title=f'Gráfico dos últimos 30 dias - {ticker}', xlabel='Data',
         ylabel='Preço', volume=False)

# Salvar o gráfico em arquivo
mpf.plot(data, type='candle', style='charles', title=f'Gráfico dos últimos 30 dias - {ticker}', xlabel='Data',
         ylabel='Preço', volume=False, savefig=f'grafico_{ticker}_{datetime.now().strftime("%Y-%m-%d")}.png')
