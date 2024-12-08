import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Gmail SMTP configuration
GMAIL_SMTP_SERVER = "smtp.gmail.com"
GMAIL_SMTP_PORT = 587

# Update these details with your Gmail credentials
app_email_address = "vikhilkhobragade@gmail.com"
password = "nfgu lesl miey udou"  # App Password if 2FA is enabled

def send_email(subject, body, recipient, cc_recipient=None):
    # Set up the MIME structure
    msg = MIMEMultipart()
    msg['From'] = app_email_address
    msg['To'] = recipient
    msg['Subject'] = subject
    if cc_recipient:
        msg['Cc'] = cc_recipient

    # Attach the email body
    msg.attach(MIMEText(body, 'plain'))

    # Recipients list
    recipients = [recipient]
    if cc_recipient:
        recipients.append(cc_recipient)

    # Set up the server and send the email
    try:
        server = smtplib.SMTP(GMAIL_SMTP_SERVER, GMAIL_SMTP_PORT)
        server.starttls()  # Start TLS for security
        server.login(app_email_address, password)  # Login to Gmail
        server.sendmail(app_email_address, recipients, msg.as_string())  # Send email
        server.quit()
        print("Email sent successfully.")
    except Exception as e:
        print(f"Error sending email: {e}")

# Usage
send_email(
    subject="Test Email",
    body="This is a test email sent from a Gmail account.",
    recipient="vikhilkhobragade@gmail.com",
    cc_recipient="vikhilkhobragade@gmail.com"
)