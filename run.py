from setting.checking_handler import checking_yaml
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
