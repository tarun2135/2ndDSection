import streamlit as st
import pandas as pd

def main():
    # Set page layout to wide (full screen)
    st.set_page_config(layout="wide")

    # Updated file path
    file_path = r"C:\Users\lenovo\Desktop\hii\1DSection_ECE\SecD1st.xlsx"
    df = load_data(file_path)
    if df is not None:
        # Filter dataframe for Section B
        df_section_b = df[df['Section'] == 'D']
        if not df_section_b.empty:
            # Convert dataframe to HTML table and render it using markdown
            st.markdown(get_table_html(df_section_b), unsafe_allow_html=True)
        else:
            st.write("No data available for Section B.")
    else:
        st.write("No data to display.")

def get_table_html(df):
    # Convert DataFrame to HTML table string
    table_html = df.to_html(index=False, escape=False, classes=["dataframe"])

    # Modify HTML string to set table width to 100% and center align text
    table_html = table_html.replace('<table', '<table style="width:100%; text-align:center;"')

    return table_html

def load_data(file_path):
    try:
        df = pd.read_excel(file_path)
        return df
    except Exception as e:
        st.error(f"An error occurred while loading the data: {e}")
        return None

if __name__ == "__main__":
    main()
