import pandas as pd
import plotly.express as px


def cash_flow_chart(df: pd.DataFrame, x: str, y: str):
    fig = px.line(df, x=x, y=y, title="Cash Flow Trend")
    return fig

