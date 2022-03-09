import yfinance as yf
import streamlit as st

st.write("""
# Stock Price App using Streamlit
Shown are the stock **closing price** and ***volume*** of various stock tickers
""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
tickerSymbol_coinbase = 'COIN'
#get data on this ticker
tickerData_coinbase = yf.Ticker(tickerSymbol_coinbase)
#get the historical prices for this ticker
tickerDf_coinbase = tickerData_coinbase.history(period='1d', start='2010-5-31', end='2022-3-01')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

tickerSymbol_google = 'GOOGL'
tickerData_google = yf.Ticker(tickerSymbol_google)
tickerDf_google = tickerData_google.history(period='1d', start='2010-5-31', end='2022-3-01')

tickerSymbol_btcusd = 'BTC-USD'
tickerData_btcusd = yf.Ticker(tickerSymbol_btcusd)
tickerDf_btcusd = tickerData_btcusd.history(period='1d', start='2010-5-31', end='2022-3-01')

tickerSymbol_nvidia = 'NVDA'
tickerData_nvidia = yf.Ticker(tickerSymbol_nvidia)
tickerDf_nvidia = tickerData_nvidia.history(period='1d', start='2010-5-31', end='2022-3-01')

# Coinbase
st.write("""
## Closing Price Coinbase
""")
st.line_chart(tickerDf_coinbase.Close)
st.write("""
## Volume Coinbase
""")
st.line_chart(tickerDf_coinbase.Volume)

# Google
st.write("""
## Closing Price Google
""")
st.line_chart(tickerDf_google.Close)
st.write("""
## Volume Google
""")
st.line_chart(tickerDf_google.Volume)

# BTCUSD
st.write("""
## Closing Price BTCUSD
""")
st.line_chart(tickerDf_btcusd.Close)
st.write("""
## Volume BTCUSD
""")
st.line_chart(tickerDf_btcusd.Volume)

# NVIDIA
st.write("""
## Closing Price NVIDIA
""")
st.line_chart(tickerDf_nvidia.Close)
st.write("""
## Volume NVIDIA
""")
st.line_chart(tickerDf_nvidia.Volume)