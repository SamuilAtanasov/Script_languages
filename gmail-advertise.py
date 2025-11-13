import smtplib
from email.message import EmailMessage

sender = "samuil.s.atanasov.2024@elsys-bg.org"
receiver_name = input ("Receiver name: ")
receiver_email = input("Receiver email: ")

subject = "Pancakes for you!"
body = f""""If happiness had a flavor – it would taste like a pancake!
With chocolate, fresh fruit, or the classic touch – pick your favorite and smile.
{receiver_name}, come on over – the pancakes won’t wait! """
print("Subject: Pancakes for you!")
print("From:", sender)
print("To: ", receiver_email)
print(body)

message = EmailMessage()
message['Subject'] = subject
message['From'] = sender

message['To'] = receiver_email
message.set_content(body)

try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender, "wago cqfw rxus kvfm")

        smtp.send_message(message)
    print("The email was sended successfully!")
except Exception as e:
    print("There was a mistake with sending:", e)