import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder, JsCode

def load_data():
    return pd.DataFrame({
        "Name": ["Alice", "Bob", "Charlie"],
        "Score": [95, 88, 92]
    })

def main():
    st.title("CDM - Proof of Concept")

    # Dummy input fields
    col1, col2, col3 = st.columns(3)
    name = col1.text_input("Name", "")
    country = col2.selectbox("Country", ["", "India", "Japan", "France", "Spain"], index=0)
    geo = col3.selectbox("Geo", ["", "India", "Japan", "France", "Spain"], index=0)

    data = load_data()

    gb = GridOptionsBuilder.from_dataframe(data)
    gb.configure_default_column(editable=True, resizable=True)

    # Optional cell renderer for first row
    checkbox_renderer = JsCode("""
    function(params) {
        if (params.node.rowIndex === 0) {
            return '☑️ ' + params.value;
        } else {
            return params.value;
        }
    }
    """)
    gb.configure_column("Name", cellRenderer=checkbox_renderer)

    grid_options = gb.build()

    AgGrid(data, gridOptions=grid_options, enable_enterprise_modules=True, theme="alpine")

if __name__ == "__main__":
    main()
