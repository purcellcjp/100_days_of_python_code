import smtplib
my_email = 'purcellqnapnas@gmail.com'
my_password = 'ttrj hcwm plts zrpq'

with smtplib.SMTP('smtp.gmail.com') as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email,
                        to_addrs='purcellcj@yahoo.com',
                        msg='Subject:Hello\n\nThis is the body of the email.')
