import seaborn as sns
#import matplotlib.pyplot as plt
import streamlit as st

iris_df = sns.load_dataset("iris")

st.title("AI Innovator First Datasurfer Streamlit App")

st.header("Dataset")
st.write(iris_df)  

st.header("Dataset description")
st.write(iris_df.describe())

# interactive selection of x and y columns
st.header("Interactive plot")
x = st.selectbox("Enter x-axis column: ",options = iris_df.columns)
y = st.selectbox("Enter y-axis column: ",options = iris_df.columns)

st.scatter_chart(x=x, y=y, color="species", data=iris_df)