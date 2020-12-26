import sqlite3

# class model
class model:
	def delete(self, id):
		pass

# class modelAstri
class modelAstri(model):
	def __init__(self):
		try:
		    self.conn = sqlite3.connect('database.sqlite')
		    self.cursor = self.conn.cursor()
		    query = '''CREATE TABLE IF NOT EXISTS astri (
		                                id_astri INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
		                                nama VARCHAR NOT NULL,
		                                semester VARCHAR NOT NULL);'''
		    self.cursor.execute(query)
		    self.conn.commit()
		    # cursor.close() 
		except sqlite3.Error as error:
		    return("Error Gagal terkoneksi ke Database", error)

	# fungsi untuk menambah data
	def insert(self, nama, semester):
	        query = '''INSERT INTO astri
	                          (nama, semester) 
	                          VALUES (?, ?);'''
	        data = (nama, semester)
	        self.cursor.execute(query, data)
	        self.conn.commit()
	        return("\nberhasil menambah data ke tabel")

	# fungsi untuk melihat semua data
	# overloading
	def get(self):
	        query = '''SELECT * FROM astri'''
	        self.cursor.execute(query)
	        records = self.cursor.fetchall()
	        return(records)
	 
	# fungsi untuk melihat data berdasarkan id
	# overloading
	def getId(self, id):
	        query = '''SELECT * FROM astri WHERE id_astri = ?'''
	        self.cursor.execute(query, [id])
	        records = self.cursor.fetchall()
	        return(records)

	# fungsi untuk melihat data berdasarkan nama
	def getNama(self, nama):
	        query = '''SELECT * FROM astri WHERE nama = ?'''
	        self.cursor.execute(query, [nama])
	        records = self.cursor.fetchall()
	        return(records)

	# fungsi untuk melihat data berdasarkan semester
	def getSemester(self, semester):
	        query = '''SELECT * FROM astri WHERE semester = ?'''
	        self.cursor.execute(query, [semester])
	        records = self.cursor.fetchall()
	        return(records)

	# fungsi untuk update data
	def update(self, id, nama, semester):
	        query = '''UPDATE astri SET nama = ?, semester = ? WHERE id_astri = ?'''
	        data = (nama, semester, id)
	        self.cursor.execute(query, data)
	        self.conn.commit()
	        return("\nUpdate Data Sukses")

	# fungsi untuk menghapus data
	# overriding
	def delete(self, id):
	        query = '''DELETE FROM astri WHERE id_astri = ?'''
	        self.cursor.execute(query, [id])
	        self.conn.commit()
	        return("\nHapus Data Sukses")

	# overriding
	def close(self):
	    self.conn.close()

# class modelJadwal
class modelJadwal(model):
	def __init__(self):
		try:
		    self.conn = sqlite3.connect('database.sqlite')
		    self.cursor = self.conn.cursor()
		    query = '''CREATE TABLE IF NOT EXISTS jadwal (
		                                id_jadwal INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
		                                hari VARCHAR NOT NULL,
		                                tanggal VARCHAR NOT NULL,
		                                kegiatan VARCHAR NOT NULL,
		                                id_astri INTEGER NOT NULL);'''
		    self.cursor.execute(query)
		    self.conn.commit()
		    # cursor.close() 
		except sqlite3.Error as error:
		    return("Error Gagal terkoneksi ke Database", error)

	# fungsi untuk menambah data
	def insert(self, hari, tanggal, kegiatan, id):
	        query = '''INSERT INTO jadwal
	                          (hari, tanggal, kegiatan, id_astri) 
	                          VALUES (?, ?, ?, ?);'''
	        data = (hari, tanggal, kegiatan, id)
	        self.cursor.execute(query, data)
	        self.conn.commit()
	        return("\nberhasil menambah data ke tabel")

	# fungsi untuk melihat semua data
	# overloading
	def get(self):
	        query = '''SELECT * FROM jadwal'''
	        self.cursor.execute(query)
	        records = self.cursor.fetchall()
	        return(records)
	 
	# fungsi untuk melihat data berdasakan id jadwal
	# overloading
	def getId(self, id):
	        query = '''SELECT * FROM jadwal WHERE id_jadwal = ?'''
	        self.cursor.execute(query, [id])
	        records = self.cursor.fetchall()
	        return(records)

# fungsi untuk melihat data berdasakan id jadwal
	def getHari(self, hari):
	        query = '''SELECT * FROM jadwal WHERE hari = ?'''
	        self.cursor.execute(query, [hari])
	        records = self.cursor.fetchall()
	        return(records)

# fungsi untuk melihat data berdasakan id jadwal
	def getTanggal(self, tanggal):
	        query = '''SELECT * FROM jadwal WHERE tanggal = ?'''
	        self.cursor.execute(query, [tanggal])
	        records = self.cursor.fetchall()
	        return(records)

# fungsi untuk melihat data berdasakan id jadwal
	def getKegiatan(self, kegiatan):
	        query = '''SELECT * FROM jadwal WHERE kegiatan = ?'''
	        self.cursor.execute(query, [kegiatan])
	        records = self.cursor.fetchall()
	        return(records)

# fungsi untuk melihat data berdasakan id jadwal
	def getIdAstri(self, id):
	        query = '''SELECT * FROM jadwal WHERE id_astri = ?'''
	        self.cursor.execute(query, [id])
	        records = self.cursor.fetchall()
	        return(records)

	# fungsi untuk update data
	def update(self, id_jadwal, hari, tanggal, kegiatan, id_astri):
	        query = '''UPDATE jadwal SET hari = ?, tanggal = ?, kegiatan = ?, id_astri = ? WHERE id_jadwal = ?'''
	        data = (hari, tanggal, kegiatan, id_astri, id_jadwal)
	        self.cursor.execute(query, data)
	        self.conn.commit()
	        return("\nUpdate Data Sukses")

	# fungsi untuk menghapus data
	# overriding
	def delete(self, id):
	        query = '''DELETE FROM jadwal WHERE id_jadwal = ?'''
	        self.cursor.execute(query, [id])
	        self.conn.commit()
	        return("\nHapus Data Sukses")
	        
	# overriding
	def close(self):
	     self.conn.close()