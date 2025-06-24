import streamlit as st
import pandas as pd

st.set_page_config(page_title="CSV to JSON/SQL Converter", layout="centered")
st.title("📁 CSV to JSON/SQL Converter")

uploaded_file = st.file_uploader("Upload a CSV file", type="csv")
output_format = st.selectbox("Choose output format", ["json", "sql"])
table_name = st.text_input("SQL table name", value="my_table")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("📄 Uploaded Data", df)

    if output_format == "json":
        json_data = df.to_json(orient="records", indent=2)
        st.download_button("⬇️ Download JSON", json_data, file_name="output.json", mime="application/json")

    elif output_format == "sql":
        statements = []
        for _, row in df.iterrows():
            cols = ", ".join(f"{col}" for col in df.columns)
            # Safely escape single quotes in SQL values
            vals = ', '.join(f"'{str(val).replace('\'', '\'\'')}'" for val in row)
            sql = f"INSERT INTO {table_name} ({cols}) VALUES ({vals});"
            statements.append(sql)
        sql_script = "\n".join(statements)
        st.download_button("⬇️ Download SQL", sql_script, file_name="output.sql", mime="text/plain")
