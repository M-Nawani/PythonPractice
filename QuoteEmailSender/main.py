import smtplib
import random
import datetime as dt

EMAIL_SENDER = "testemailed007@gmail.com"
EMAIL_RECEIVER = "testemail0121@yahoo.com"
PASSWORD = "Country@123"

now = dt.datetime.now()
current_day = now.weekday()

with open("quotes.txt") as file:
    all_quotes = file.readlines()
    quote_of_the_week = random.choice(all_quotes)

if current_day == 2:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL_SENDER, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL_SENDER,
                            to_addrs=EMAIL_RECEIVER,
                            msg=f"Subject:Positive quote of the week\n\n{quote_of_the_week}")

