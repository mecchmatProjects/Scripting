import os
import datetime

def get_list(to_check):
        rez_list = {}
        files = os.listdir(to_check)
        for f in files:
            filename = to_check + '/' + f
            if os.path.isdir(filename):
                rez_list.update(get_list(filename))
            else:
                rez_list[filename] = os.path.getmtime(filename)
        return rez_list

rez_list = get_list('T22.7')
rez_list_sorted = sorted(rez_list, key=lambda x: rez_list[x])

for r_l in rez_list_sorted:
    print(f'{rez_list[r_l]} - {r_l}')

print()
print(f'The oldest file is "{rez_list_sorted[0]}" and was created at {datetime.datetime.fromtimestamp(rez_list[rez_list_sorted[0]])}')