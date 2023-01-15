import random
from datetime import datetime
import time
import smtplib
from email import encoders
from email.mime.multipart import MIMEMultipart, MIMEBase
from email.mime.text import MIMEText

CHUNK_SIZE = 60     # mails count in chunk
PAUSE = 40          # seconds
TRIES = 3


class Sender:

    def __init__(self, mail, password, subject, common_text, recipients,
                 files, as_attachment, randomize=False):
        self._mail = mail
        self._password = password
        self._subject = subject
        self._common_text = common_text
        self._recipients = recipients
        self._files = files
        self._attach = as_attachment
        self._randomize = randomize

        self._texts = list()
        self._attachments = list()
        self._assignments = dict()
        self._unsent = list()

        self._prepare()
        self._assign()

    def _prepare(self):
        if self._attach:
            for path in self._files:
                with open(path, 'rb') as f:
                    self._attachments.append(f.read())
        else:
            for path in self._files:
                with open(path, 'r', encoding='utf-8') as f:
                    self._texts.append(self._common_text + f.read())

    def _assign(self):
        indeces = list(range(len(self._files)))
        for recipient in self._recipients:
            if self._randomize:
                i = random.randrange(len(indeces))
            else:
                i = 0
            index = indeces.pop(i)
            self._assignments[recipient] = index
            if not indeces:
                indeces = list(range(len(self._files)))

    def send_mail(self, recipient, mailServer):
        index = self._assignments[recipient]
        message = self._texts[index] if not self._attach \
            else self._common_text

        msg = MIMEMultipart()
        msg['From'] = self._mail
        msg['To'] = recipient
        msg['Subject'] = self._subject
        msg.attach(MIMEText(message, "plain"))
        if self._attach:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(self._attachments[index])

            # Encode file in ASCII characters to send by email
            encoders.encode_base64(part)

            # Add header as key/value pair to attachment part
            part.add_header(
                "Content-Disposition",
                "attachment; filename= {}".format(self._files[index]),
            )

            # Add attachment to message and convert message to string
            msg.attach(part)

        mailServer.sendmail(self._mail, recipient, msg.as_string())

    def send_chunk(self, to_send, report_name):
        gmailUser = self._mail
        gmailPassword = self._password

        mailServer = smtplib.SMTP('smtp.gmail.com', 587)
        mailServer.ehlo()
        mailServer.starttls()
        mailServer.ehlo()
        mailServer.login(gmailUser, gmailPassword)

        with open(report_name, 'a') as f:
            no = 0
            for i, recipient in to_send:
                try:
                    self.send_mail(recipient, mailServer)
                    index = self._assignments[recipient]
                    f.write("{} {} {}\n".format(i, recipient, self._files[index]))
                    print('Sending mail', i, recipient, self._files[index])
                    no += 1
                except smtplib.SMTPException as e:
                    self._unsent.extend(to_send[no:])
                    print(f"Error sending mail to {i} {recipient} ({e}). Closing chunk")
                    mailServer.close()
                    return

        mailServer.close()

    def send_chunks(self, to_send, report_name):
        chunks = len(to_send) // CHUNK_SIZE + 1
        for i in range(chunks):
            print('Sending chunk', i, 'from', chunks)
            self.send_chunk(to_send[i * CHUNK_SIZE: (i + 1) * CHUNK_SIZE], report_name)
            if i < chunks - 1:
                time.sleep(PAUSE)

    def send_all(self):
        self._unsent = list(zip(range(1, len(self._recipients) + 1), self._recipients))
        report_name = datetime.now().strftime("%Y%m%d_%H%M") + '.txt'
        for k in range(TRIES):
            to_send = self._unsent[:]
            print('Sending. Try', k + 1, 'to send:', len(to_send))
            self._unsent.clear()
            self.send_chunks(to_send, report_name)
            if not self._unsent:
                return

        for i, recipient in self._unsent:
            print(f"Not sent to: {i} {recipient}")
