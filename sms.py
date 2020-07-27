# Must install twilio using pip
from twilio.rest import Client 
 
account_sid = 'AC84246579081b286453be3511e6016f25' 
auth_token = '430803ce6bd1ddfec945a571d992d605' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='+447401227823',  
                              body='hi',      
                              to='+447497087646' 
                          ) 
 
print(message.sid)