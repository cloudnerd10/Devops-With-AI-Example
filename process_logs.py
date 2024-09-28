import sys
import smtplib
from email.mime.text import MIMEText

def analyze_logs(log_file):
    # Read the log file
    with open(log_file, 'r') as f:
        logs = f.read()

    # Process the logs (e.g., send to Gemini AI API)
    # For demonstration purposes, print the logs
    print("Analyzing logs...")
    print(logs)

    # You could also send the logs to an API:
    # response = requests.post('https://gemini-api-url/analyze', json={'logs': logs})
    # analysis = response.json()
    
    # For demonstration, we return a dummy analysis
    analysis = "Steps to resolve: Check configuration settings and retry."

    return analysis

def send_email(analysis):
    # Send an email with the analysis
    msg = MIMEText(analysis)
    msg['Subject'] = 'GitHub Actions Failure Analysis'
    msg['From'] = 'your-email@example.com'
    msg['To'] = 'your-email@example.com'

    try:
        # Setup your email server here (Gmail example)
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login("your-email@example.com", "your-password")
        server.send_message(msg)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    log_file = sys.argv[1]
    analysis = analyze_logs(log_file)
    send_email(analysis)
