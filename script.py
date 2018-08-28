import sys
import xml.dom.minidom

import psycopg2 #using PostgreSQL
""" 
#for mSQL lite connections
import mysql.connector
from mysql.connector import errorcode 
"""

'''
	Kevin Gamez CS288 FALL 2017
'''
doc = xml.dom.minidom.parse(sys.argv[1])
tables=doc.getElementsByTagName('table')[2] #look only nodes from this portion
skip=0
#print("Exchange, Symbol, Company, Volume, Price, Change") #first line reserved as a header
try:
	#make a database called 'stocks'
	#cnx = mysql.connector.connect(user='root',password='pass',database='stocks')
	cnx=psycopg2.connect(
		host="localhost",
		dbname="-",
		user="-",
		password="-"
	)
	cursor=cnx.cursor() #create cursor obj.
	cursor.execute("DROP TABLE IF EXISTS data") #overwrite old table
	query="CREATE TABLE data(Exchange TEXT,Symbol TEXT PRIMARY KEY,Company VARCHAR(64),Volume VARCHAR(16),Price NUMERIC, Diff NUMERIC)"
	cursor.execute(query)
	exh='NYSE'
	for tr in tables.getElementsByTagName('tr'): #each row
		for td in tr.getElementsByTagName('td'):
			for a in td.getElementsByTagName('a'): #there's an <a> tag!
				name=a.firstChild.nodeValue.split('(') #make an array
				n= name[0] #get name
				sym= name[1].replace(')',"") #get Symbol
		if skip==0: #skip the row headers
			skip=skip+1
			#print "skip"
			continue
		vol=tr.getElementsByTagName('td')[2].firstChild.nodeValue.replace(',','') #gets rid of commas
		price=float(tr.getElementsByTagName('td')[3].firstChild.nodeValue.replace('$',''))
		chg=float(tr.getElementsByTagName('td')[4].firstChild.nodeValue)
#PHP INPUT--->
		query="INSERT INTO data (Exchange, Symbol, Company, Volume, Price, Diff) VALUES (%s,%s,%s,%s,%s,%s)"
		cursor.execute(query,(exh,sym,n,vol,price,chg))
		#cursor.execute("") #set key
except psycopg2.DatabaseError as err:
	print(err)
else:
	cnx.commit()
	cnx.close()
	#print("NYSE,%s,%s,%s,%s,%s" %(sym,n,vol,price,chg) ).replace("\n","") #there was a '\n' character somewhere

	#cant use %d in query, use %s!
	#cant use % in query
	#cant use 'query VALUES( %s,...,%s) % (var,...) ' --> has to be separate (,)
