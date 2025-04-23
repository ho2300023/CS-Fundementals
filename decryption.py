from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import os

def load_key(path='key.bin'):
    with open(path, 'rb') as key_file:
        return key_file.read()

def decrypt_file(file_path, key):
    try:
        with open(file_path, 'rb') as f:
            encrypted_data = f.read()

        iv = encrypted_data[:16]
        ct = encrypted_data[16:]

        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted_data = unpad(cipher.decrypt(ct), AES.block_size)

        with open(file_path, 'wb') as f:
            f.write(decrypted_data)

        print(f"[+] Decrypted: {file_path}")
    except Exception as e:
        print(f"[-] Failed to decrypt {file_path}: {e}")

def main():
    key = load_key()

    file_path = input("Enter the full path to the encrypted file: ").strip()
    if not os.path.isfile(file_path):
        print("[-] File not found.")
        return

    decrypt_file(file_path, key)

if __name__ == "__main__":
    main()
