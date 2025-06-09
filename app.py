import streamlit as st
import pandas as pd

# Load data from Excel file
def load_data():
    file_path = "Sample - CDM POC.xlsx"
    sheet_data = pd.read_excel(file_path, sheet_name="Sheet1")
    return sheet_data

# Streamlit App
def main():
    st.title("Excel Data Viewer")

    # Load data
    data = load_data()

    # Display the data as a table
    st.subheader("Excel Data")
    st.dataframe(data, use_container_width=True)

    # Optionally, you can add features like row grouping or highlighting here.

if __name__ == "__main__":
    main()
