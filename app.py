import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder, JsCode

# Sample DataFrame
def load_data():
    return pd.DataFrame({
        "Name": ["Alice", "Bob", "Charlie"],
        "Score": [95, 88, 92]
    })

# Streamlit app
def main():
    st.title("CDM - Proof of Concept")

    # Dummy fields
    col1, col2, col3 = st.columns(3)
    name = col1.text_input("Name", "")
    country = col2.selectbox("Country", ["", "India", "Japan", "France", "Spain"])
    geo = col3.selectbox("Geo", ["", "India", "Japan", "France", "Spain"])

    # Load data
    data = load_data()

    # Configure AgGrid
    gb = GridOptionsBuilder.from_dataframe(data)
    gb.configure_default_column(editable=True)

    # Add a simple checkbox renderer to one column
    cell_renderer = JsCode("""
    function(params) {
        if (params.node.rowIndex === 0) {
            return "✅ " + params.value;
        }
        return params.value;
    }
    """)
    gb.configure_column("Name", cellRenderer=cell_renderer)

    grid_options = gb.build()

    AgGrid(data, gridOptions=grid_options, theme="alpine")

if __name__ == "__main__":
    main()
