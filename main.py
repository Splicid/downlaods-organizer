import os, sys, shutil, random, pystray, threading
import tkinter as tk
from pathlib import Path
from PIL import Image, ImageDraw



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

def create_image(width, height, color1, color2):
    # Generate an image and draw a pattern
    image = Image.new('RGB', (width, height), color1)
    dc = ImageDraw.Draw(image)
    dc.rectangle(
        (width // 2, 0, width, height // 2),
        fill=color2)
    dc.rectangle(
        (0, height // 2, width // 2, height),
        fill=color2)

    return image

def program_status(icon, item):
    if str(item) == "Exit":
        icon.stop()
    elif str(item) == "Stop Loop":
        global program_life
        program_life = False


def run_icon():
    # In order for the icon to be displayed, you must provide an icon
    icon = pystray.Icon(
        'File Organizer', icon=create_image(64, 64, 'black', 'white'), menu=pystray.Menu(
            pystray.MenuItem("Stop Loop", program_status),
            pystray.MenuItem("Exit", program_status)
        ))

    # To finally show you icon, call run
    icon.run()

def main_loop():
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
 

Thread1 = threading.Thread(target=run_icon)
Thread2 = threading.Thread(target=main_loop)
Thread1.start()
Thread2.start()
