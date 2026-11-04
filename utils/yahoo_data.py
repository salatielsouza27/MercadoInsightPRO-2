def calculate_score(row):
    return 0
import pandas as pd
import yfinance as yf
def get_market_data(symbol,period="30d",interval="1h"):
    try:
        df=yf.download(tickers=symbol,period=period,interval=interval,auto_adjust=True,progress=False,threads=False)
        if isinstance(df.columns,pd.MultiIndex): df.columns=df.columns.get_level_values(0)
        return df.dropna()
    except Exception:return pd.DataFrame()
