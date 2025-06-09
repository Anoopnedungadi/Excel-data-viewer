import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder, JsCode

# Load data from Excel file
def load_data():
    file_path = "Sample - CDM POC.xlsx"
    sheet_data = pd.read_excel(file_path, sheet_name="Sheet1")
    return sheet_data

def main():
    st.title("CDM - Proof of Concept")

    # Dummy input fields
    with st.container():
        col1, col2, col3 = st.columns(3)
        name = col1.text_input("Name", "")
        country = col2.selectbox("Country", ["", "India", "Japan", "France", "Spain"], index=0)
        geo = col3.selectbox("Geo", ["", "India", "Japan", "France", "Spain"], index=0)

    # Load data
    data = load_data()

    # Insert a dummy checkbox column
    data.insert(0, "Select", ["☐"] + [""] * (len(data) - 1))  # first row gets the checkbox

    # Configure grid
    gb = GridOptionsBuilder.from_dataframe(data)
    gb.configure_default_column(editable=True, resizable=True)

    # Tooltip example
    gb.configure_column(
        data.columns[2],  # Assuming this is the column you want tooltip on
        headerTooltip="Confidence score: 95. Reason: SME weightage: 1, Multiple values: 2"
    )

    # Bold + background color styling for first row
    row_style = JsCode("""
        function(params) {
            if (params.node.rowIndex === 0) {
                return { 'fontWeight': 'bold', 'backgroundColor': '#f0f0f0' };
            }
        };
    """)
    gb.configure_grid_options(getRowStyle=row_style)

    grid_options = gb.build()

    # Display grid
    st.subheader("Interactive Data Viewer")
    AgGrid(data, gridOptions=grid_options, enable_enterprise_modules=True, theme="alpine")

if __name__ == "__main__":
    main()
