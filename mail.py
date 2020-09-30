import smtplib, ssl
import pandas as pd
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
sendermail = "ipocheck123@gmail.com"
password = "1invoker1"
recievermail1 = "desai.achyutha2000@gmail.com"
recievermail2 = "desai.anirudhad@gmail.com"
subject = "TEST MAIL"

df = pd.read_csv("hehe.csv", parse_dates=["  Price Date  "]).drop(columns=["_merge"])
df.to_html('df_diff.html')
file = open('df_diff.html')
html = file.read()
message = MIMEMultipart('alternative')
message['Subject'] = subject
message['From'] = sendermail
message['To'] = recievermail1
text = "Hi there! This is a test mail to confirm the working of the ipo project."
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')
message.attach(part1)
message.attach(part2)
port = 465

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(sendermail, password)
    server.sendmail(sendermail, recievermail1, message.as_string())
    server.sendmail(sendermail, recievermail2, message.as_string())
    server.quit()
os.remove("hehe.csv")
os.remove("df_diff.html")