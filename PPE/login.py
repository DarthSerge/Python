#!C:\Python27\python.exe

import cgitb
cgitb.enable()

import cgi
import MySQLdb
import query
import sha, time, Cookie, os
import urllib2

# Initialisation

form = cgi.FieldStorage() 
action = form.getvalue('action')

def start() :

	if action == 'connect' :

		login = query.checkInjection(form.getvalue('login'))
		mdp = query.checkInjection(form.getvalue('mdp'))

		user = query.connection(login,mdp)

		if user != -1:

			sessionCookie(user)
			print "Location: utilisateurs.py\r\n"

		else :

			entete()
			print '<div id="errorLog">Login et/ou mot de passe incorrect !</div>'

	else :

		entete()

def entete() :

	# Debut de la page web

	print 'Content-Type: text/html\n'
	print '<head>\n'
	print '<meta charset="utf-8">\n'
	print '<link rel="stylesheet" type="text/css" href="template.css">\n'
	print '<title>Gestion des utilisateurs</title>\n'
	print '</head>\n'

	forms()

def sessionCookie(pUser) :

	cookie = Cookie.SimpleCookie()
	string_cookie = os.environ.get('HTTP_COOKIE')

	# Nouvelle session

	if not string_cookie :

		sid = sha.new(repr(time.time())).hexdigest()

		cookie['sid'] = sid
		cookie['admin'] = pUser

		# Date d'expiration (en secondes)

		cookie['sid']['expires'] = 60 * 60
		cookie['admin']['expires'] = 60 * 60

	# Session deja existante

	else:

		cookie.load(string_cookie)
		sid = cookie['sid'].value
		admin = cookie['admin'].value

def forms() :

	htmlFormConnect = '<div id="bloc"><form action="login.py" method="post">' \
	+ '<h1>Gestion des utilisateurs</h1>' \
	+ '<p>Connexion</p>' \
	+ '<div><label>Addresse email :<span>saisir une addresse valide</span></label><input type="text" name="login"/></div>' \
	+ '<div><label>Mot de passe :</label><input type="password" name="mdp"/></div>' \
	+ '<input type="hidden" name="action" value="connect"/>' \
	+ '<input type="submit" value="Se connecter" id="boutonConnexion"/>' \
	+ '</form>'

	htmlFormPassOublie = '<form action="passoublie.py" method="post"><br />' \
	+ '<p>Mot de passe oublie</p>' \
	+ '<input type="submit" value="En demander un nouveau" id="boutonPassoublie"/>' \
	+ '</form>'

	print htmlFormConnect
	print htmlFormPassOublie

	print '</div>'

start()