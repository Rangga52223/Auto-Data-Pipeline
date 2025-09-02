from setting.checking_handler import checking_yaml
import os
def start():
    while True:
        try:
            checking_yaml()
            print('''
Pilih Salah Satu:
1.Full Auto Pipeline
2.EDA
3.Analysis
4.Processing
5.Intergrate AI Framwork
6.Predict Data
''')
            command = input("Masukkan perintah : ").strip().lower()
            
            if command == "exit":
                print("Program dihentikan oleh pengguna.")
                break

        except KeyboardInterrupt:
            print("\nProgram dihentikan dengan Ctrl+C.")
            break

def list_files(folder_path):
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    
    print("Daftar file:")
    for i, f in enumerate(files, start=1):
        print(f"{i}. {f}")
    
    return files

def main():
    print("""
  /$$$$$$  /$$   /$$ /$$$$$$$   /$$$$$$  /$$$$$$$  /$$       /$$$$$$ /$$   /$$ /$$$$$$$$
 /$$__  $$| $$  | $$| $$__  $$ /$$__  $$| $$__  $$| $$      |_  $$_/| $$$ | $$| $$_____/
| $$  \ $$| $$  | $$| $$  \ $$| $$  \ $$| $$  \ $$| $$        | $$  | $$$$| $$| $$      
| $$$$$$$$| $$  | $$| $$  | $$| $$$$$$$$| $$$$$$$/| $$        | $$  | $$ $$ $$| $$$$$   
| $$__  $$| $$  | $$| $$  | $$| $$__  $$| $$____/ | $$        | $$  | $$  $$$$| $$__/   
| $$  | $$| $$  | $$| $$  | $$| $$  | $$| $$      | $$        | $$  | $$\  $$$| $$      
| $$  | $$|  $$$$$$/| $$$$$$$/| $$  | $$| $$      | $$$$$$$$ /$$$$$$| $$ \  $$| $$$$$$$$
|__/  |__/ \______/ |_______/ |__/  |__/|__/      |________/|______/|__/  \__/|________/
                                                                                        
                                                                                        
Auto Data Pipeline - Pre Alpha 0.1""")
    start()


if __name__ == "__main__":
    main()
