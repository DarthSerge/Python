#!C:\Python27\python.exe

import cgitb
cgitb.enable()

import cgi
import MySQLdb

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

def connection(pLogin,pMdp) :

	db = MySQLConnect()

  	sql	= "SELECT id FROM utilisateur WHERE prenom = Login AND password = MD5(Mdp)"

  	sql = sql.replace("Login","'" + pLogin + "'")
  	sql = sql.replace("Mdp","'" + pMdp +"'")

	cursor = db.cursor()

	cursor.execute(sql)

	return(cursor.fetchone() != None)

def updatePassword(pNewMdp,pId) :

	db = MySQLConnect()

  	sql	= "UPDATE utilisateur SET password = MD5(NewMdp) WHERE id = " + str(pId)

  	sql = sql.replace("NewMdp","'" + pNewMdp + "'")
 
	cursor = db.cursor()

	cursor.execute(sql)

def recupId(pEmail):

	db = MySQLConnect()
 
 	sql = "SELECT id FROM utilisateur WHERE not(admin) AND email = emailrecup"

 	sql = sql.replace("emailrecup","'" + pEmail + "'")

   	cursor = db.cursor()

   	cursor.execute(sql)

	if cursor.fetchone() != None :
		return cursor.fetchone()
   	else :
   		return 0