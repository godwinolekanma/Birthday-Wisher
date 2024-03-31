# Birthday Email Sender

This Python script sends birthday wishes via email to individuals listed in a CSV file. It checks the current date against the birthdays in the CSV file and sends personalized wishes to those celebrating their birthdays.

## Requirements

- Python 3.x
- pandas
- smtplib

## Setup

1. Clone the repository or download the starting file.
2. Ensure you have Python installed on your system.
3. Install required dependencies from requirements.txt or pip:
   
       pip install pandas
4. Set up a Gmail account to use as the sender's email address.
5. Enable less secure apps or create an app password for the Gmail account.
   
## Usage

1. Prepare your CSV file (`birthdays.csv`) containing the following columns:
- `name`: Recipient's name
- `email`: Recipient's email address
- `day`: Day of birth (integer)
- `month`: Month of birth (integer)

Example:

    name,email,day,month
    John Doe,johndoe@example.com,25,3
    Olivia Doe,Oliviadoe@example.com,1,8

2. Create letter templates in the `letter_templates` directory. These templates should be plain text files with placeholders for the recipient's name, e.g., `[NAME]`.

3. Update main.py `EMAIL` and `USER_PASSWORD` with your sender's email address and password (or use environment variables for security).

## Notes

- Make sure to keep your CSV file (`birthdays.csv`) and letter templates up to date.
- Handle sensitive information securely, especially email passwords.

