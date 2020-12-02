import sqlite3
con = sqlite3.connect('properties/db.sqlite')
cursor = con.cursor()

def insert_penghuni():
    query = 'insert into penghuni(namapenghuni) VALUES (\'%s\');'
    query = query  % ('Siska')
    cursor.execute(query)
    con.commit()


def select_penghuni():
    query = 'select * from penghuni'  
    cursor.execute(query)
    all_results = cursor.fetchall()
    con.commit()
    for result in all_results:
        print(result)

select_penghuni()
#insert_penghuni()

# class DataManager:
# 	def __init__(self):
# 		self.con = sqlite3.connect('properties/db.sqlite')
# 		self.cursor = self.con.cursor() # instantiate a cursor obj
# 	def executeQuery(self, query, retVal=False):
# 		self.cursor.execute(query)
# 		all_results = self.cursor.fetchall()
# 		self.con.commit()
# 		if retVal:
# 			return all_results
        
# class Astri(DataManager):
# 	def setDataPerson(self, nama, email):
# 		self.query = 'INSERT INTO Person (nama, email) \
# 			VALUES (\'%s\', \'%s\')' 
# 		self.query = self.query % (nama, email)
# 		print('self.query : ', self.query )
# 		self.executeQuery(self.query)
# 		
# 	def getDataPerson(self, nama, email):
# 		self.query = 'SELECT id_person FROM Person \
# 			where nama=\'%s\' and email=\'%s\' ' 
# 		self.query = self.query % (nama, email)
# 		print('self.query : ', self.query )
# 		id_person = self.executeQuery(self.query, retVal=True)
# 		return id_person

