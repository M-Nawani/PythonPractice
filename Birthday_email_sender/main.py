import random
import smtplib
import pandas as pd
import datetime as dt

PLACEHOLDER = '[NAME]'
sender_email = ""
receiver_email = ""
password = ""

data_frame = pd.read_csv("birthdays.csv")
birthday_list = data_frame.values.tolist()

now = dt.datetime.now()
current_day = now.day
current_month = now.month

birthday = []

for birthday in birthday_list:
    if current_month == birthday[3] and current_day == birthday[4]:
        name = birthday[0]
        file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
        with open(file_path, mode="r") as letter_data:
            letter_content = letter_data.read()
            new_data = letter_content.replace(PLACEHOLDER, name)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=sender_email, password=password)
            connection.sendmail(from_addr=sender_email,
                                to_addrs=receiver_email,
                                msg=f"Subject:Happy Birthday\n\n{new_data}")




