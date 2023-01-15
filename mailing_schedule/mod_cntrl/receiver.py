import re
import os
import os.path as op
import shutil
from datetime import datetime
import imaplib
import email
from email.header import decode_header

from config_dict import ConfigDict

class Receiver:
    def __init__(self, mail, password, report_file=None,
                 event_date=None, results_path=None):
        self._mail = mail
        self._password = password
        self._report_file = report_file
        self._event_date = event_date
        self._results_path = results_path

        self._senders = list()
        self._folder_names = list()
        self._tasks = list()
        self._not_replied_file = "not_replied_{}.txt".format(event_date) \
            if event_date else ""

        self._prepare()
        self._make_dirs()

    def _prepare(self):
        if self._report_file is None:
            return

        with open(self._report_file, 'r', encoding='utf-8') as f:
            for line in f:
                folder, sender, task = line.split()
                self._senders.append(sender)
                self._folder_names.append('{:0>3}'.format(folder))
                self._tasks.append(task)

    def _make_dirs(self):
        if self._results_path is None:
            return

        for i, folder in enumerate(self._folder_names):
            path = op.join(self._results_path, folder)
            os.mkdir(path)
            os.mkdir(op.join(path, "results"))
            shutil.copy(self._tasks[i], path)

    def receive_all(self):
        imap = imaplib.IMAP4_SSL("imap.gmail.com", 993)
        imap.login(self._mail, self._password)
        imap.select('INBOX')
        with open(self._not_replied_file, 'w') as f:
            for i, sender in enumerate(self._senders):
                ind_results_path = op.join(
                    self._results_path, self._folder_names[i], "results")
                if not self._receive_mail(imap, sender, ind_results_path):
                    f.write('{} {}\n'.format(i + 1, sender))
        imap.logout()

    def get_senders(self, candidates):
        imap = imaplib.IMAP4_SSL("imap.gmail.com", 993)
        imap.login(self._mail, self._password)
        imap.select('INBOX')
        from_list = list()
        for sender in candidates:
            if self._receive_mail(imap, sender, None):
                from_list.append(sender)
        imap.logout()
        return from_list

    def _get_str_decoded(self, header):
        decoded = ""
        for b_str, encoding in decode_header(header):
            if not encoding:
                encoding = 'utf-8'
            decoded += b_str.decode(encoding) if isinstance(b_str, bytes) \
                else b_str
        return decoded

    def _receive_mail(self, imap, sender, ind_results_path):
        u_code_pattern = r'\\u[0-9A-Fa-f]{4}'
        status, response = imap.uid(
            'search', None,
            'FROM {0}'.format(sender),
            'ON {}'.format(self._event_date))
        if status != 'OK':
            return False

        unread_msg_nums = response[0].split()
        if not unread_msg_nums:
            return False

        if ind_results_path is None:
            return True

        print("processing", sender)
        with open(op.join(ind_results_path, '..', "texts.txt"), 'w',
                  encoding='utf-8') as f:
            f.write('From: {}\n'.format(sender))
            for e_id in unread_msg_nums:
                e_id = e_id.decode('utf-8')
                _, response = imap.uid('fetch', e_id, '(RFC822)')
                html = response[0][1].decode('utf-8')
                email_message = email.message_from_string(html)
                subject = email_message['Subject']
                try:
                    subject_str = self._get_str_decoded(subject)
                except TypeError:
                    subject_str = ""
                f.write('Subject: {}\n'.format(subject_str))
                charsets = email_message.get_charsets()
                for i, part in enumerate(email_message.walk()):
                    try:
                        content_type = part.get_content_type()
                        if content_type == 'text/plain' and \
                                not part.get('Content-Disposition'):
                            part_body = part.get_payload(decode=True)
                            part_str = part_body.decode(charsets[i])
                            if re.search(u_code_pattern, part_str):
                                part_str = part_body.decode('unicode-escape')
                            f.write('{}\n'.format(part_str))
                        elif part.get_content_maintype() == 'multipart':
                            continue

                        if part.get('Content-Disposition') is None:
                            continue

                        attachment = part.get_filename()
                        if not attachment:
                            continue

                        attachment_name = self._get_str_decoded(attachment)
                        path = op.join(ind_results_path, attachment_name)
                        with open(path, 'wb') as g:
                            g.write(part.get_payload(decode=True))
                    except Exception as e:
                        print("Exception while processing {}. Reason: {}".format(
                            sender, e))
        return True


if __name__ == '__main__':
    config = ConfigDict('config.txt')
    params = config.getconfig()
    files_path = params['files_path']

    event_date_time = datetime.strptime(
        params['practice_date_time'], "%d.%m.%Y %H:%M")
    event_date = event_date_time.strftime("%d-%b-%Y")
    report_file = event_date_time.strftime("%Y%m%d_%H%M") + '.txt'

    receiver = Receiver(
        params['your_mail'], params['your_password'],
        report_file, event_date,
        params['results_path'])
    receiver.receive_all()
    print("Mails were received")
