from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACac2c95ddd04d6854427a06b20ec0ea37"
# Your Auth Token from twilio.com/console
auth_token  = "0f8e24c24b16710104d7969f6f46e650"

client = Client(account_sid, auth_token)


    if numofpeople >= 10:
    
    userinfo=open("userinfo.txt", "r")
    for x in userinfo:
        phonenumber=userinfo.split()[2]
        message = client.messages.create(
            to=phonenumber, 
            from_="",
            body="The place that you are trying to go now is dangerous! We recommend you to choose other places to go!")


print(message.sid)