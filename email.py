import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def create_email_content(data):
    """Create email content with food truck locations."""
    content = ""
    for location in data['locations']:
        content += f"Location: {location['name']}\n"
        for post in location['posts']:
            content += f"  Food Truck: {post['food_truck']}\n"
            content += f"  Street: {post['street']}\n\n"
    return content

def send_email(data):
    sender_email = "your-email@example.com"
    receiver_email = "manager-email@example.com"
    password = "your-password"

    # Create the email content
    email_content = create_email_content(data)

    # Set up the MIME
    message = MIMEMultipart("alternative")
    message["Subject"] = "LA Food Truck Locations"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create plain-text part of the message
    text_part = MIMEText(email_content, "plain")
    message.attach(text_part)

    # Send the email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

# Send email with food truck locations
send_email(data)
