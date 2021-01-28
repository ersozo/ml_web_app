import streamlit as st

import numpy as np
import pandas as pd

st.title('My first app')

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40],
    'third column': [100, 200, 300, 400]
}))


st.button("Start")

row = st.slider("Row", 0,50)
col = st.slider("Column", 0,50)

data = np.ones((row,col))
st.write(data)


df = pd.DataFrame(np.array([[1, 3 ,5], [7, 9, 11], [34, 545, 76]]), columns= ["a", "b", "c"])
st.write(df)


