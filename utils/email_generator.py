import random
import string

def generate_emails(count=100):
    emails = []
    for _ in range(count):
        name = ''.join(random.choices(string.ascii_letters, k=8))
        domain = random.choice(['example.com', 'testmail.com', 'mail.net', 'mail.org'])
        email = f"{name}@{domain}"
        emails.append(email)
    return emails
  
