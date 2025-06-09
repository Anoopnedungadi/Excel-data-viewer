import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder

# Load data from Excel file
def load_data():
    file_path = "Sample - CDM POC.xlsx"
    sheet_data = pd.read_excel(file_path, sheet_name="Sheet1")
    return sheet_data

# Streamlit App
def main():
    st.title("CDM proof of concept")

    # Load data
    data = load_data()

    # First row setup
    header_row = data.iloc[[0]].copy()  # First row after headers
    header_row_style = {
        "fontWeight": "bold",
        "backgroundColor": "#f0f0f0",
    }

    # Manage visibility with checkbox
    show_remaining_rows = st.checkbox("Show additional rows", value=False)
    displayed_data = header_row if not show_remaining_rows else data

    # Create grid options
    gb = GridOptionsBuilder.from_dataframe(displayed_data)
    gb.configure_default_column(editable=True, resizable=True)
    gb.configure_column(data.columns[0], tooltipField="Confidence score: 95. Reason: SME weightage: 1, Multiple values: 2")
    grid_options = gb.build()

    # Apply styling for the header row
    if not show_remaining_rows:
        grid_options["rowStyle"] = header_row_style

    # Display the AgGrid
    st.subheader("Interactive Data Viewer")
    AgGrid(displayed_data, gridOptions=grid_options, enable_enterprise_modules=True, theme="alpine")

if __name__ == "__main__":
    main()
