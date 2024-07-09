import smtplib
import datetime as dt
import random
import pandas as pd

##################### Extra Hard Starting Project ######################
def send_wish(name, email):
    letter_num = random.randint(1,3)
    with open(f"letter_templates/letter_{letter_num}.txt") as file:
        letter_template = file.read()
        letter_final = letter_template.replace("[NAME]", name)


        sender_email = "[your mail]"
        receiver_email = email

        passw = "{your password}"

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=sender_email, password=passw)
            connection.sendmail(from_addr=sender_email, to_addrs=email, msg=f"Subject:Happy Birthday To You!!\n\n{letter_final}")

    print(letter_template)
# 2. Check if today matches a birthday in the birthdays.csv
today = dt.datetime.now()
current_month = today.month
current_day = today.day

dataframe = pd.read_csv("birthdays.csv")

data_as_dict = dataframe.to_dict(orient="records")

for person in data_as_dict:
    if person["month"] == current_month and person["day"] == current_day:
        send_wish(person["name"], person["email"])

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




