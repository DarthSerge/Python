#!C:\Python27\python.exe

import cgitb
cgitb.enable()

import cgi
import MySQLdb

def MySQLConnect() :

	db = MySQLdb.connect("localhost", "root", "", "utilisateurs")

def checkInjection(pString) :
	temp = ""
	for char in pString :
		if char == "'" :
			temp += "\\" + char
		else :
			temp += char

	return temp

def queryConnection(pLogin,pMdp) :

	db = MySQLdb.connect("localhost", "root", "", "utilisateurs")

  	sql	= "SELECT id FROM utilisateur WHERE prenom = Login AND password = MD5(Mdp)"

  	sql = sql.replace("Login","'" + pLogin + "'")
  	sql = sql.replace("Mdp","'" + pMdp +"'")

	cursor = db.cursor()

	cursor.execute(sql)

	return(cursor.fetchone() != None)
