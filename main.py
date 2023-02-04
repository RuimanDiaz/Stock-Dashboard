import streamlit as st
import yfinance as yf
import requests as rq

#sidebar
st.sidebar.markdown("<h1 style='text-align: center; color: purple;'>Stock's </h1>", unsafe_allow_html=True)
st.sidebar.image('otra-modified.png')
option=st.sidebar.selectbox('Topics',('Chart','Financials','News'))
stock = st.sidebar.text_input("type stock to start",max_chars=4, key="name")
stock =stock.upper()
st.sidebar.markdown("<h5 style='text-align: center; color: grey;'>By Ruiman Diaz</h5>", unsafe_allow_html=True)

# Newsapi 
url = ('https://newsapi.org/v2/everything?'
       'q='+stock+'&'
       'from=2023-02-04&'#year-month-day
       'sortBy=popularity&'
       'apiKey=YOUR_API_KEY')
response=rq.get(url)

# yfinance data
stock_name=yf.Ticker(str(stock))

data = stock_name.history(period='1d',start='2010-5-31',end='2020-5-31')

if stock=='':
   
   st.markdown("<h2 style='text-align: center; color: purple;'>Please select a stock to start </h2>", unsafe_allow_html=True)
  # st.image('https://eodhistoricaldata.com/financial-apis-blog/wp-content/uploads/2019/04/nasdaq_company_logos.jpg')
   st.image('https://wallpapercave.com/wp/wp9587602.jpg')
if option=='Financials':

   st.markdown("<h2 style='text-align: center; color: purple;'>Financial Information</h2>", unsafe_allow_html=True)
   st.write(f'you are watching the {stock} financial information')

   
   st.write(stock_name.analyst_price_target)
   
   st.caption('Balance sheet')
   st.write(stock_name.balance_sheet)


   st.caption('Income Statement')
   st.write(stock_name.income_stmt)

   st.caption('Cash flow')
   stock_name.cash_flow

   st.caption('what are others thinking? ')
   stock_name.recommendations_summary

if option =='Chart':
   st.markdown(f"<h2 style='text-align: center; color: purple;'>{stock }</h2>", unsafe_allow_html=True)
   st.line_chart(data.Close)
   st.line_chart(data.Volume)

if option=='News':
   st.markdown("<h2 style='text-align: center; color: purple;'>Recent news</h2>", unsafe_allow_html=True)
   st.write('')
   for p in response.json()['articles']:
    st.write(f'Title : '+ p['title' ]+' | '+p['publishedAt'])
    st.write(f'Url : ' +p['url'])
    st.write('')