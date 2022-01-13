import os
# /home/illia/Documents
# /home/illia/Downloads
import time

if __name__ == '__main__':
    dir1 = input("First directory: \n")
    dir2 = input("Second directory: \n")
    out = input("Output file: \n")
    output = open(out, 'w+')

    files = set(os.listdir(dir1)).intersection(set(os.listdir(dir2)))
    res = []
    for f in files:
        t = (dir1 + '/' + f, dir2 + '/' + f)
        res.append((dir1 + '/' + f, dir2 + '/' + f))
        if abs(os.path.getctime(t[0]) - os.path.getctime(t[1])) != 0:
            print("{} - created:  {}, {} - created: {}".format(t[0], time.ctime(os.path.getctime(t[0])), t[1], time.ctime(os.path.getctime(t[1]))), file=output)
        else:
            print("{} - {} - both created: {}".format(t[0],t[1], time.ctime(os.path.getctime(t[0]))), file=output)


