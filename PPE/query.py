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

  	sql	= "PREPARE check_id " \
		+ "FROM 'SELECT id FROM utilisateur WHERE prenom = ? AND password = ?'; " \
		+ "SET @login = '" + pLogin + "'; " \
  		+ "SET @mdp = '" + pMdp + "'; " \
		+ "EXECUTE check_id USING @login , @mdp; "
	cursor = db.cursor()

	cursor.execute(sql)

	print cursor.rowcount

	print sql

	return(cursor.rowcount != 0)
