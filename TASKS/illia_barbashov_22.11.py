import os.path as path
import shutil

def chunk_zip(large_zip, zip_size):
    chapters = 1
    buffer = ''
    with open(large_zip, 'rb') as src:
        while True:
            current_chunk = open(large_zip + '.%03d' % chapters, 'wb')
            written = 0
            while written < zip_size:
                if len(buffer) > 0:
                    current_chunk.write(buffer)
                current_chunk.write(src.read(min(1024, zip_size - written)))
                written += min(1024, zip_size - written)
                buffer = src.read(1)
                if len(buffer) == 0:
                    break
            current_chunk.close()
            if len(buffer) == 0:
                break
            chapters += 1


def zipfiles(src, dest, zip_size, zip_name = 'attachments'):
    shutil.make_archive(zip_name, 'zip', src)
    saved_zip = "{}/{}.zip".format(dest, zip_name)
    file_size = path.getsize(saved_zip)
    if file_size > zip_size:
        chunk_zip(saved_zip, zip_size)

if __name__ == '__main__':
    src = input("Directory to create archive: ")
    dest = input("result zip path : ")
    zip_size = int(input("zip size in megabytes: "))*1024*1024
    zipfiles(src, dest, zip_size)
