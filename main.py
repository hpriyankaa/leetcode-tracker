import pandas as pd
import smtplib
from datetime import datetime
import schedule

df = pd.read_excel('habit-tracker.xlsx')


df['Datetime'] = pd.to_datetime(df['Datetime'])

l_row = df.iloc[-1]
l_time = l_row['Datetime']


curr_time = datetime.now()


diff = l_time-curr_time



def send_email(message, receiver_email):
    my_email = 'hpriyanka2024@gmail.com'
    passwd = 'yobm fxlw cytu guqh'


    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(my_email, passwd)


    server.sendmail(my_email, receiver_email, message)
if diff.days >1:
    print("sending email..")
    send_email("This is to remind you that you haven't solved the leetcode of the day, please solve it!","shyamkarthick20@gmail.com")
    print("Sent email")






