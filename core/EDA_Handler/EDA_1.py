import pandas as pd
import numpy as np
from core.utils.checking_nulss_nan import checking_n_20

def EDA_csv(folder_data):
    df = pd.read_csv(folder_data)
    hasil_eda_pertama = f'''
Hasil shaping data: {df.shape}
Isi Colomn dari file yang di kasih: {df.columns}'''
    print(hasil_eda_pertama)
    checking_n_20(df)
    