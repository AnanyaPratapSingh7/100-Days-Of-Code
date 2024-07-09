import smtplib
import datetime as dt
import random



#-----------------------------------EMAIL FUNCTIONALITY-------------------------------
def send_mail(message):
    sender_email = "[your mail]"
    receiver_email = "[receiver's mail]"

    passw = "[your password]"

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=sender_email, password=passw)
        connection.sendmail(from_addr=sender_email, to_addrs=receiver_email, msg=message)


#------------------------------------CHECK WEEKDAY-----------------------------------
current_day = dt.datetime.now().weekday()
#Check if day is Monday is=0
if current_day==1:
    #-------------------------GENERATE RANDOM QUOTE FROM LIST--------------------------
    with open(file="quotes.txt") as file:
        quotes = file.readlines()

    random_quote = random.choice(quotes)

    message = f"Subject:Monday Motivational Quote\n\n{random_quote}"

    send_mail(message)


