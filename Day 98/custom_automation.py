from pathlib import Path
import shutil

DOWNLOADS = Path.home() / "Downloads"

FOLDERS = {
    "Images": [".jpg",".jpeg",".png",".gif",".webp"],
    "Documents": [".pdf",".docx",".doc",".txt",".pptx",".xlsx",".csv"],
    "Videos": [".mp4",".mkv",".mov",".avi"],
    "Music": [".mp3",".wav",".aac"],
    "Archives": [".zip",".rar",".7z"],
    "Programs": [".exe",".msi"],
}

for folder in FOLDERS:
    (DOWNLOADS/folder).mkdir(exist_ok=True)

for item in DOWNLOADS.iterdir():
    if item.is_file():
        for folder, exts in FOLDERS.items():
            if item.suffix.lower() in exts:
                dest=DOWNLOADS/folder/item.name
                if not dest.exists():
                    shutil.move(str(item), str(dest))
                break

print("Downloads organized.")
