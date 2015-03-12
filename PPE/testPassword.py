

import hashlib
from getpass import getpass
from random import choice

import cgitb
cgitb.enable()

import cgi
import MySQLdb


db = MySQLdb.connect("localhost", "root", "", "utilisateurs")
form = cgi.FieldStorage()
action = form.getvalue('action')
print "Content-Type: text/html\n"


def connexion():
    email=form.getvalue('login')
    password=form.getvalue('password')
    # Hachage du mot de passe
    password_chiffre=hashlib.sha1(password).hexdigest()


def recuppassbdd():
    connexion()
    sql = "select * FROM utilisateur WHERE email="+ email + "and password =" + password_chiffre
    cursor = db.cursor()
    cursor.execute(sql)


connexion()
recuppassbdd()
