import re

def repl(match: re.Match):
    arr = match.group(0).replace("/",".").split(".")
    if len(arr[1]) == 1:
        arr[1] = "0" + arr[1]

    return ".".join(arr)


if __name__ == '__main__':
    with open('t20-1-input.text') as f:
        lines = f.readlines()
        res = []
        for line in lines:
            res.append(re.sub(r'(\d\d\d\d[\/|\.]\d{1,2}[\/|\.]\d\d)', repl, line))

        for line in res:
            print(line)
