import os
import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from langchain_google_genai import GoogleGenerativeAI

def analyze_logs(log_file):
    with open(log_file, 'r') as f:
        logs = f.read()
        # Analyze the logs here
        print("Log Analysis: ")
        print(logs)
        llm = GoogleGenerativeAI(model="gemini-pro")
        return llm.invoke(logs)

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

if __name__ == "__main__":
    log_file = sys.argv[1]
    body = analyze_logs(log_file)
    sender_email = "gcpofakhil@gmail.com"
    sender_password = "mwlwxqkonowiturr"  # This needs to be an App Password, not your regular password
    recipient_email = "akhilreddy.ankireddy10@gmail.com"
    subject = "Test Email"
    send_email(sender_email, sender_password, recipient_email, subject, body)
