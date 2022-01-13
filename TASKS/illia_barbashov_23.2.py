import re
from docx import Document
import os

def repl(match: re.Match):
    arr = match.group(0).replace("/",".").split(".")
    if len(arr[1]) == 1:
        arr[1] = "0" + arr[1]

    return ".".join(arr)

def format_date(filename):
    document = Document(filename)
    for paragraph in document.paragraphs:
        for run in paragraph.runs:
            text = run.text
            if text != '\n':
                text = re.sub(r'(\d\d\d\d[\/|\.]\d{1,2}[\/|\.]\d\d)', repl, text)
                run.text = text

    fname, ext = os.path.splitext(filename)
    fname += '_'
    newfilename = fname + ext
    document.save(newfilename)


if __name__ == '__main__':
    import sys

    if len(sys.argv) == 1:  # якщо не вистачає параметрів, ввести
        filename = input(".docx file name: ")
    else:
        filename = sys.argv[1]
    format_date(filename)