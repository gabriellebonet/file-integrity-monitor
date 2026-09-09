import hashlib
import os
import time

def calc_hash(path_file):
    hash_sha256 = hashlib.sha256()
    try:
        with open(path_file, "rb") as f:
            for pack in iter(lambda: f.read(4096), b""):
                hash_sha256.update(pack)
        return hash_sha256.hexdigest()
    except FileNotFoundError:
        return None

def monitor_file(path_file, sec=3):
    if not os.path.exists(path_file):
        print(f"Erro: O arquivo '{path_file}' não existe.")
        return
        
    print(f"Registrando o Hash inicial do seguinte arquivo: '{path_file}'")
    first_hash = calc_hash(path_file)
    print(f"Hash atual: '{first_hash}'\n")
    print(f"Monitiramento iniciado... \n")

    try:
        while True:
            time.sleep(sec)
            current_hash = calc_hash(path_file)
            
            if current_hash is None:
                print(f"\nAlerta: O arquivo foi deletado!!")
                return
            elif current_hash != first_hash:
                print(f"\nAlerta: O arquivo foi alterado!")
                print(f"Primeiro Hash : '{first_hash}'")
                print(f"Hash atual: '{current_hash}'\n")
                first_hash = current_hash
            else:
                print("[OK] Arquivo intocado...", end="\r")
                
    except KeyboardInterrupt:
        print("Monitoramento finalizado.")

if __name__ == "__main__":
    test_file = "secret.txt"

    if not os.path.exists(test_file):
        with open(test_file, "w") as f:
            f.write("Texto teste teste!!")
    
    monitor_file(test_file)
