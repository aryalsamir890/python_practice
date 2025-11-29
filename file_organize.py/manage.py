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

# upper is mine no such important logic or not more advanced 

# by the chatgpt best one !!!!
# .....
# ....
# ...
# ..
# .
import os
import shutil

# Path of your messy folder
folder = r"C:\Users\User\OneDrive\Desktop\ython.py\file_organize.py"

# List all files
files = os.listdir(folder)

for i in files:
    src = os.path.join(folder, i)

    # Skip if it is a folder
    if os.path.isdir(src):
        continue

    # Get extension safely
    _, ext = os.path.splitext(i)
    ext = ext.lower()  # make it lowercase

    # Decide destination folder
    if ext == ".mp4":
        dest_folder = os.path.join(folder, "Videos")
    elif ext in [".jpg", ".jpeg", ".png"]:
        dest_folder = os.path.join(folder, "Images")
    elif ext == ".pdf":
        dest_folder = os.path.join(folder, "Documents")
    else:
        dest_folder = os.path.join(folder, "Others")

    # Create folder if not exists
    os.makedirs(dest_folder, exist_ok=True)

    # Move file
    dest = os.path.join(dest_folder, i)
    shutil.move(src, dest)

print("Files organized successfully!")
