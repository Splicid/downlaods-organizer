import os, sys, shutil, random
import tkinter as tk
from pathlib import Path


window = tk.Tk()

# Paths of all directorys being used
download_path = Path.home()/ "Downloads"
desktop_path = Path.home()/ "Desktop"
pic_path = Path.home()/ "Desktop/Images"
exe_path = Path.home()/ "Desktop/Executable"
zip_path = Path.home()/ "Desktop/Zips"
document_path = Path.home()/ "Desktop/Docs"
random_path = Path.home()/ "Desktop/Random Files"

# List of paths that are being used
dict = [pic_path, exe_path, zip_path, document_path, random_path]

program_life = True

for folder in dict:
    try:
        if os.path.exists(folder):
            print(f"Path Exists for {folder}" )
        else:
            os.mkdir(folder)
    except ValueError:
        print(ValueError)

Dict = {".exe":exe_path, ".jpg":pic_path, ".xls":document_path, ".csv":document_path, ".xlsx":document_path, ".pdf":document_path, ".zip":zip_path}

while program_life:
    # Creates a list of any files in downloads
    dir_list = os.listdir(download_path)

    # checks download directory size 
    directory_size = len(dir_list)

    # if download directory size is more than 0 loop well run
    while directory_size > 0:
        dir_list = os.listdir(download_path)
        directory_size = len(dir_list)

        for files in dir_list:
            split = os.path.splitext(files)
            dict_check = Dict.get(split[1])

            if dict_check == None:
                shutil.move(f"{download_path}/{files}", f"{random_path}/{files}")
            else:
                shutil.move(f"{download_path}/{files}", f"{dict_check}/{files}")
 
