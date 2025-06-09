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
    st.title("Enhanced Excel Viewer")

    # Load data
    data = load_data()

    # Create AgGrid options for grouping and highlighting
    gb = GridOptionsBuilder.from_dataframe(data)
    gb.configure_default_column(groupable=True, sortable=True, filterable=True, editable=False)

    # Highlight cells conditionally (e.g., based on value)
    gb.configure_column("ColumnName", cellStyle={"backgroundColor": "lightyellow"})

    # Enable row grouping
    gb.configure_selection(selection_mode="single", use_checkbox=True)

    # Build grid options
    grid_options = gb.build()

    # Display data with AgGrid
    st.subheader("Excel Data with Grouping and Highlights")
    AgGrid(
        data,
        gridOptions=grid_options,
        enable_enterprise_modules=True,
        theme="alpine",  # Available themes: 'streamlit', 'alpine', 'balham', 'material'
    )

if __name__ == "__main__":
    main()
