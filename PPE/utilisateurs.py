#!C:\Python27\python.exe

import cgitb
cgitb.enable()

import cgi
import MySQLdb
import query
import sha, time, Cookie, os

# Connexion a la base de donnees

db = query.MySQLConnect()
form = cgi.FieldStorage() 
action = form.getvalue('action')

def header() :

	# Debut de la page web

	print 'Content-Type: text/html\n'
	print '<head>\n'
	print '<meta charset="utf-8">\n'
	print '<title>Gestion des utilisateurs</title>\n'
	print '</head>\n'

	# Titre de la page

	print '<h1>Liste des utilisateurs</h1>\n'

def checkSessionCookie() :

	cookie = Cookie.SimpleCookie()
	string_cookie = os.environ.get('HTTP_COOKIE')

	if not string_cookie :

		print 'Location:login.py'

	else :

		return cookie

def afficheFormulaire(pCookie):

	if pCookie['admin'] :

		if action == 'mod':
			uid = form.getvalue('id')
			cursor = db.cursor()
			cursor.execute("select * from utilisateur where id = " + str(uid))
			row = cursor.fetchone()
			nom = row[1]
			prenom = row[2]
			email = row[3]
			password = ''
			nextAction = 'saveMod'

		else:
			nom = ''
			prenom = ''
			email = ''
			password = ''
			nextAction = 'add'

		htmlForm = '<form action="utilisateurs.py" method="post"><br />' \
		+ '<input type="text" name="nom" placeholder="Entrez un nom" value="' + str(nom) + '"/><br />' \
		+ '<input type="text" name="prenom" placeholder="Entrez un prenom" value="' + str(prenom) + '"/><br />' \
		+ '<input type="text" name="email" placeholder="Entrez un email" value="' + str(email) + '"/><br />' \
		+ '<input type="password" name="password" placeholder="Entrez un mot de passe" value="' + str(password) + '"/><br />' \
		+ '<input type="hidden" name="action" value="' + nextAction + '"/>'

		if nextAction == 'saveMod':
			htmlForm += '<input type="hidden" name="id" value="' + uid + '"/>' \
			+ '<input type="submit" value="Enregistrer la modification" />'

		else:
			htmlForm += '<input type="submit" value="Ajouter" />'

		print (htmlForm)

def deleteUtilisateur():

	if action == 'supp':
		uid = form.getvalue('id')
		sql = "DELETE FROM utilisateur WHERE not(admin) AND id = " + uid
		cursor = db.cursor()
		cursor.execute(sql)
		db.commit()

def insertUtilisateur():

	if action == 'add' or action == "saveMod":
		nom = form.getvalue('nom')
		prenom = form.getvalue('prenom')
		email = form.getvalue('email')
		password = form.getvalue('password')

		if (nom == None or prenom == None or email == None):
			return

		if action == 'add':
			sql = 'INSERT INTO utilisateur VALUES (' \
			+ '\'\', ' \
			+ '\'' + nom + '\', ' \
			+ '\'' + prenom + '\', ' \
			+ '\'' + email + '\', ' \
			+ '\'' + password + '\', ' \
			+ '0)'

		else:
			uid  = form.getvalue('id')
			sql = 'UPDATE utilisateur SET ' \
			+ 'nom = \'' + nom + '\', ' \
			+ 'prenom = \'' + prenom + '\', ' \
			+ 'email = \'' + email + '\', ' \
			+ 'password = \'' + str(password) + '\' ' \
			+ 'WHERE id = ' + str(uid)

		cursor = db.cursor()
		cursor.execute(sql)
		db.commit()

def printUtilisateur(row):

	print '<tr>'

	# Nom, prenom et email

	print '<td>' + str(row[1]) + '</td>' \
	+ '<td>' + str(row[2]) + '</td>' \
	+ '<td>' + str(row[3]) + '</td>' \

	# Admin ou non

	if row[5] == 1:
		print '<td>Oui</td>'

	else:
		print '<td>Non</td>'

	# Suppression si non-admin

	print '<td>'

	if row[5] != 1:
		print '<a href="utilisateurs.py?action=supp&id=' \
		+ str(row[0]) + '">Supprimer</a>'

	print '</td>'

	# Modification

	print '<td><a href ="utilisateurs.py?action=mod&id=' + str(row[0]) + '">Modifier</a></td>'

	print '</tr>'

def printUtilisateurs():
	
	cursor = db.cursor()
	cursor.execute("select * from utilisateur")
	print '<table border=1>'

	# Ligne des titres

	print '<tr>'

	print '<th>Nom</th>' \
	+ '<th>Prenom</th>' \
	+ '<th>Email</th>' \
	+ '<th>Admin</th>' \
	+ '<th>Suppression</th>' \
	+ '<th>Modification</th>' \

	print '</tr>'

	# Liste des utilisateurs

	for row in cursor.fetchall():
		printUtilisateur(row)

	print '</table>'

cookie = checkSessionCookie()
header()
afficheFormulaire(cookie)
insertUtilisateur()
deleteUtilisateur()
printUtilisateurs()

db.close()