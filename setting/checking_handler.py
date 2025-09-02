import yaml

def checking_yaml():
    'Mengecek telah disetting belum aplikasinya'
    with open("setting/settings.yaml", "r") as f:
        data = yaml.safe_load(f)
    if data["setup"]["is_setup"]== False:
        print('Kamu belum setup aplikasi ini, kamu wajib setup')
        print('link/alamat database kamu ?')
        command = input("Masukkan perintah : ").strip().lower()
        data["dataset"]["link"] = command
        print('Host database kamu ?')
        command = input("Masukkan perintah : ").strip().lower()
        data["dataset"]["host"] = command
        print('Api llm Kamu ?')
        print('-Langganan LLM khusus developer, mulai dari gemini/chat-gpt')
        command = input("Masukkan perintah : ").strip().lower()
        data["initial_settings"]["api_llm"] = command
        print('Api key Kamu ?')
        print('-api key dari langganan api ai, jika tidak ada bisa skip')
        command = input("Masukkan perintah : ").strip().lower()
        data["initial_settings"]["api_key"] = command
        print('Korelasi Toleran:')
        print('-batas minimal toleransi kolom saat korelasi')
        command = input("Masukkan perintah : ").strip().lower()
        data["initial_settings"]["tolerance_minimal_correlation"] = command
        data["setup"]["is_setup"] = True
        with open("setting/settings.yaml", "w") as f:
            yaml.safe_dump(data, f, default_flow_style=False, sort_keys=False)
        print('Setup Done !!!!')
