import smtplib
import datetime as dt
import random

my_email = 'purcellqnapnas@gmail.com'
my_password = 'ttrj hcwm plts zrpq'

# load quotes
with open('quotes.txt', 'r') as file:
    lines = file.readlines()

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 0:    # Monday

    quote = random.choice(lines)
    print(quote)

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs='purcellcj@yahoo.com',
                            msg=f'Subject:Quote of the Day\n\n{quote}')
