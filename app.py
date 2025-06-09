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
    st.title("CDM - proof of Concept")

    # Load data
    data = load_data()

    # Split the first row (header row) and remaining rows
    header_row = data.iloc[[0]]  # First row after headers
    remaining_rows = data.iloc[1:]  # Other rows

    # Create grid options for AgGrid
    gb = GridOptionsBuilder.from_dataframe(data)
    gb.configure_default_column(editable=True, resizable=True)

    # Add a checkbox in the first cell of the bold row
    gb.configure_column(
        data.columns[0],
        cellRenderer="""function(params) {
            if (params.node.rowIndex === 0) {
                return `<input type='checkbox' onclick='toggleRows()' /> ` + params.value;
            } else {
                return params.value;
            }
        }"""
    )

    # Add tooltip to bold row
    gb.configure_column(
        data.columns[1],
        tooltipField="Confidence score: 95. Reason: SME weightage: 1, Multiple values: 2"
    )

    # Set the bold row with styling
    grid_options = gb.build()
    grid_options["rowStyle"] = """function(params) {
        if (params.node.rowIndex === 0) {
            return {fontWeight: 'bold', backgroundColor: '#f0f0f0'};
        }
        return null;
    };"""

    # Display the AgGrid with the options
    st.subheader("Interactive Data Viewer")
    AgGrid(data, gridOptions=grid_options, enable_enterprise_modules=True, theme="alpine")

if __name__ == "__main__":
    main()
