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
    st.title("Excel Data Viewer with Expandable Rows")

    # Load data
    data = load_data()

    # Add a group column for hierarchy
    data.insert(0, "Group", ["Main Row"] + ["Sub Row"] * (len(data) - 1))

    # Create AgGrid options for grouping and styling
    gb = GridOptionsBuilder.from_dataframe(data)
    gb.configure_default_column(groupable=True, sortable=True, filterable=True, editable=False)

    # Configure the grouping behavior
    gb.configure_column(
        "Group", 
        rowGroup=True, 
        hide=True  # Group column is used internally and doesn't need to be displayed
    )

    # Configure the first row's style
    gb.configure_grid_options(
        getRowStyle=lambda params: {
            "fontWeight": "bold",
            "backgroundColor": "#d3d3d3" if params["node"]["level"] == 0 else "white",
        }
    )

    # Build grid options
    grid_options = gb.build()

    # Display data with AgGrid
    st.subheader("Excel Data with Expandable Rows")
    AgGrid(
        data,
        gridOptions=grid_options,
        enable_enterprise_modules=True,
        theme="alpine",  # Available themes: 'streamlit', 'alpine', 'balham', 'material'
    )

if __name__ == "__main__":
    main()
