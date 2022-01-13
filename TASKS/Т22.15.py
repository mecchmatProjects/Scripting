import os

dirs = os.listdir('T22.15/')

pairs = []
for i in range(len(dirs)):
    for j in range(i+1, len(dirs)):
        pairs.append([dirs[i], dirs[j]])

def check_pair(pair):
    first, second = pair
    first = os.listdir('T22.15/'+first)
    second = os.listdir('T22.15/'+second)
    all_files = list(set(first + second))
    in_both = list(set(first) & set(second))
    return len(in_both) / len(all_files), in_both

P = 0.4

for pair in pairs:
    percent, in_both = check_pair(pair)
    if percent > P:
        print(f'Pair: ({pair[0]}, {pair[1]}), percent: {round(percent*100)}%, files_in_both_dirs: {in_both}')
