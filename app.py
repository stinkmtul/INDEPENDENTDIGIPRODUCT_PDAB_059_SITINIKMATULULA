import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from page import eda, modelintegration

def main():
    st.sidebar.title('Navigasi')
    page = st.sidebar.selectbox('Pilih Halaman', ['Eda', 'Model Integration'])

    if page == 'Eda':
        eda.main()
    elif page == 'Model Integration':
        modelintegration.main()

if __name__ == "__main__":
    main()