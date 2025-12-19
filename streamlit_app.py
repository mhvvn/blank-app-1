import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np




st.markdown(
    """
    # My first app
    ## My second app
    ###### Heading level 6
    Hello, para calon praktisi data masa depan!

    ```python
    codest.code(code, language='python')
    ```

    """
)

code = """def hello():
    print("Hello, Streamlit!")"""
st.code(code, language='python')

st.text('Halo, calon praktisi data masa depan.')


st.latex(r"""
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
""")

st.text('ini contoh rumus dengan latex')

df = pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})

st.dataframe(data=df, width=500, height=150)

st.text('ini contoh dataframe')


df = pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})
st.table(data=df)

st.text('ini contoh tabel')


st.metric(label="Temperature", value="28 °C", delta="1.2 °C")
st.text('ini contoh metric')


x = np.random.normal(15, 5, 250)
 
fig, ax = plt.subplots()
ax.hist(x=x, bins=15)
st.pyplot(fig)

st.text('ini contoh bar chart')




all_users = ["Alice", "Bob", "Charly"]
with st.container(border=True):
    users = st.multiselect("Users", all_users, default=all_users)
    rolling_average = st.toggle("Rolling average")

np.random.seed(42)
data = pd.DataFrame(np.random.randn(20, len(users)), columns=users)
if rolling_average:
    data = data.rolling(7).mean().dropna()

tab1, tab2 = st.tabs(["Chart", "Dataframe"])
tab1.line_chart(data, height=250)
tab2.dataframe(data, height=250, use_container_width=True)


map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)
