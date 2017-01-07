import smtplib
import random
import collections
import env

def check_unique(array, ints):

    n = 0;
    for val in ints:
        
        if(n == val):
            return True
        n+=1    
     
    return False;
   

def smtp_init(server):

    
    #get all the server data that you need to use email client
    server.starttls()
    server.login(env.email_username, env.email_pass);



def main(): 
        
  
    #set up server 
    server = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_init(server)    



    
    nameDeque = [0,1,2,3,4,5]
  

    while( check_unique(env.names, nameDeque)):
        
        random.shuffle(nameDeque);
  
    n = 0;
    for val in nameDeque:
        
        tmpMessage = "Hey " + env.names[n] + " you have "  + env.names[val]+  ".Your limit is 20 dollars -Santa"
        server.sendmail(env.email_username, env.emails[n], tmpMessage);
        print env.names[n] + " message has been sent out"
        n += 1     
    server.quit()
     



if __name__=="__main__":
    main()




