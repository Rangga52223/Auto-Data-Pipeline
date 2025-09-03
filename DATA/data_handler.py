import os
def list_files(folder_path):
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    
    print("Daftar file:")
    for i, f in enumerate(files, start=1):
        print(f"{i}. {f}")
    
    return files