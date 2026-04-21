import yfinance as yf   
import streamlit as st  
import pandas as pd
import os


st.write("""# Stock Price App""")

tickerSymbol = 'GOOGL'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(start='2010-1-1', end='2012-1-1')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)