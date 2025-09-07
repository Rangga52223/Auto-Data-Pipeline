import pandas as pd
import os

def main_data_input(data_file):
    # Ambil ekstensi file
    _, ext = os.path.splitext(data_file)
    ext = ext.lower()

    if ext == ".csv":
        return data_csv(data_file)
    elif ext == ".parquet":
        return data_parquet(data_file)
    elif ext == ".json":
        return data_json(data_file)
    else:
        raise ValueError(f"Format file {ext} tidak didukung. Gunakan CSV, Parquet, atau JSON.")

def data_parquet(data_files):
    df = pd.read_parquet(data_files)
    print('Data Yang kamu Input adalah parquet')
    print('Jumlah baris dan kolom data:', df.shape)
    return(df)

def data_csv(data_files):
    df = pd.read_csv(data_files)
    print('Data Yang kamu Input adalah CSV')
    print('Jumlah baris dan kolom data:', df.shape)
    return(df)

def data_json(data_files):
    df = pd.read_csv(data_files) 
    print('Data Yang kamu Input adalah Json')
    print('Jumlah baris dan kolom data:', df.shape)
    return(df)
   