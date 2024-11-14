import os

def change_file_extension(directory, old_ext, new_ext):
    for filename in os.listdir(directory):
        if filename.endswith(old_ext):
            base = os.path.splitext(filename)[0]
            new_filename = f"{base}{new_ext}"
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
            print(f"Renamed: {filename} -> {new_filename}")



directory = input("Enter the directory path: ")
old_ext = input("Enter the extension you want to change:")
new_ext = input("Enter the new extension:")
change_file_extension(directory, old_ext, new_ext)
