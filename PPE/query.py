#!C:\Python27\python.exe

import cgitb
cgitb.enable()

import cgi
import MySQLdb

#Ouvre la connection à la base de données
def MySQLConnect() :

	return MySQLdb.connect("localhost", "root", "", "utilisateurs")

def checkInjection(pString) :
	temp = ""
	for char in pString :
		if char == "'" :
			temp += "\\" + char
		else :
			temp += char

	return temp

#Test les identifiants de connection
def connection(pLogin,pMdp) :

	db = MySQLConnect()

  	sql	= "SELECT id FROM utilisateur WHERE prenom = Login AND password = MD5(Mdp)"
  	sql = sql.replace("Login","'" + pLogin + "'")
  	sql = sql.replace("Mdp","'" + pMdp +"'")

	cursor = db.cursor()
	cursor.execute(sql)

	return(cursor.fetchone() != None)

#Met à jour la table avec le mot de passe temporaire
def updatePassword(pNewMdp,pId) :

	db = MySQLConnect()

  	sql	= "UPDATE utilisateur SET password = NewMdp WHERE id = " + pId
  	sql = sql.replace("NewMdp","'" + pNewMdp + "'")
 
	cursor = db.cursor()
	cursor.execute(sql)