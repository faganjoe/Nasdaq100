import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import yfinance as yf

st.title('Nasdaq Stock App')

st.sidebar.header('User Input')


@st.cache
def load_data():
    url = 'https://en.wikipedia.org/wiki/NASDAQ-100#Components'
    html = pd.read_html(url, header=0)
    df = html[3]
    return df


df = load_data()

sector = df.groupby('GICS Sector')

sorted_sector_unique = sorted(df['GICS Sector'].unique())
selected_sector = st.sidebar.multiselect('Sector', sorted_sector_unique, sorted_sector_unique)

df_selected_sector = df[(df['GICS Sector'].isin(selected_sector))]

st.header('Display Companies in Selected Sector')
st.write('Data Dimension: ' + str(df_selected_sector.shape[0]) + ' rows and ' + str(
    df_selected_sector.shape[1]) + ' columns.')
st.dataframe(df_selected_sector)

st.title('Stock Comparison')
ticker1 = st.selectbox('Company', df['Ticker'])
ticker2 = st.selectbox('Company', df['Ticker'], key='company2')

tickerData1 = yf.Ticker(ticker1)
tickerData2 = yf.Ticker(ticker2)

tickerDf1 = tickerData1.history(period='1d', start='2010-5-31', end='2020-5-31')
tickerDf2 = tickerData2.history(period='1d', start='2010-5-31', end='2020-5-31')


st.line_chart(tickerDf1.Close)
st.line_chart(tickerDf2.Close)


