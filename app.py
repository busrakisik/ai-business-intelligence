import streamlit as st
import pandas as pd

st.set_page_config(page_title="AI Business Intelligence System", layout="wide")

st.title("AI Business Intelligence System")
st.write("Upload a CSV file to explore your data.")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Data Preview")
    st.dataframe(df.head())

    st.subheader("Basic Info")
    st.write(f"Rows: {df.shape[0]}")
    st.write(f"Columns: {df.shape[1]}")

    numeric_cols = df.select_dtypes(include="number").columns.tolist()

    if numeric_cols:
        st.subheader("Summary Statistics")
        st.dataframe(df[numeric_cols].describe())

        selected_col = st.selectbox("Choose a numeric column for quick chart", numeric_cols)

        st.subheader(f"{selected_col} Chart")
        st.bar_chart(df[selected_col])
    else:
        st.warning("No numeric columns found in this file.")
else:
    st.info("Upload a CSV file to begin.")
