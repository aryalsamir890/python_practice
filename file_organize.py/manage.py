import os #os is a built-in Python module that helps you interact with the operating system:
# Check what files/folders exist
# Create folders
# Get file paths
# Work with directories
import shutil  #It is used for moving, copying, and deleting files/folders.

# code to move the files to the respective folders 

file=os.listdir(r"C:\Users\User\OneDrive\Desktop\ython.py\file_organize.py")
for i in file:
    if "." in i:
        if i.split(".")[1]=="mp4":
            shutil.move(r"C:\Users\User\OneDrive\Desktop\ython.py\file_organize.py\song.mp4",r"C:\Users\User\OneDrive\Desktop\ython.py\file_organize.py\video")
        elif i.split(".")[1]=="JPG":
            shutil.move(r"C:\Users\User\OneDrive\Desktop\ython.py\file_organize.py\pic.JPG",r"C:\Users\User\OneDrive\Desktop\ython.py\file_organize.py\photos")
        elif i.split(".")[1]=="pdf":
            shutil.move(r"C:\Users\User\OneDrive\Desktop\ython.py\file_organize.py\note.pdf",r"C:\Users\User\OneDrive\Desktop\ython.py\file_organize.py\pdfs")
        else:
            continue
    else:
        continue