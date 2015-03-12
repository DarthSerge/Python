#!C:\Python27\python.exe
import smtplib
from email.mime.text import MIMEText
from smtplib import SMTPException

EMAIL_SUBJECT = "Mot de passe oublie"
EMAIL_FROM = "ndeye@lenouveauparisdakar.fr"
EMAIL_RECEIVERS = ['capitolin.terry@live.fr']

def listToStr(lst):

    """This method makes comma separated list item string"""
    return ','.join(lst)

def send_email(msg):
  
    """This method sends an email"""
    msg_header = "From: " + EMAIL_FROM + "\n" + \
                 "To: " + listToStr(EMAIL_RECEIVERS) + "\n" + \
                 "Subject: " + EMAIL_SUBJECT + "\n"
    msg_body =  msg_header + msg
    try:
      #establish a connection with the local SMTP server.
      smtpObj = smtplib.SMTP('smtp.lenouveauparisdakar.fr:587')
      #Now send the email
      smtpObj.sendmail(EMAIL_FROM, EMAIL_RECEIVERS, msg_body)
      #Close the connection and session.
      smtpObj.quit()
    except SMTPException as error:
      print "Error: unable to send email :  {err}".format(err=error)

