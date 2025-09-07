import pandas as pd

def cek_null(df, aksi=None):
    null_counts = df.isnull().sum()
    null_counts = null_counts[null_counts > 0]  # hanya kolom yang ada null

    if null_counts.empty:
        print("✅ Tidak ada nilai null pada DataFrame.")
        return df

    print("🔎 Kolom dengan nilai null:")
    for col, count in null_counts.items():
        print(f"- {col}: {count} nilai null")

    # Opsi penanganan
    if aksi is None:
        print("\nPilih aksi untuk menangani nilai null:")
        print("1. Ganti dengan 0")
        print("2. Hapus baris yang mengandung null")
        print("3. Hapus kolom yang seluruhnya null")
        print("4. Lewati (tidak melakukan perubahan)")
        pilihan = input("Masukkan pilihan (1/2/3/4): ")
    else:
        pilihan = str(aksi)

    if pilihan == "1":
        df = df.fillna(0)
        print("➡️ Semua nilai null diganti dengan 0")
    elif pilihan == "2":
        df = df.dropna()
        print("➡️ Baris yang mengandung null dihapus")
    elif pilihan == "3":
        df = df.dropna(axis=1, how="all")
        print("➡️ Kolom yang seluruhnya null dihapus")
    elif pilihan == "4":
        print("➡️ Tidak ada perubahan dilakukan")
    else:
        print("❌ Pilihan tidak valid. Tidak ada perubahan dilakukan.")

    return df
