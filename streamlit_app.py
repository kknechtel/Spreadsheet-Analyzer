import tempfile
import pandas as pd
import streamlit as st

from financial_analyzer.analyzer import Analyzer
from financial_analyzer.charts import cash_flow_chart
from financial_analyzer import spreadsheet

st.set_page_config(page_title="Financial Analyzer", layout="wide")

if "analyzer" not in st.session_state:
    st.session_state.analyzer = Analyzer()
if "sheets" not in st.session_state:
    st.session_state.sheets = None
if "uploaded_path" not in st.session_state:
    st.session_state.uploaded_path = None
if "selected_sheet" not in st.session_state:
    st.session_state.selected_sheet = None

st.title("Financial Analyzer")

upload_tab, analysis_tab, viz_tab = st.tabs(["Upload", "Analysis", "Visualization"])

with upload_tab:
    uploaded_file = st.file_uploader("Upload Excel file", type=["xlsx", "xls"])
    if uploaded_file:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".xlsx") as tmp:
            tmp.write(uploaded_file.getbuffer())
            st.session_state.uploaded_path = tmp.name
        st.session_state.sheets = st.session_state.analyzer.process_file(
            st.session_state.uploaded_path
        )
        st.success("File processed")
        sheet_names = list(st.session_state.sheets.keys())
        st.session_state.selected_sheet = st.selectbox(
            "Select sheet", sheet_names
        )
        st.dataframe(st.session_state.sheets[st.session_state.selected_sheet])

with analysis_tab:
    if st.session_state.sheets:
        df = st.session_state.sheets[st.session_state.selected_sheet]
        if st.button("Analyze with LLM"):
            prompt = (
                "Provide insights for the following table:\n"
                + df.head().to_csv(index=False)
            )
            result = st.session_state.analyzer.analyze_with_llm(prompt)
            st.write(result)
    else:
        st.info("Upload a spreadsheet first.")

with viz_tab:
    if st.session_state.sheets:
        df = st.session_state.sheets[st.session_state.selected_sheet]
        numeric_df = spreadsheet.extract_numeric(df).dropna(how="all")
        cols = numeric_df.select_dtypes(float).columns
        if len(cols) >= 2:
            x_col = st.selectbox("X-axis", cols, key="xcol")
            y_col = st.selectbox("Y-axis", cols, key="ycol")
            fig = cash_flow_chart(numeric_df, x=x_col, y=y_col)
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Not enough numeric columns to plot.")
    else:
        st.info("Upload a spreadsheet first.")

