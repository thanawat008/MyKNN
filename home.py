import streamlit as st
import pandas as pd

st.title("Hello")
st.header("Hello")
st.subheader("Profile")

st.image('./img/man.jpg')
st.subheader("Thanawat Phongpae")

dt=pd.read_csv('./data/iris-3.csv')
st.header("ข้อมูลดอกไม้")
st.write(dt.head(10))