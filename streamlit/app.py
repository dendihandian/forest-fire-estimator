import streamlit as st
from pages.classification import classfication_page
from pages.regression import regression_page
from pages.info import info_page

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
        ("Regression", "Classification", "Info")
    )

if page == 'Regression':
    regression_page()
if page == 'Classification':
    classfication_page()
else:
    info_page()