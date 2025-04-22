import os

def collect_files(directory):
    with open('files.log', 'w') as log:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith((".txt", ".jpg", ".docx")):
                    full_path = os.path.join(root, file)
                    print(full_path)
                    log.write(full_path + '\n')

# Run the script
if __name__ == "__main__":
    path = input("Specify the path to use: ")
    collect_files(path)
