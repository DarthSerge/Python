#!C:\Python27\python.exe

import cgitb
cgitb.enable()

import cgi
import MySQLdb

def MySQLConnect() :

	return MySQLdb.connect("localhost", "root", "", "utilisateurs")

def checkInjection(pString) :

	if pString == None :

		return ""

	temp = ""

	for char in pString :

		if char == "'" :

			temp += "\\" + char

		else :

			temp += char

	return temp

def connection(pLogin,pMdp) :

	db = MySQLConnect()

	sql	= "SELECT id, admin FROM utilisateur WHERE email = Login AND password = MD5(Mdp)"

	sql = sql.replace("Login","'" + pLogin + "'")
	sql = sql.replace("Mdp","'" + pMdp +"'")

	cursor = db.cursor()

	cursor.execute(sql)

	row = cursor.fetchone()

	if row == None :

		return -1

	else :

		return row[1]

def updatePassword(pNewMdp,pId) :

	db = MySQLConnect()

	sql	= "UPDATE utilisateur SET password = MD5(NewMdp) WHERE id = " + str(pId)

	sql = sql.replace("NewMdp","'" + pNewMdp + "'")

	cursor = db.cursor()

	cursor.execute(sql)

def recupId(pEmail):

	db = MySQLConnect()

	sql = "SELECT id FROM utilisateur WHERE not(admin) AND email = emailRecup"

	sql = sql.replace("emailRecup","'" + pEmail + "'")

	cursor = db.cursor()

	cursor.execute(sql)

	row = cursor.fetchone()

	if row == None :

		return 0

	else :

		return row[0]