import imaplib
import email
import os
from dotenv import load_dotenv
from extract_links import extract_links_from_html
from click_links import click_links
from save_links import save_links
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

    links = []

    for num in data:
        _, data = mail.fetch(num, '(RFC822)')
        msg = email.message_from_bytes(data[0][1])

        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/html":
                    html_content = part.get_payload(decode=True).decode('utf-8')
                    links.extend(extract_links_from_html(html_content))
        else:
            content_type = msg.get_content_type()
            content = msg.get_payload(decode=True).decode()

            if content_type == "text/html":
                links.extend(extract_links_from_html(content))

    mail.logout()
    return links


links = search_emails()
# Click on the links
for link in links:
    click_links(link)

# Save the links to a file
save_links(links)
