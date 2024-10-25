import json
import time
import random
from datetime import datetime, timedelta
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Step 1: Fetch the mock data
def fetch_mock_data():
    """Simulate fetching mock data from an API."""
    with open('mockLocationData.json', 'r') as f:
        return json.load(f)

# Step 2: Display the food truck locations
def display_food_truck_locations(data):
    """Display food truck locations from the mock data."""
    print("\n--- Current Food Truck Locations ---")
    for location in data['locations']:
        print(f"Area: {location['name']}")
        for post in location['posts']:
            print(f"  Food Truck: {post['food_truck']}")
            print(f"  Current Location: {post['street']}")
            print(f"  Last Updated: {post['timestamp']}")
            print()

# Step 3: Send email notification
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

# Step 4: Simulate real-time updates
def simulate_real_time_updates(data):
    while True:
        # Randomly update a food truck's location
        location = random.choice(data['locations'])
        post = random.choice(location['posts'])
        post['street'] = f"{random.randint(100, 999)} {random.choice(['Main', 'Broadway', 'Spring'])} St, Los Angeles, CA"
        post['timestamp'] = datetime.now().isoformat()

        # Display updated data
        display_food_truck_locations(data)

        # Send email with updated locations
        send_email(data)

        # Wait for a bit before the next update
        time.sleep(10)

# Main execution
data = fetch_mock_data()
simulate_real_time_updates(data)
