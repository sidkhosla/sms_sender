# Must install twilio using pip
from twilio.rest import Client 
 
account_sid = 'Get using Twilio website'
auth_token = 'Get using Twilio website' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='+447401227823',  
                              body='hi',      
                              to='+447497087646' 
                          ) 
 
print(message.sid)