import imaplib
import email
import os
from dotenv import load_dotenv
load_dotenv()

username = os.getenv('EMAIL')
password = os.getenv('PASSWORD')

# Connect to the email server
def connect_to_email():
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login(username, password)
    mail.select('inbox')
    return mail

# Search emails
def search_emails():
    mail = connect_to_email()
    _, search_data = mail.search(None, '(BODY "unsubscribe")')
    data = search_data[0].split()

    for num in data:
        _, data = mail.fetch(num, '(RFC822)')
        msg = email.message_from_bytes(data[0][1])
        print(msg['subject'])

        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/html":
                    html_content = part.get_payload(decode=True).decode('utf-8')
                    print(html_content)
        else:
            content_type = msg.get_content_type()
            content = msg.get_payload(decode=True).decode()

            if content_type == "text/html":
                print(content)

    mail.logout()


search_emails()
