import os

def find_files(start_dir, extensions):
    found_files = []
    for root, dirs, files in os.walk(start_dir):
        for file in files:
            if file.lower().endswith(tuple(extensions)):
                found_files.append(os.path.join(root, file))
    return found_files

def save_log(file_list, log_path='files.log'):
    with open(log_path, 'w') as log_file:
        for file_path in file_list:
            log_file.write(file_path + '\n')

def main():
    # Example usage
    user_dir = input("Enter the directory to search: ").strip()
    if not os.path.isdir(user_dir):
        print("Invalid directory.")
        return
    
    file_types = ['.txt', '.docx', '.jpg']
    print(f"Searching for files with extensions: {file_types}")
    result_files = find_files(user_dir, file_types)
    
    save_log(result_files)
    print(f"Found {len(result_files)} file(s). Paths saved to 'files.log'.")

if __name__ == "__main__":
    main()
