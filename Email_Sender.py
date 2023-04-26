import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Email, To, Content


os.environ['SENDGRID_API_KEY'] = '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'

from_email = Email("myemail@gmail.com")
to_email = To("person1@gmail.com", "person1@gmail.com")
subject = "Sending email with SendGrid and Python"
content = Content("text/plain", """Hi everyone, I am sending this very important 
email to your from sendgrid but it is just a test to be honest. Ok bye.""")

message = Mail(
    from_email=from_email,
    to_emails=to_email,
    subject=subject,
    plain_text_content=content
)

try:
    sg = SendGridAPIClient()
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)
