from twilio.rest import  Client
accound_sid = "AC75c8a114a077e29ffa28b8c1796be8b3" 
auth_token = "200102726ea717d7e35454fcb74f9619"  #different for different number

client = Client(accound_sid,auth_token)

message = client.messages.create(
    to="your registered number",
    from_="+14153603343", #twilio number
    body = "hii"

print(message.sid)
