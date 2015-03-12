#!C:\Python27\python.exe

import cgitb
cgitb.enable()

import cgi
import MySQLdb
import genererpass
import query

db = MySQLdb.connect("localhost", "root", "", "utilisateurs")
form = cgi.FieldStorage()
action = form.getvalue('action')
emailrecup = form.getvalue('email')

print "Content-Type: text/html\n"

def printHead():

    print"<!doctype html>"
    print"<html><head>"
    print"<meta http-equiv='Content-Type' content='text/html; charset=iso-8859-1' />"
    print"</head><body>"

def main():

    if action == 'valid' :
        IdRetour = query.recupId(emailrecup)
        if IdRetour != 0 :
           genererpass.sendnewpasswordemail(IdRetour)
        else :
            print "Adresse email inconnue"
    else :
        print "<FORM ACTION='passoublie.py' METHOD='get'>"
        print "<P>Email :</P>"
        print "<P><INPUT NAME='email' SIZE=20 MAXLENGTH=20 TYPE='text'></P>"
        print "<INPUT TYPE='submit' NAME='send' VALUE='Valider'>"
        print '<INPUT TYPE="hidden" VALUE="valid" NAME="action">'
        print "</FORM></body></html>"



printHead()
main()


