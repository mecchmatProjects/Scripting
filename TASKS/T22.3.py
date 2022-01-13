import os

folder1 = 'T22.3_1'
folder2 = 'T22.3_2'

files_in_folder1 = set(os.listdir(folder1))
files_in_folder2 = set(os.listdir(folder2))

files_in_f2_f2 = files_in_folder1 & files_in_folder2

for filename in files_in_f2_f2:
    filesize1 = os.path.getsize(folder1 + '/' + filename)
    filesize2 = os.path.getsize(folder2 + '/' + filename)
    if filesize1 != filesize2:
        print(f'File "{filename}" in both directories has different size: {filesize1} and {filesize2} bytes!')