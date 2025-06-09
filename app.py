import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder

# Load data from Excel file
@st.cache_data
def load_data():
    file_path = "Sample - CDM POC.xlsx"
    sheet_data = pd.read_excel(file_path, sheet_name="Sheet1")
    return sheet_data

# Streamlit App
def main():
    st.title("Excel Data Viewer with AgGrid")

    # Load data
    data = load_data()

    # Add grouping and interactivity
    gb = GridOptionsBuilder.from_dataframe(data)
    gb.configure_default_column(groupable=True, sortable=True, filterable=True)
    grid_options = gb.build()

    st.subheader("Interactive Data Viewer")
    AgGrid(data, gridOptions=grid_options)

if __name__ == "__main__":
    main()
