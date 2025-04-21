import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
import base64

def generate_aes_key():
    return get_random_bytes(32)  # AES-256

def save_key(key, path='key.bin'):
    with open(path, 'wb') as key_file:
        key_file.write(key)

def encrypt_file(file_path, key):
    try:
        with open(file_path, 'rb') as f:
            data = f.read()
        
        cipher = AES.new(key, AES.MODE_CBC)
        ct_bytes = cipher.encrypt(pad(data, AES.block_size))
        iv = cipher.iv

        encrypted_data = iv + ct_bytes  # prepend IV for decryption
        
        with open(file_path, 'wb') as f:
            f.write(encrypted_data)
        
        print(f"Encrypted: {file_path}")
    except Exception as e:
        print(f"Failed to encrypt {file_path}: {e}")

def main():
    key = generate_aes_key()
    save_key(key)

    try:
        with open('files.log', 'r') as f:
            file_paths = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("files.log not found. Run Task 2 first.")
        return

    for file_path in file_paths:
        encrypt_file(file_path, key)

if __name__ == "__main__":
    main()
