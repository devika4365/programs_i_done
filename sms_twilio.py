from twilio.rest import Client 
 
account_sid = 'AC5c236fc2813c036d42d0ed6b8b7a5b5e' 
auth_token = '[AuthToken]' 
client = Client(account_sid, auth_token) 
content=input("Enter text to send") 
message = client.messages.create( 
                              from_='+12059227520',  
                              body=content,      
                              to='+917382434834' 
                          ) 
 
print(message.sid)
