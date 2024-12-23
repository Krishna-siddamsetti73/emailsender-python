import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd

# Load email data from Excel
data = pd.read_excel("Flutter_experience_20241223_RG.xlsx")  # Make sure to provide the correct path
recipient_email = data["Email"].tolist()  # Assuming "Email" is a column in your Excel sheet

# Set up the SMTP server
smtp_server = "smtp.gmail.com"
smtp_port = 587
sender_email = "shivrikshna73@gmail.com"
sender_password = "jszs maxq okaw ekxc"

# Create the email message
subject = "meeting for flutter development team"
body = """hey! everyone this is krishna siddamsetti flutter developer  at blueplanet solution 
there are so many projects are there for the flutter development i would like to form a team and introduce so i request you all to join the meeting
at 2.30 pm EST (12.00 AM IST ) i request you evryone to join the meeting for the formation of flutter development team"""

# Send the email to each recipient
for recipient in recipient_email:
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = recipient
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    # Connect to the server and send the email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient, msg.as_string())

print("Emails sent successfully!")