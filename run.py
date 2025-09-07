from data_selection import pilih_file
from setting.checking_handler import checking_yaml
from core.core import full_main


def start():
    """
    Loop utama untuk interaksi dengan user.
    """
    while True:
        try:
            checking_yaml()
            print(
                """
Pilih Salah Satu:
1. Input Data
exit. Keluar
"""
            )
            command = input("Masukkan perintah : ").strip().lower()

            if command == "1":
                file = pilih_file()
                if file:
                    full_main(file)

            elif command == "exit":
                print("Program dihentikan oleh pengguna.")
                break

        except KeyboardInterrupt:
            print("\nProgram dihentikan dengan Ctrl+C.")
            break


def main():
    """
    Entry point aplikasi Auto Data Pipeline.
    """
    print(
        """
  /$$$$$$  /$$   /$$ /$$$$$$$   /$$$$$$  /$$$$$$$  /$$       /$$$$$$ /$$   /$$ /$$$$$$$$
 /$$__  $$| $$  | $$| $$__  $$ /$$__  $$| $$__  $$| $$      |_  $$_/| $$$ | $$| $$_____/
| $$  \ $$| $$  | $$| $$  \ $$| $$  \ $$| $$  \ $$| $$        | $$  | $$$$| $$| $$      
| $$$$$$$$| $$  | $$| $$  | $$| $$$$$$$$| $$$$$$$/| $$        | $$  | $$ $$ $$| $$$$$   
| $$__  $$| $$  | $$| $$  | $$| $$__  $$| $$____/ | $$        | $$  | $$  $$$$| $$__/   
| $$  | $$| $$  | $$| $$  | $$| $$  | $$| $$      | $$        | $$  | $$\  $$$| $$      
| $$  | $$|  $$$$$$/| $$$$$$$/| $$  | $$| $$      | $$$$$$$$ /$$$$$$| $$ \  $$| $$$$$$$$
|__/  |__/ \______/ |_______/ |__/  |__/|__/      |________/|______/|__/  \__/|________/
                                                                                        
                                                                                        
Auto Data Pipeline - Pre Alpha 0.1
Apa yang baru:
- Menambahkan identifier file CSV, Parquet, dan JSON.
- Menambahkan deteksi null dan duplikat.
"""
    )
    start()


if __name__ == "__main__":
    main()
