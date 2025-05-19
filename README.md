# Financial Analyzer

This project provides a simple financial spreadsheet analysis tool built with **Streamlit**.
It allows users to upload spreadsheets, detect financial tables, perform basic analysis
with OpenAI, and visualize cash flow trends.

## Features

- Upload Excel spreadsheets with multi-sheet support
- Automatic table detection using `pandas` and `openpyxl`
- Identification of common financial statements
- Integration with OpenAI for additional insights (API key required)
- Storage of processed data in a local SQLite database
- Interactive visualizations with Plotly
- Docker configuration and GitHub Actions workflow for testing

## Quick Start

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the Streamlit app:
   ```bash
   streamlit run streamlit_app.py
   ```
3. Upload a spreadsheet and explore the **Upload**, **Analysis**, and **Visualization** tabs.

## Deployment

The project includes a `Dockerfile` for container-based deployment and a sample
GitHub Actions workflow for CI. See `docs/DEPLOYMENT.md` for details.

