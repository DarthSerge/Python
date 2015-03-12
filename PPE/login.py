#!C:\Python27\python.exe

import cgitb
cgitb.enable()

import cgi
import MySQLdb
import query

form = cgi.FieldStorage() 
action = form.getvalue('action')

def printHead():

    print "Content-Type: text/html\n"
    print "<head>"
    print '<meta charset="UTF-8">'
    print "</head>"
    print ("<H1>Connexion</H1>")

def printForm():

	if action == 'connect' :

		login = query.checkInjection(form.getvalue('login'))
		mdp = query.checkInjection(form.getvalue('mdp'))

		if query.queryConnection(login,mdp) : 
			print "Connection" #Mettre ici l'accès à la page utilisateur.py avec la gestion des SESSION
		else :
			print "Try harder"    
	else :
		print "<h2>"
		print '<FONT COLOR="Royal blue">'
		print "</FONT>"
		print "</h2>"
		print ""
		print '<FORM ACTION="login.py" METHOD="post">'
		print "<P>Login :</P>"
		print '<P><INPUT NAME="login" SIZE=20 MAXLENGTH=20 TYPE="text"></P>'
		print '<P>Mot de passe :</P>'
		print '<P><INPUT NAME="mdp" SIZE=20 MAXLENGTH=20 TYPE="password"></P>'
		print ""
		print '<INPUT TYPE="hidden" VALUE="connect" NAME="action">'
		print '<INPUT TYPE="submit" VALUE="Se connecter">'
		print "</FORM>"

printHead()
printForm()
