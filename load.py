import mysql.connector
import os
import csv

con = mysql.connector.connect(
	host = 'localhost',
	user = 'felipe',
	password = 'Ufrj2016.2'
)

database = 'Intuitive'
tablename = 'Care'
directories = ['./Q3_csvs/']
cur = con.cursor()
cur.execute('CREATE DATABASE '+database+ ';')
cur.execute('USE '+database + ';')
for directory in directories:
	for filename in os.listdir(directory):
		if filename.endswith("csv"):
			with open(directory+filename,encoding="ISO-8859-1") as csv_file:
				if(filename.startswith("Relatorio")):
					[next(csv_file) for x in range(2)]
					head = csv_file.readline() 
					#print(head)
					head = head[:-1]
					columns_to_create = head.replace(" ","_")
					columns_to_create = columns_to_create.replace(';',' VARCHAR(255),') + ' VARCHAR(255)'
					columns_to_create = columns_to_create.replace('"Registro_ANS" VARCHAR(255)','"Registro_ANS" BIGINT')
					columns_to_create = columns_to_create.replace('"Data_Registro_ANS" VARCHAR(255)','"Data_Registro_ANS" DATE')
					columns_to_create = columns_to_create.replace("\"","")
					id_column = 'id INT NOT NULL AUTO_INCREMENT PRIMARY KEY'
					#print(columns_to_create)
					command = 'CREATE TABLE IF NOT EXISTS '+'Relatorio'+'('+columns_to_create+','+id_column+');'
					print(filename)
					print(command)
					cur.execute(command)
					csv_data = csv_file.readlines()
					columns_to_create = columns_to_create.replace('VARCHAR(255)','')
					columns_to_create = columns_to_create.replace('DATE','')
					columns_to_create = columns_to_create.replace('BIGINT','')
					for line in csv_data:
						values = line[:-1].replace('\'','\"').replace('\"','').split(';')
						data_campos = values[-1].split('/')
						data = '%s-%s-%s'%tuple([data_campos[2],data_campos[1],data_campos[0]])
						values[-1] = data
						#print(values)
						operation = 'INSERT INTO '+'Relatorio'+'('+columns_to_create+')'
						command = operation+'VALUES("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")'%tuple(values)+';'
						cur.execute(command)
				else:
					head = csv_file.readline() 
					#print(head)
					head = head[:-1]
					columns_to_create = head.replace(';',' VARCHAR(255),') + ' VARCHAR(255)'
					columns_to_create = columns_to_create.replace('"DESCRICAO"','DESCRICAO')
					columns_to_create = columns_to_create.replace('"REG_ANS" VARCHAR(255)','REG_ANS BIGINT')
					columns_to_create = columns_to_create.replace('"CD_CONTA_CONTABIL" VARCHAR(255)','CD_CONTA_CONTABIL BIGINT')
					columns_to_create = columns_to_create.replace('"DATA" VARCHAR(255)','DATA DATE')
					columns_to_create = columns_to_create.replace('"VL_SALDO_FINAL" VARCHAR(255)','VL_SALDO_FINAL DECIMAL(16,2)')
					id_column = 'id INT NOT NULL AUTO_INCREMENT PRIMARY KEY'
					#print(columns_to_create)
					command = 'CREATE TABLE IF NOT EXISTS '+tablename+'('+columns_to_create+','+id_column+');'
					print(filename)
					print(command)
					cur.execute(command)
					csv_data = csv_file.readlines()
					columns_to_create = columns_to_create.replace('VARCHAR(255)','')
					columns_to_create = columns_to_create.replace('DATE','')
					columns_to_create = columns_to_create.replace('BIGINT','')
					columns_to_create = columns_to_create.replace('DECIMAL(16,2)','')
					for line in csv_data:
						values = line[:-1].replace('\'','\"').replace('\"','').split(';')
						data_campos = values[0].split('/')
						data = '%s-%s-%s'%tuple([data_campos[2],data_campos[1],data_campos[0]])
						values[0] = data
						values[-1] = values[-1].replace(',','.')
						#print(values)
						operation = 'INSERT INTO '+tablename+'('+columns_to_create+')'
						command = operation+'VALUES("%s","%s","%s","%s","%s")'%tuple(values)+';'
						cur.execute(command)
						
#close the connection to the database.
print('-------ok  ')
#cur.execute('ALTER TABLE '+tablename+' MODIFY COLUMN value FLOAT(16,2);')
print('-------ok  ')
#cur.execute('ALTER TABLE '+tablename+' MODIFY COLUMN timestamp BIGINT;')
print('-------ok  ')
con.commit()
con.close()
