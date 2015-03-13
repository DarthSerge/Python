#!C:\Python27\python.exe

from sendmail import send_email
from getpass import getpass
from random import choice
import query

def genererpass() :

	letter1 = ['a','b','c','d']
	letter2 = ['A','B','C','D']
	symbol1 = ['_','/','%','!','$']
	number1 = ['1','2','3','4','5','6']

	# Genere un mot de passe aleatoire

	return choice(letter1) + choice(number1) + choice(letter2) + choice(symbol1) + choice(letter1) + choice(number1)

def sendnewpasswordemail(pId) :

	NewPass = genererpass()
	send_email("Votre nouveau mot de passe : " + str(NewPass))
	query.updatePassword(NewPass,pId)

def insertbdd() :

	sql = 'INSERT INTO utilisateur VALUES (' \
	+ '\'\',' \
	+ '\'' + nom + '\',' \
	+ '\'' + prenom + '\',' \
	+ '\'' + email + '\',' \
	+ 'MD5(\'' + password + '\'),' \
	+ '0)'

	cursor = db.cursor()
	cursor.execute(sql)
	db.commit()