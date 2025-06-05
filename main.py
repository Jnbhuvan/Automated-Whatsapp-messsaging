# Step 1: Import necessary libraries 
from twilio.rest import Client
from datetime import datetime, timedelta
import time

# Step 2: twilio credentials
account_sid = "your_account_sid_here"
auth_token = "your_auth_token_here"
# Note: Replace 'your_account_sid_here' and 'your_auth_token_here' with your actual Twilio credentials.

# import os

# account_sid = os.getenv("TWILIO_ACCOUNT_SID")
# auth_token = os.getenv("TWILIO_AUTH_TOKEN")
# client = Client(account_sid, auth_token)

# client = Client(account_sid, auth_token)

# Step 3: Define the function to send SMS
def send_whatsapp_msg(recipent_no,message):
    try:
        message = client.messages.create(
            from_= 'whatsapp:+14155238886',
            body = message,
            to = f'whatsapp:{recipent_no}'
        )
        print(f'Message sent successfully to {recipent_no}')
    except Exception as e:
        print(f'Failed to send message to {recipent_no}: {e}')
        
#step 4 : user input

name = input('Enter the recipient name: ')

recipent_no = input('Enter the recipient number with country code: ')
message = input(f'Enter the message: {name} ')

#step 5: parse date/time and calculate delay
#date_str = '2025-04-27'
date_str = input('Enter the date and time to send the message (YYYY-MM-DD HH:MM): ')
time_str = input('Enter the time to send the message (HH:MM in 24hour format): ')

#date_time
schedule_datetime = datetime.strptime(f'{date_str} {time_str}',"%Y-%m-%d %H:%M")
current_datetime = datetime.now()

#calculate delay
time_diff = schedule_datetime - current_datetime
delay_seconds = time_diff.total_seconds()

if delay_seconds < 0:
    print("The scheduled time is in the past. Please enter a future time.")
else:
    print(f"Message will be sent in {delay_seconds} seconds to {name}.")        
    #wait for the delay
    time.sleep(delay_seconds)

#send the message
    send_whatsapp_msg(recipent_no,message)
    print(f"Message sent to {name} at {schedule_datetime.strftime('%Y-%m-%d %H:%M')}")
    print("Message sent successfully!")


#2025-04-27 12:4 