
def checking_n_20(data):
    jumlah_null = data.isnull().sum()
    print('Ini Jumlah Null',jumlah_null)
    kolom_Null = data.columns[data.isnull().any()]
    print('Ini kolom yang Terdapat Null:', kolom_Null)

    
