import os
def pilih_file(folder_path: str = "DATA") -> str | None:
    """
    Menampilkan daftar file dalam folder dan meminta user memilih salah satunya.

    Args:
        folder_path (str): Nama folder tempat file disimpan (default: "DATA").

    Returns:
        str | None: Path lengkap file yang dipilih, atau None jika tidak ada.
    """
    try:
        files = os.listdir(folder_path)
        files = [f for f in files if os.path.isfile(os.path.join(folder_path, f))]

        if not files:
            print("⚠️ Tidak ada file dalam folder ini.")
            return None

        print("\n📂 Daftar file di folder:")
        for i, file in enumerate(files, start=1):
            print(f"{i}. {file}")

        while True:
            try:
                pilihan = int(input("Pilih nomor file: "))
                if 1 <= pilihan <= len(files):
                    file_terpilih = files[pilihan - 1]
                    print(f"✅ Kamu memilih file: {file_terpilih}")
                    return os.path.join(folder_path, file_terpilih)
                else:
                    print("❌ Nomor tidak valid, coba lagi.")
            except ValueError:
                print("❌ Input harus berupa angka.")

    except FileNotFoundError:
        print("❌ Folder tidak ditemukan.")
        return None