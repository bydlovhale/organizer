import os
import shutil

# Change: User prompted for folder 
FOLDER = input("Enter folder path to organize: ")

# Change: Extensions expanded
EXT_MAP = {
    "Images": [".jpg", ".jpeg", ".png"],
    "Docs": [".pdf", ".docx", ".txt", ".pptx"],
    "Videos": [".mp4", ".avi"]
}

for fname in os.listdir(FOLDER):
    fpath = os.path.join(FOLDER, fname)
    if os.path.isfile(fpath):
        ext = os.path.splitext(fname)[1]
        moved = False
        for folder, exts in EXT_MAP.items():
            if ext in exts:
                target = os.path.join(FOLDER, folder)
                os.makedirs(target, exist_ok=True)
                shutil.move(fpath, os.path.join(target, fname))
                print(f"Moved {fname} -> {folder}")
                moved = True
                break
        # Change: Unknown extensions go to 'Others'
        if not moved:
            other = os.path.join(FOLDER, "Others")
            os.makedirs(other, exist_ok=True)
            shutil.move(fpath, os.path.join(other, fname))
            print(f"Moved {fname} -> Others")
