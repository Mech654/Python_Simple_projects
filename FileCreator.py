import os

def create_files(filename, extension, num_files, directory):
    if not os.path.exists(directory):
        create_dir = input(f"Directory {directory} does not exist. Do you want to create it? (yes/no): ").strip().lower()
        if create_dir == "yes":
            os.makedirs(directory)
            print(f"Directory {directory} created.")
        else:
            print("No files will be created.")
            return
    
    for i in range(1, num_files + 1):
        file_name = f"{filename}_{i}{extension}"
        file_path = os.path.join(directory, file_name)
        with open(file_path, 'w') as file:
            pass  # Leave the file empty
        print(f"File created: {file_path}")

filename = input("Enter the base file name: ")
extension = input("Enter the file extension (e.g., .txt, .html): ")
num_files = int(input("Enter the number of files to create: "))
directory = input("Enter the directory where files will be created: ")

create_files(filename, extension, num_files, directory)
