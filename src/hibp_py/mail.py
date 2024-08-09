import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr
from hibp_py.utils import load_config


config = load_config()


SERVER = config['SMTP_SERVER']
PORT = config['SMTP_PORT']
FROM_NAME = config['FROM_NAME']
FROM_EMAIL = config['FROM_EMAIL']
SUBJECT = config['SUBJECT']


def send_email(email, body):
    """Send an email

    Args:
        email (str): The recipient's email address
        body (str): The email body
    """
    if 'TEST_RECIPIENT' in config.keys():
        email = config['TEST_RECIPIENT']

    message = MIMEMultipart('alternative')
    message['Subject'] = SUBJECT
    message['From'] = formataddr((FROM_NAME, FROM_EMAIL))
    message['To'] = email

    message.attach(MIMEText(body, 'html'))

    server = smtplib.SMTP()
    server.connect(SERVER, PORT)
    server.sendmail(FROM_EMAIL, email, message.as_string())
    server.quit()


def create_body(email, breachNames):
    """Creates the email body

    Args:
        email (str): The recipient's email address
        breachNames (list): A list of breach names

    Returns:
        str: The email body
    """
    with open('input/email.html', 'r') as file:
        body = file.read()

    breaches_list = ''
    breached_data = ''
    data_classes = []

    breaches = {}

    with open(f'data/breaches.json', 'r') as file:
        data = json.load(file)

        for breachName in breachNames:
            breaches[breachName] = data[breachName]

    for breachName in breaches:
        if breaches[breachName]:
            breach = breaches[breachName]

            if breach['Domain']:
                breaches_list += f'<li><a href="https://{breach["Domain"]}"' + \
                    f'>{breach["Title"]}</a></li>'
            else:
                breaches_list += f'<li>{breach["Title"]}</li>'

            if breach["DataClasses"]:
                for data_class in breach["DataClasses"]:
                    if data_class not in data_classes:
                        data_classes.append(data_class)
                        breached_data += f'<li>{data_class}</li>'

    body = body.replace('{email}', email)
    body = body.replace('{breaches}', breaches_list)
    body = body.replace('{breached_data}', breached_data)

    return body
