import os, shutil

files = os.listdir()
cfile_name = __file__.split('\\')[-1]

for file in files:
    if file == cfile_name:continue
    if not os.path.isfile(file):continue

    suffix = file.split('.')[-1]
    if not os.path.exists(suffix):
        os.mkdir(suffix)
    shutil.move(file,suffix)
