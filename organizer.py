
**Code (organizer.py)**  
```python
import os, shutil

FOLDER = "Downloads"  # change to your folder path
EXT_MAP = {"Images": [".jpg", ".png"], "Docs": [".pdf", ".docx", ".txt"], "Videos": [".mp4"]}

for fname in os.listdir(FOLDER):
    fpath = os.path.join(FOLDER, fname)
    if os.path.isfile(fpath):
        ext = os.path.splitext(fname)[1]
        for folder, exts in EXT_MAP.items():
            if ext in exts:
                target = os.path.join(FOLDER, folder)
                os.makedirs(target, exist_ok=True)
                shutil.move(fpath, os.path.join(target, fname))
                print(f"Moved {fname} -> {folder}")
