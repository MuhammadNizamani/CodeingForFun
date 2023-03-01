import os


def find_folders(path):
    folder_names = []
    folder_links = []
    for dirpath, dirnames, filenames in os.walk(path):
        for dirname in dirnames:
            folder_path = os.path.join(dirpath, dirname)
            folder_names.append(dirname)
            folder_links.append(folder_path)
    return folder_names, folder_links


folder_names, folder_links = find_folders("E:\\")

print("Name of file")
for i, folder in enumerate(folder_names):
    if folder == "OpenLabeling":
        print(f"{i+1}. {folder} ({folder_links[i]})")
