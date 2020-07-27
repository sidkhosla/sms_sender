# Must install twilio using pip
from twilio.rest import Client 
 
account_sid = 'Get using Twilio website'
auth_token = 'Get using Twilio website' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                            #   from_='number given by twilio',  
                              body='hi',      
                            #   to='verfied number' 
                          ) 
 
print(message.sid)