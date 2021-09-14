from twilio.rest import  Client
accound_sid = "AC75c8a114a077e29ffa28b8c1796be8b3"
auth_token = "200102726ea717d7e35454fcb74f9619"

client = Client(accound_sid,auth_token)

message = client.messages.create(
    to="+918448344321",
    from_="+14153603343",
    body = "hii"

print(message.sid)