import os

directory  = "C:/local/9 class/Script_languages/list_of_files"

list_file = "names.txt"
names = []

with open(directory + "/" + list_file, "r") as f:
    names = [line.strip() for line in f if line.strip()]

print("names : ")
print(names)

for name in names:
    file_path = os.path.join(directory, name + ".txt")
    with open(file_path, "w") as new_file:
        new_file.write(f"Hello {name}")