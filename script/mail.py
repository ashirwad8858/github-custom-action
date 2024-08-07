import smtplib
from email.message import EmailMessage
import argparse

def send_email(smtp_server, smtp_port, username, password, from_email, to_email):
    subject = 'Test Email'
    body = 'This is a test email sent from GitHub'

    msg = EmailMessage()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.set_content(body)

    # Send the email
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(username, password)
            server.send_message(msg)
            print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

def main():
    parser = argparse.ArgumentParser(description='Send an email using SMTP.')
    parser.add_argument('--smtp_server', type=str, required=True, help='SMTP server address')
    parser.add_argument('--smtp_port', type=int, required=True, help='SMTP server port')
    parser.add_argument('--username', type=str, required=True, help='SMTP server username')
    parser.add_argument('--password', type=str, required=True, help='SMTP server password')
    parser.add_argument('--from_email', type=str, required=True, help='Email address of the sender')
    parser.add_argument('--to_email', type=str, required=True, help='Email address of the recipient')

    args = parser.parse_args()

    send_email(args.smtp_server, args.smtp_port, args.username, args.password, args.from_email, args.to_email)

if __name__ == "__main__":
    main()
