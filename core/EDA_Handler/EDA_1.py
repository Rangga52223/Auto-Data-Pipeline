import pandas as pd
import numpy as np
from core.EDA_Handler.null_handler import cek_null

def main_eda(df):
    auto_data_explore(df)

def auto_data_explore(df):
    print("\n===== 🔎 5 Data Teratas =====")
    print(df.head())

    print("\n===== 📊 Info Data =====")
    df.info()

    print("\n===== 🚩 Cek Null =====")
    cek_null(df)  # jangan ditimpa dengan df, biar jelas fungsinya hanya ngecek

        