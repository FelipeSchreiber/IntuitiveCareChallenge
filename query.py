import mysql.connector
import os
import csv

con = mysql.connector.connect(
	host = 'localhost',
	user = 'felipe',
	password = 'Ufrj2016.2',
	database = 'Intuitive'
)

tablename = 'Care'
cur = con.cursor()
max_date = "SELECT MAX(DATA) FROM "+tablename
min_date = "SELECT DATE_ADD(({}),INTERVAL -3 DAY)".format(max_date)
cur.execute(min_date)
rows = cur.fetchall()
print('Data de inicio:\n{}\n'.format(rows[0][0]))
subquery1 = "SELECT * FROM "+tablename+" WHERE DESCRICAO LIKE '%EVENTOS/ SINISTROS CONHECIDOS%' AND DATA >= ({})".format(min_date)
#print(subquery1)
subquery2 = "SELECT REG_ANS, SUM(VL_SALDO_FINAL) AS total FROM ({}) AS sub1 GROUP BY REG_ANS ORDER BY  total DESC limit 10".format(subquery1)
subquery3 = "SELECT REG_ANS FROM ({}) AS sub2".format(subquery2)
command = "SELECT Razão_Social FROM Relatorio WHERE Registro_ANS IN ({})".format(subquery3)
#print(command)
cur.execute(command)
rows = cur.fetchall()
for r in rows:
	print(r[0])
print('-----------------------FIM QUERY 1------------------------------')

min_date = "SELECT DATE_ADD(({}),INTERVAL -1 YEAR)".format(max_date)
cur.execute(min_date)
rows = cur.fetchall()
print('Data de inicio:\n{}\n'.format(rows[0][0]))
subquery1 = "SELECT * FROM "+tablename+" WHERE DESCRICAO LIKE '%EVENTOS/ SINISTROS CONHECIDOS%' AND DATA >= ({})".format(min_date)
#print(subquery1)
subquery2 = "SELECT REG_ANS, SUM(VL_SALDO_FINAL) AS total FROM ({}) AS sub1 GROUP BY REG_ANS ORDER BY  total DESC limit 10".format(subquery1)
subquery3 = "SELECT REG_ANS FROM ({}) AS sub2".format(subquery2)
command = "SELECT Razão_Social FROM Relatorio WHERE Registro_ANS IN ({})".format(subquery3)
#print(command)
cur.execute(command)
rows = cur.fetchall()
for r in rows:
	print(r[0])
print('-----------------------FIM QUERY 2------------------------------')
con.close()
