import zipfile
import os

file = 'T22.12/image.zip'
packet_size = int(1024*600)

def split_zip(outfile):
    with open(outfile, "rb") as output:
        filecount = 0
        while True:
            data = output.read(packet_size)
            print(len(data))
            if not data:
                break
            with open("{}{:03}".format(outfile, filecount), "wb") as packet:
                packet.write(data)
            filecount += 1

def merge_zip(outfile):
    files = os.listdir(outfile[:-outfile[::-1].index('/')])
    cat = outfile[:-outfile[::-1].index('/')]
    filename = outfile[-outfile[::-1].index('/'):]
    name = filename[:-filename[::-1].index('.')-1]
    ext = filename[-filename[::-1].index('.'):]
    for i in reversed(range(len(files))):
        if filename not in files[i]:
            del files[i]
    zip_path = f'T22.12_rez/{name}_rez.{ext}'
    with open(zip_path, 'wb') as rez:
        for file in files:
            with open(cat + '/' + file, 'rb') as f:
                rez.write(f.read())
    z = zipfile.ZipFile(zip_path)
    z.extractall('T22.12_rez')

merge_zip(file)