#!C:\Python27\python.exe

import cgitb
cgitb.enable()

import cgi
import MySQLdb
import query
import sha, time, Cookie, os

# Connexion a la base de donnees

form = cgi.FieldStorage() 
action = form.getvalue('action')

def start() :

	if action == 'connect' :

		login = query.checkInjection(form.getvalue('login'))
		mdp = query.checkInjection(form.getvalue('mdp'))

		if query.connection(login,mdp) :

			sessionCookie()
			print 'Location:utilisateurs.py'

		else :

			header()
			print '<div>Login et/ou mot de passe incorrect !</div>'

	else :

		header()

def header() :

	# Debut de la page web

	print 'Content-Type: text/html\n'
	print '<head>\n'
	print '<meta charset="utf-8">\n'
	print '<title>Gestion des utilisateurs</title>\n'
	print '</head>\n'

	# Titre de la page

	print '<h1>Connexion</h1>\n'

	forms()

def sessionCookie() :

	cookie = Cookie.SimpleCookie()
	string_cookie = os.environ.get('HTTP_COOKIE')

	# Nouvelle session

	if not string_cookie :

		sid = sha.new(repr(time.time())).hexdigest()
		admin = query.checkAdmin(form.getvalue('login'))

		cookie['sid'] = sid
		#cookie['admin'] = admin

		# Date d'expiration (en secondes)

		cookie['sid']['expires'] = 60 * 60

	# Session deja existante

	else:

		cookie.load(string_cookie)
		sid = cookie['sid'].value
		#admin = cookie['admin'].value

	print cookie

def forms() :

	htmlFormConnect = '<form action="login.py" method="post"><br />' \
	+ '<input type="text" name="login" placeholder="Entrez votre login"/><br />' \
	+ '<input type="password" name="mdp" placeholder="Entrez votre mot de passe"/><br />' \
	+ '<input type="hidden" name="action" value="connect"/>' \
	+ '<input type="submit" value="Se connecter" />'

	htmlFormPassOublie = '<form action="passoublie.py" method="post"><br />' \
	+ '<input type="submit" value="Mot de passe oublie" />'

	print (htmlFormConnect)
	print (htmlFormPassOublie)

start()