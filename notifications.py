import smtplib


def send_email(subject, message, to_email, user_email, user_password, email_provider="smtp.gmail.com"):
    """email_provider: Gmail (smtp.gmail.com), Yahoo (smtp.mail.yahoo.com), 
    Hotmail (smtp.live.com), Outlook (smtp-mail.outlook.com)"""
    with smtplib.SMTP(email_provider) as connection:  # gmail smtp server
        connection.starttls()  # for encryption
        try:
            connection.login(user=user_email, password=user_password)
            connection.sendmail(from_addr=user_email,
                                to_addrs=to_email,
                                msg=f"Subject:{subject}\n\n{message}".encode('utf-8'))
            print(f"Message Sent to {to_email}!")
        except Exception:
            print("Error! Message not sent")
