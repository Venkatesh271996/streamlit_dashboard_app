import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "tips.png")
DATA_PATH = os.path.join(dir_of_interest, "data", "tips.csv")

st.title("Dashboard - tips Data")

img = image.imread(IMAGE_PATH)
st.image(img)

df = pd.read_csv(DATA_PATH)
st.dataframe(df)

gender = st.selectbox("Select the Gender:", df['sex'].unique())

col1, col2 = st.columns(2)

fig_1 = px.histogram(df[df['sex'] == gender], x="total_bill")
col1.plotly_chart(fig_1, use_container_width=True)

fig_2 = px.box(df[df['sex'] == gender], y="total_bill")
col2.plotly_chart(fig_2, use_container_width=True)


col1, col2 = st.columns(2)

fig_1 = px.histogram(df[df['sex'] == gender], x="tip")
col1.plotly_chart(fig_1, use_container_width=True)

fig_2 = px.box(df[df['sex'] == gender], y="tip")
col2.plotly_chart(fig_2, use_container_width=True)


chart=px.scatter(df,x="tip",y="total_bill",color="sex",title="Tips Vs Total Bill")
st.plotly_chart(chart,use_container_width=True)

chart=px.bar(df,x="day",y="total_bill",color="day",title="Total Bill based upon day")
st.plotly_chart(chart,use_container_width=True)
