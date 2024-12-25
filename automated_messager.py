"""
twilio  :
datetime module: future or current time
time module: use time sleep module

"""
     # STEPS#
# 1 twilio clinent setup
# 2 user inputs
# 3 scheduling logic
# 4 send message

from twilio.rest import Client    #this will used of send the whattsapp message
from datetime import datetime, timedelta           #timedelta used to check the differnce between present and which time to send
import time         #if we want to send this after 1 hour or after 2 hours  it will send


#step 2  twilio credentials both tacken from after login with twilio account
account_sid = "twilio acc_id"
auth_token = "twilio auth_no"

client=Client(account_sid,auth_token)

#step 3 design send messages functions
def send_whattsapp_message(recipient_number, message_body):
    try:
        message=client.messages.create(         #it's an twilio method
            from_='whatsapp:number fro twilio',
            body=message_body,
            to=f'whatsapp:{recipient_number}'
        )
        print(f'Message sent successfully! Message SID{message.sid}')

    except Exception as e:
        print("An error accoured....")



#users input

name = input("Enter the recipient name : ")
recipient_number = input("Enter the recipient whatsapp number with country code (like +91 ): ")
message_body =input(f"Enter the message you want to send to {name} : ")

#step 5 date/time and calculate delay

date_str = input("Enter the date to send the message (YYYY_MM_DD): ")
time_str = input("Enter the time to send the message (HH:MM in 24hour format): ")


#datetime
schedule_datetime = datetime.strptime(f'{date_str} {time_str}', "%Y-%m-%d %H:%M")        
current_datetime = datetime.now()


#calculate delay
time_difference = schedule_datetime - current_datetime
delay_seconds= time_difference.total_seconds()

if delay_seconds <= 0:
    print("The specified time is in the past. Pleace enter a future date and time: ")
else:
    print(f'Message scheduled to be sent to {name} at {schedule_datetime}')   

    #wait untill the shceduled time
    time.sleep(delay_seconds)

    #send the message
    send_whattsapp_message(recipient_number,message_body)