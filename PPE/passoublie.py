#!C:\Python27\python.exe

import cgitb
cgitb.enable()

import cgi
import MySQLdb

db = MySQLdb.connect("localhost", "root", "", "utilisateurs")
form = cgi.FieldStorage()
action = form.getvalue('action')
print "Content-Type: text/html\n"

def main():
    print"<!doctype html>"
    print"<html><head>"
    print"<meta http-equiv='Content-Type' content='text/html; charset=iso-8859-1' />"
    print"</head><body>"
    print "<FORM ACTION='passoublie.py' METHOD='get'>"
    print "<P>Email :</P>"
    print "<P><INPUT NAME='email' SIZE=20 MAXLENGTH=20 TYPE='text'></P>"
    print "<INPUT TYPE='submit' NAME='send' VALUE='Valider'>"
    print "</FORM></body></html>"

def recupermail():
    emailrecup = form.getvalue('email')

def recupidbdd():
    recupermail()
    sql="select id from utilisateur where not(admin) and email= "+ emailrecup
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()

main()
recupidbdd()

