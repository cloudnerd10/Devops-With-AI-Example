import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, recipient_email, subject, body):
    try:
        # Create message container
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject

        # Add body to email
        message.attach(MIMEText(body, 'plain'))

        # Create SMTP session
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        
        # Login to the server
        server.login(sender_email, sender_password)
        
        # Send email
        text = message.as_string()
        server.sendmail(sender_email, recipient_email, text)
        
        print("Email sent successfully!")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        
    finally:
        server.quit()

# Example usage
if __name__ == "__main__":
    sender_email = ""
    sender_password = "your_app_password"  # This needs to be an App Password, not your regular password
    recipient_email = "recipient@example.com"
    subject = "Test Email"
    body = "This is a test email sent from Python!"
    
    send_email(sender_email, sender_password, recipient_email, subject, body)
