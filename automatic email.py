import smtplib 
import email.message #library

def send_email(): #define function
    email_body = """
    <p> Hello, this is a test email </p>
    <p> Take care and wash your hands </p> """

    msg = email.message.EmailMessage()
    msg['Subject'] = 'Test Email'
    msg['From'] = '#use your own email'
    msg['To'] = '#enter destination email'
    password = '#enter your password' #be careful, because your password will be exposed
    msg.add_header('Content-Type', 'text/html')#add header to make sure the email is in html format
    msg.set_payload(email_body)#set the email body

    s = smtplib.SMTP('smtp.gmail.com', 587)#connect to the server
    s.starttls()#start the encryption
    s.login(msg['From'], password)#login with your email and password
    s.sendmail(msg['From'], msg['To'], msg.as_string())#send the email to the destination email 
    print('Email sent')
    s.quit()#close the connection
