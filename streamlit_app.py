import streamlit as st
import pandas as pd

st.title("Microsoft Stock Data Dashboard by Rania Gaston")

df = pd.read_csv("msft.csv")

tabs = st.tabs(["📋 Raw Data", "📈 Price Chart", "📊 Volume Chart", "📉 Daily Change"])

with tabs[0]:
    st.subheader("Raw Data for MSFT")
    st.dataframe(df, use_container_width=True)

with tabs[1]:
    st.subheader("Closing Price for MSFT")
    st.line_chart(df["Close"])

with tabs[2]:
    st.subheader("Volume for MSFT")
    st.bar_chart(df["Volume"])

with tabs[3]:
    st.subheader("Daily Percentage Change in Microsoft Stock Price")
    df["Daily Change (%)"] = df["Close"].pct_change() * 100
    st.line_chart(df["Daily Change (%)"])
    st.write("This graph shows the daily percentage change in Microsoft's closing stock price.")
