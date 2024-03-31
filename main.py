import pandas
import os
import datetime as dt
import random
import smtplibt

now = dt.datetime.now()  # Get current date and time
EMAIL = os.environ.get("EMAIL")  # Sender's email address
USER_PASSWORD = os.environ.get("USER_PASSWORD")  # Get user password from environment variables


def send_email(recipient_email, wish):
    """
    Function to send birthday wishes via email.

    Args:
        recipient_email (str): Recipient's email address.
        wish (str): Birthday wish message.
    """
    # Establish connection to SMTP server
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()  # Start TLS encryption
        connection.login(user=EMAIL, password=USER_PASSWORD)  # Login to sender's email account
        # Send email
        connection.sendmail(from_addr=EMAIL,
                            to_addrs=recipient_email,
                            msg=f"Subject:Happy Birthday\n\n{wish}")


# Read data from CSV file into pandas DataFrame
data = pandas.read_csv("birthdays.csv")
# Convert DataFrame to dictionary
data_dict = data.to_dict(orient="records")

# Iterate over each birthday record
for birth in data_dict:
    # Check if current date matches the birthday
    if now.day == birth["day"] and now.month == birth["month"]:
        # Select a random letter template and read its content
        with open(f"./letter_templates/letter_{random.randint(1, 3)}.txt") as file:
            birthday_wish = file.read()  # Read content of the letter template
            birthday_wish = birthday_wish.replace("[NAME]", birth["name"])  # Replace placeholder with recipient's name
            email = birth["email"]  # Recipient's email address
            send_email(email, birthday_wish)  # Send birthday wish email
