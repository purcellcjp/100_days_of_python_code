import smtplib
import datetime as dt
import random
import pandas as pd
import os

##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

my_email = 'purcellqnapnas@gmail.com'
my_password = 'ttrj hcwm plts zrpq'

now = dt.datetime.now()
month = now.month
day_of_week = now.weekday()
day_num = now.day
# print(month, day_num)

df = pd.read_csv('birthdays.csv')
# print(df.dtypes)

cur_bdays_df = df[(df.month == month) & (df.day == day_num)]
print(cur_bdays_df)

# lookup template file names
template_names = os.listdir('letter_templates')
# print(files)
# Choose one file to use as template
template_name = random.choice(template_names)
# load template file
with open(f'letter_templates/{template_name}') as file:
    template = file.read()
# print(template)

for index, row in cur_bdays_df.iterrows():
    name = row['name']
    email = row.email
    new_msg = template
    new_msg = new_msg.replace('[NAME]', str(name))
    print('name:', name, 'email:', email, sep='|')

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=email,
                            msg=f'Subject:Happy Birthday!!!\n\n{new_msg}')
