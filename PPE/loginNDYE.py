#!C:\Python27\python.exe

import cgitb
cgitb.enable()

import cgi
import MySQLdb


db = MySQLdb.connect("localhost", "root", "", "utilisateurs")
form = cgi.FieldStorage()
action = form.getvalue('action')
print "Content-Type: text/html\n"

def login():
	print "<H3>Connection</H3>"
	print "<FORM ACTION='testPassword.py' METHOD='post'>"
	print "<P>Login :</P>"
	print "<P><INPUT NAME='Login' SIZE=20 MAXLENGTH=20 TYPE='text'></P>"
	print "<P>Mot de passe :</P>"
	print "<P><INPUT NAME='password' SIZE=20 MAXLENGTH=20 TYPE='password'></P>"
	print "<INPUT TYPE='submit' NAME='send' VALUE='Connexion'>"
	print "</FORM>"

def passOublie():
    print "<a href='passoublie.py'>Mot de passe oublie</a>"

login()
passOublie()
