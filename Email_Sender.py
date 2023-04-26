import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Email, To, Content


os.environ['SENDGRID_API_KEY'] = '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'

from_email = Email("ziamalhi1234@gmail.com")
to_email = To("ziamalhi786@gmail.com")
subject = "Sending email with SendGrid and Python"
content = Content("text/plain", "Hello, this is a test email sent from Python using the SendGrid API.")

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
