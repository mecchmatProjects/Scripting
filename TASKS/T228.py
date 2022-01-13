import os
import json
import datetime

def check():

    directory_to_monitor = 'T22.8/dir_to_monitor'
    directory_for_logs = 'T22.8/Log'

    def get_list(to_check):
        rez = {}
        rez_list = {}
        if to_check not in rez:
            rez[to_check] = {}
        files = os.listdir(to_check)
        for f in files:
            filename = to_check + '/' + f
            if os.path.isdir(filename):
                rez[to_check][f], rez_list_temp = get_list(filename)
                rez_list.update(rez_list_temp)
            else:
                rez[to_check][f] = {'size': os.path.getsize(filename), 'Last modification': os.path.getmtime(filename)}
                rez_list.update({filename: {'size': os.path.getsize(filename), 'Last modification': os.path.getmtime(filename)}})
        return rez, rez_list

    last_log = None
    compare = False 
    logs = os.listdir(directory_for_logs)
    if logs:
        logs = sorted(logs, key=lambda x: os.path.getmtime(directory_for_logs + '/' + x), reverse=True)
        last_log = logs[0]

    r, r2 = get_list(directory_to_monitor)
    dt = datetime.datetime.now().strftime('%m_%d_%Y %H_%M_%S')
    json.dump(r2, open(f'{directory_for_logs}/{dt}.json', 'w'), indent=4)

    if last_log:
        log_new = r2
        log_old = json.load(open(directory_for_logs + '/' + last_log, 'r'))

        new_files = list(set(log_new) - set(log_old))
        deleted_files = list(set(log_old) - set(log_new))
        old_files = list(set(log_old) & set(log_new))

        modified_files = []
        for f in old_files:
            if log_new[f]['Last modification'] != log_old[f]['Last modification']:
                modified_files.append(f)

        if len(new_files):
            print('New files:', new_files)
        if len(deleted_files):
            print('Deleted files:', deleted_files)
        if len(modified_files):
            print('Modified files:', modified_files)
        
        return new_files, deleted_files, modified_files
    return None, None, None

if __name__ == '__main__':
    check()
