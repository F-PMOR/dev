#!/usr/bin/env python3
# This script is used to sort file in a directory by
# moving the file in the adhoc repository.
# each key represented by the file extension as a value that is the
# destination directory. 

from pathlib import Path

# CONSTANTES
HOMEDIR = Path.home()
SORTDIR = HOMEDIR / "Downloads" # / "test"
DUPLICATEDIR = SORTDIR.joinpath("duplicate")
FILETYPE = {
            ".7z" : "archives",
            ".gz" : "archives",
            ".rar" : "archives",
            ".zip" : "archives",
            ".bin" : "bin",
            ".dll" : "bin",
            ".exe" : "bin",
            ".msi" : "bin",
            ".sql" : "Base_de_donnees",
            ".py" : "dev",
            ".vsix" : "dev",
            ".azw" : "documents", # fichiers kindle
            ".csv" : "documents",
            ".doc" : "documents",
            ".docx" : "documents",
            ".json" : "documents",
            ".pdf" : "documents",
            ".ppt" : "documents",
            ".pptx" : "documents",
            ".pub" : "documents",
            ".txt" : "documents",
            ".vcf" : "documents",
            ".xls" : "documents",
            ".xlsx" : "documents",
            ".xlsx" : "documents",
            ".jpeg" : "images",
            ".png" : "images",
            ".tif" : "images",
            ".jpg" : "images",
            ".rpm" : "linux",
            ".repo" : "linux",
            ".deb" : "linux",
            ".mp3" : "music",
            ".m4a" : "music",
            ".wav" : "music",
            ".ogg" : "music",
            ".wma" : "music",
            ".mid" : "music",
            ".kdbx" : "securite",
            ".mp4" : "video",
            
            }


def duplicate(fichier):
    try: 
        fichier.rename(DUPLICATEDIR / file.name)
    except FileExistsError as err:
        print(f"☠  File :\n   -> '{file.name}' found in the directory : '{DUPLICATEDIR}'\n   -> File DELETED ! ☠")
        fichier.unlink()

#########
# main ##
#########
# create the trash directory for the first duplicate files found
DUPLICATEDIR.mkdir(exist_ok=True)
# search for file inside the directory that as to be sorted
for file in [f for f in SORTDIR.glob("*") if f.is_file()]:
    suffix=str(file.suffix.lower())
    destdir=FILETYPE.get(suffix, file.parent)
    pathdestdir = SORTDIR.joinpath(destdir)
    pathdestdir.mkdir(exist_ok=True)
    try: 
        file.rename(pathdestdir / file.name)
    except FileExistsError as err:
        print(f"⚠ : File : \n    -> '{file.name}' ever found in the directory : '{SORTDIR / destdir}'\n    -> Moved to : {DUPLICATEDIR} !\n    -> ☠  Check for duplication, Next time, the file will be deleted !")
        duplicate(file)
