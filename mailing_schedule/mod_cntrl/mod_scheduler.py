import time
import os
import os.path as op
from datetime import datetime

from sender import Sender
from receiver import Receiver
from config_dict import ConfigDict


class Scheduler:

    def __init__(self, datetime_str, sender):
        self._datetime = datetime.strptime(datetime_str, "%d.%m.%Y %H:%M")
        self._sender = sender

    def run(self):
        while True:
            if datetime.now() >= self._datetime:
                break

            time.sleep(60)

        self._sender.send_all()

def form_recipients(files_path, your_mail, your_password, event_date):
    members = list()
    with open(op.join(files_path, 'group.txt'), 'r', encoding='utf-8') as f:
        for line in f:
            mail, name, auto = line.strip().split(';')
            if not auto.strip():
                members.append(mail.strip())
    receiver = Receiver(your_mail, your_password, event_date=event_date)
    from_list = receiver.get_senders(members)
    with open(op.join(files_path, 'recipients.txt'), 'w') as f:
        for addr in from_list:
            f.write("{}\n".format(addr))
    absent = list(set(members) - set(from_list))
    print("Absent:", *absent, sep='\n')

if __name__ == '__main__':
    config = ConfigDict('config.txt')
    params = config.getconfig()
    files_path = params['files_path']

    event_date_time = datetime.strptime(
        params['practice_date_time'], "%d.%m.%Y %H:%M")
    event_date = event_date_time.strftime("%d-%b-%Y")
    form_recipients(files_path, params['your_mail'], params['your_password'],
                    event_date)

    with open(op.join(files_path, 'practice', 'text.txt'), 'r',
              encoding='utf-8') as f:
        practice_common_text = f.read()
    with open(op.join(files_path, 'recipients.txt'), 'r') as f:
        recipients = f.read().split()
    items = os.listdir(op.join(files_path, 'practice'))
    practice_files = [op.join(files_path, 'practice', f)
             for f in items if op.isfile(op.join(files_path, 'practice', f))
                      and f != 'text.txt']

    sender = Sender(
        params['your_mail'], params['your_password'], params['subject_practice'],
        practice_common_text, recipients, practice_files, params['as_attachment'],
        params.get('randomize', False))
    scheduler = Scheduler(params['practice_date_time'], sender)
    scheduler.run()
    print("Mails were sent_2")
