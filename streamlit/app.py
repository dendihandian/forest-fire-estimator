import streamlit as st
from pages.classification import classfication_page
from pages.regression import regression_page

st.title('Forest Fire Estimator', anchor=None)
st.write("""
    - Exploratory Data Analysis and Modeling
        - [Pre Modeling](https://github.com/dendihandian/forest-fire-estimator/blob/main/forest-fire-estimator-premodeling.ipynb)
        - [Regression Modeling](https://github.com/dendihandian/forest-fire-estimator/blob/main/forest-fire-estimator-modeling.ipynb)
    - [Dataset](https://archive.ics.uci.edu/ml/datasets/forest+fires)
""")

with st.sidebar:

    page = st.selectbox(
        "Select page",
        ("Regression", "Classification")
    )

if page == 'Regression':
    regression_page()
else:
    classfication_page()