from twilio.rest import Client
import keys
# Your Twilio Account SID and Auth Token


# Create a Twilio client
client = Client(keys.account_sid, keys.auth_token)

# Send a message
message = client.messages.create(
    body="Ishaque wants to play chess ",
    from_=keys.twilio_number,
    to=keys.my_phone_number
)

print(f"Message : {message.body}")
