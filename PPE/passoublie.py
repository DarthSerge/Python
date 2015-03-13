#!C:\Python27\python.exe

import cgitb
cgitb.enable()

import cgi
import MySQLdb
import genererpass
import query

form = cgi.FieldStorage()
action = form.getvalue('action')
emailrecup = form.getvalue('email')

def entete() :

	# Debut de la page web

	print 'Content-Type: text/html\n'
	print '<head>\n'
	print '<meta charset="utf-8">\n'
	print '<link rel="stylesheet" type="text/css" href="template.css">\n'
	print '<title>Gestion des utilisateurs</title>\n'
	print '</head>\n'

def form():

	if action == 'valid' :

		IdRetour = query.recupId(emailrecup)

		if IdRetour != 0 :

			genererpass.sendnewpasswordemail(IdRetour)

		else :

			print 'Adresse email inconnue'

	else :

		htmlForm = '<div id="bloc"><form action="login.py" method="post">' \
		+ '<h1>Gestion des utilisateurs</h1>' \
		+ '<p>Mot de passe oublie</p>' \
		+ '<div><label>Addresse email :<span>saisir une addresse valide</span></label><input type="text" name="email"/></div>' \
		+ '<input type="hidden" name="action" value="valid"/>' \
		+ '<input type="submit" value="Valider" id="boutonConnexion"/>' \
		+ '</form>'

		print htmlForm

		print '</div>'

entete()
form()


