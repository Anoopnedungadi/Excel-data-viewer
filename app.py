import streamlit as st
import pandas as pd

# Load data from Excel file
def load_data():
    file_path = "Sample - CDM POC.xlsx"
    sheet_data = pd.read_excel(file_path, sheet_name="Sheet1")
    return sheet_data

# Streamlit App
def main():
    st.title("Excel Data Viewer with Grouping Functionality")

    # Load data
    data = load_data()

    # Add a checkbox to toggle visibility of additional rows
    show_rows = st.checkbox("Show additional rows", value=False)

    # Extract the first row and the remaining rows
    header_row = data.iloc[[0]]  # First row after headers
    remaining_rows = data.iloc[1:]  # Other rows

    # Style the first row
    st.subheader("Visible Row")
    st.markdown(
        header_row.style.set_properties(**{
            "font-weight": "bold",
            "background-color": "#f0f0f0"
        }).to_html(), 
        unsafe_allow_html=True
    )

    # Conditionally show remaining rows
    if show_rows:
        st.subheader("Additional Rows")
        st.dataframe(remaining_rows, use_container_width=True)

if __name__ == "__main__":
    main()
