import streamlit as st
import pandas as pd
from matplotlib import image
import plotly.express as px
import altair as alt
import os

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "layoff.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "layoffs.csv")
st.title("Dashboard - Layoff Data")

img = image.imread(IMAGE_PATH)
st.image(img)

layoff_dataset = pd.read_csv(DATA_PATH)

layoff_dataset.drop_duplicates(keep="first",inplace=True)
layoff_dataset["percentage_laid_off"]=layoff_dataset["percentage_laid_off"].fillna(0)
layoff_dataset["total_laid_off"]=layoff_dataset["total_laid_off"].fillna(0)
layoff_dataset.dropna(axis=0,inplace=True)
st.dataframe(layoff_dataset)

# layoff based upon location
layoff_based_upon_location=layoff_dataset.groupby("location")["total_laid_off"].sum().sort_values(ascending=False).head(10)
location_names=list(layoff_based_upon_location.index)
location_layoff_count=list(layoff_based_upon_location.values)


layoff_based_upon_location = pd.DataFrame(list(zip(location_names, location_layoff_count)),
               columns =['Location', 'Total No of Layoff'])
plot=px.bar(layoff_based_upon_location, x=layoff_based_upon_location["Location"], y=layoff_based_upon_location["Total No of Layoff"],title="top 10 locations based upon layoff ")
st.plotly_chart(plot)


# layoff based upon country
layoff_based_upon_country=layoff_dataset.groupby("country")["total_laid_off"].sum().sort_values(ascending=False).head(10)
plot=px.bar(layoff_based_upon_country,x=layoff_based_upon_country.index,y=layoff_based_upon_country.values,title="Top 10 countries based upon layoff").update_layout(
    xaxis_title="Country", yaxis_title="Layoff count"
)
st.plotly_chart(plot)

# layoff based upon companu
layoff_based_upon_company=layoff_dataset.groupby("company")["total_laid_off"].sum().sort_values(ascending=False).head(10)
plot=px.bar(layoff_based_upon_company,x=layoff_based_upon_company.index,y=layoff_based_upon_company.values,title="Top 10 companies based upon layoff data").update_layout(
    xaxis_title="Country", yaxis_title="total number of Layoff "
)
st.plotly_chart(plot)