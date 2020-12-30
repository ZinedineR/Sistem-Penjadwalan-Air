import sqlite3

#class model
class model:
	def __init__(self):
		try:
		    self._conn = sqlite3.connect('database.sqlite')
		    self._cursor = self._conn.cursor()
		except:
		    return("Error Gagal terkoneksi ke Database")
	def close(self):
	    	self._conn.close()
	# method abstract
	def get(self):
			pass
	# method abstract
	def getId(self, id):
			pass
	# method abstract
	def delete(self, id):
			pass

# class modelAdmin
class modelAdmin(model):
	def __init__(self):
			super().__init__()
			query = '''CREATE TABLE IF NOT EXISTS admin (
		                                id_admin INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
		                                email VARCHAR NOT NULL,
		                                password VARCHAR NOT NULL);'''
			self._cursor.execute(query)
			self._conn.commit()

	# fungsi cek login
	def cekLogin(self, email, password):
	        query = '''SELECT id_admin FROM admin WHERE email = ? AND password = ?'''
	        data = (email, password)
	        self._cursor.execute(query, data)
	        records = self._cursor.fetchone()
	        return(records)

	# fungsi untuk menambah data
	def insert(self, email, password):
	    try:    
	        query = '''INSERT INTO admin (email, password) VALUES (?, ?);'''
	        data = (email, password)
	        self._cursor.execute(query, data)
	        self._conn.commit()
	        return("\nBerhasil menambah data")
	    except:
	    	return("\nKesalahan input, gagal menambah data")

	# fungsi untuk melihat semua data
	def get(self):
	        query = '''SELECT * FROM admin'''
	        self._cursor.execute(query)
	        records = self._cursor.fetchall()
	        return(records)
	 
	# fungsi untuk melihat data berdasarkan id
	def getId(self, id):
	        query = '''SELECT * FROM admin WHERE id_admin = ?'''
	        self._cursor.execute(query, [id])
	        records = self._cursor.fetchall()
	        return(records)

	# fungsi untuk melihat data berdasarkan email
	def getEmail(self, email):
	        query = '''SELECT * FROM admin WHERE email = ?'''
	        self._cursor.execute(query, [email])
	        records = self._cursor.fetchall()
	        return(records)

	# fungsi untuk update data
	def update(self, id, email, password):
	    try:
	        query = '''UPDATE penghuni SET email = ?, password = ? WHERE id_admin = ?'''
	        data = (email, password, id)
	        self._cursor.execute(query, data)
	        self._conn.commit()
	        return("\nUpdate Data Sukses")
	    except:
	    	return("\nKesalahan input, gagal update data")

	# fungsi untuk menghapus data
	def delete(self, id):
	    try:    
	        query = '''DELETE FROM admin WHERE id_admin = ?'''
	        self._cursor.execute(query, [id])
	        self._conn.commit()
	        return("\nHapus Data Sukses")
	    except:
	    	return("\nKesalahan input, gagal hapus data")

# class modelPenghuni
class modelPenghuni(model):
	def __init__(self):
			super().__init__()
			query = '''CREATE TABLE IF NOT EXISTS penghuni (
		                                id_penghuni INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
		                                nama VARCHAR NOT NULL,
		                                semester VARCHAR NOT NULL,
		                                email VARCHAR NOT NULL,
		                                password VARCHAR NOT NULL,
		                                id_lorong INTEGER NOT NULL,
		                                id_admin INTEGER NOT NULL);'''
			self._cursor.execute(query)
			self._conn.commit()

	# fungsi cek login
	def cekLogin(self, email, password):
	        query = '''SELECT id_penghuni FROM penghuni WHERE email = ? AND password = ?'''
	        data = (email, password)
	        self._cursor.execute(query, data)
	        records = self._cursor.fetchone()
	        return(records)

	# fungsi untuk menambah data
	def insert(self, nama, semester, email, password, id_lorong, id_admin):
	    try:
	        query = '''INSERT INTO penghuni
	                          (nama, semester, email, password, id_lorong, id_admin) 
	                          VALUES (?, ?, ?, ?, ?, ?);'''
	        data = (nama, semester, email, password, id_lorong, id_admin)
	        self._cursor.execute(query, data)
	        self._conn.commit()
	        return("\nberhasil menambah data")
	    except:
	    	return("\nKesalahan input, gagal menambah data")

	# fungsi untuk melihat semua data
	def get(self):
	        query = '''SELECT * FROM penghuni'''
	        self._cursor.execute(query)
	        records = self._cursor.fetchall()
	        return(records)
	 
	# fungsi untuk melihat data berdasarkan id
	def getId(self, id):
	        query = '''SELECT * FROM penghuni WHERE id_penghuni = ?'''
	        self._cursor.execute(query, [id])
	        records = self._cursor.fetchall()
	        return(records)

	# fungsi untuk melihat data berdasarkan nama
	def getNama(self, nama):
	        query = '''SELECT * FROM penghuni WHERE nama = ?'''
	        self._cursor.execute(query, [nama])
	        records = self._cursor.fetchall()
	        return(records)

	# fungsi untuk melihat data berdasarkan semester
	def getSemester(self, semester):
	        query = '''SELECT * FROM penghuni WHERE semester = ?'''
	        self._cursor.execute(query, [semester])
	        records = self._cursor.fetchall()
	        return(records)

	# fungsi untuk melihat data berdasarkan email
	def getEmail(self, email):
	        query = '''SELECT * FROM penghuni WHERE email = ?'''
	        self._cursor.execute(query, [email])
	        records = self._cursor.fetchall()
	        return(records)

	# fungsi untuk melihat data berdasarkan id lorong
	def getIdLorong(self, id):
	        query = '''SELECT * FROM penghuni WHERE id_lorong = ?'''
	        self._cursor.execute(query, [id])
	        records = self._cursor.fetchall()
	        return(records)

	# fungsi untuk update data
	def update(self, id, nama, semester, email, password, id_lorong):
	    try:
	        query = '''UPDATE penghuni SET nama = ?, semester = ?, email = ?, password = ?, id_lorong = ? WHERE id_penghuni = ?'''
	        data = (nama, semester, id_lorong, id)
	        self._cursor.execute(query, data)
	        self._conn.commit()
	        return("\nUpdate Data Sukses")
	    except:
	    	return("\nKesalahan input, gagal update data")

	# fungsi untuk menghapus data
	def delete(self, id):
		try:
			query = '''DELETE FROM penghuni WHERE id_penghuni = ?'''
			self._cursor.execute(query, [id])
			self._conn.commit()
			return("\nHapus Data Sukses")
		except:
			return("\nKesalahan input, gagal hapus data")

# class modelLorong
class modelLorong(model):
	def __init__(self):
			super().__init__()
			query = '''CREATE TABLE IF NOT EXISTS lorong (
		                                id_lorong INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
		                                nama_lorong VARCHAR NOT NULL);'''
			self._cursor.execute(query)
			self._conn.commit()

	# fungsi untuk menambah data
	def insert(self, nama_lorong):
	    try:
	        query = '''INSERT INTO lorong
	                          (nama_lorong) 
	                          VALUES (?);'''
	        data = nama_lorong
	        self._cursor.execute(query, [data])
	        self._conn.commit()
	        return("\nberhasil menambah data")
	    except:
	    	return("\nKesalahan input, gagal menambah data")

	# fungsi untuk melihat semua data
	def get(self):
	        query = '''SELECT * FROM lorong'''
	        self._cursor.execute(query)
	        records = self._cursor.fetchall()
	        return(records)
	 
	# fungsi untuk melihat data berdasarkan id lorong
	def getId(self, id):
	        query = '''SELECT * FROM lorong WHERE id_lorong = ?'''
	        self._cursor.execute(query, [id])
	        records = self._cursor.fetchall()
	        return(records)

	# fungsi untuk melihat data berdasarkan nama_lorong
	def getNamaLorong(self, nama_lorong):
	        query = '''SELECT * FROM lorong WHERE nama_lorong = ?'''
	        self._cursor.execute(query, [nama_lorong])
	        records = self._cursor.fetchall()
	        return(records)

	# fungsi untuk update data
	def update(self, id, nama_lorong):
		try:
			query = '''UPDATE lorong SET nama_lorong = ? WHERE id_lorong = ?'''
			data = (nama_lorong, id)
			self._cursor.execute(query, data)
			self._conn.commit()
			return("\nUpdate Data Sukses")
		except:
			return("\nKesalahan input, gagal update data")

	# fungsi untuk menghapus data
	def delete(self, id):
	    try:
	        query = '''DELETE FROM lorong WHERE id_lorong = ?'''
	        self._cursor.execute(query, [id])
	        self._conn.commit()
	        return("\nHapus Data Sukses")
	    except:
	    	return("\nKesalahan input, gagal hapus data")

# class modelPenggunaan
class modelPenggunaan(model):
	def __init__(self):
			super().__init__()
			query = '''CREATE TABLE IF NOT EXISTS lorong (
		                                id_penggunaan INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
		                                deskripsi VARCHAR NOT NULL);'''
			self._cursor.execute(query)
			self._conn.commit()

	# fungsi untuk menambah data
	def insert(self, penggunaan):
	    try:
	        query = '''INSERT INTO penggunaan
	                          (deskripsi) 
	                          VALUES (?);'''
	        data = nama_lorong
	        self._cursor.execute(query, [data])
	        self._conn.commit()
	        return("\nberhasil menambah data ke tabel")
	    except:
	    	return("\nKesalahan input, gagal menambah data")

	# fungsi untuk melihat semua data
	def get(self):
	        query = '''SELECT * FROM penggunaan'''
	        self._cursor.execute(query)
	        records = self._cursor.fetchall()
	        return(records)
	 
	# fungsi untuk melihat data berdasarkan id penggunaan
	def getId(self, id):
	        query = '''SELECT * FROM penggunaan WHERE id_penggunaan = ?'''
	        self._cursor.execute(query, [id])
	        records = self._cursor.fetchall()
	        return(records)

	# fungsi untuk melihat data berdasarkan deskripsi
	def getDeskripsi(self, deskripsi):
	        query = '''SELECT * FROM penggunaan WHERE deskripsi = ?'''
	        self._cursor.execute(query, [deskripsi])
	        records = self._cursor.fetchall()
	        return(records)

	# fungsi untuk update data
	def update(self, id, deskripsi):
	    try:
	        query = '''UPDATE penggunaan SET deskripsi = ? WHERE id_penggunaan = ?'''
	        data = (deskripsi, id)
	        self._cursor.execute(query, data)
	        self._conn.commit()
	        return("\nUpdate Data Sukses")
	    except:
	    	return("\nKesalahan input, gagal update data")

	# fungsi untuk menghapus data
	def delete(self, id):
	    try:
	        query = '''DELETE FROM penggunaan WHERE id_penggunaan = ?'''
	        self._cursor.execute(query, [id])
	        self._conn.commit()
	        return("\nHapus Data Sukses")
	    except:
	    	return("\nKesalahan input, gagal hapus data")

# class modelJadwal
class modelJadwal(model):
	def __init__(self):
			super().__init__()
			query = '''CREATE TABLE IF NOT EXISTS jadwal (
		                                id_jadwal INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
		                                waktu_mulai VARCHAR NOT NULL,
		                                waktu_selesai VARCHAR NOT NULL,
		                                tanggal VARCHAR NOT NULL,
		                                id_lorong INTEGER NOT NULL,
		                                id_penggunaan INTEGER NOT NULL);'''
			self._cursor.execute(query)
			self._conn.commit()

	# fungsi untuk menambah data
	def insert(self, tanggal, id_lorong, id_penggunaan):
	    try:
	        validasi = '''SELECT * FROM jadwal WHERE tanggal = ?'''
	        self._cursor.execute(query, [tanggal])
	        records = self._conn.fetchall()
	        if count(records) > 2:
	        	return("\nMaaf tanggal tersebut telah full")
	        elif count(records) == 1 and records[1] == "06.00":
	        	waktu_mulai = "12.00"
	        	waktu_selesai = "17.00"
	        else:
	        	waktu_mulai = "06.00"
	        	waktu_selesai = "11.00"
	        query = '''INSERT INTO jadwal
	                          (waktu_mulai, waktu_selesai, tanggal, id_lorong, id_penggunaan) 
	                          VALUES (?, ?, ?, ?, ?);'''
	        data = (waktu_mulai, waktu_selesai, tanggal, id_lorong, id_penggunaan)
	        self._cursor.execute(query, data)
	        self._conn.commit()
	        return("\nberhasil menambah data")
	    except:
	    	return("\nKesalahan input, gagal menambah data")

	# fungsi untuk melihat semua data
	def get(self):
	        query = '''SELECT * FROM jadwal'''
	        self._cursor.execute(query)
	        records = self._cursor.fetchall()
	        return(records)
	 
	# fungsi untuk melihat data berdasakan id jadwal
	def getId(self, id):
	        query = '''SELECT * FROM jadwal WHERE id_jadwal = ?'''
	        self._cursor.execute(query, [id])
	        records = self._cursor.fetchall()
	        return(records)

	# fungsi untuk melihat data berdasakan waktu mulai
	def getWaktuMulai(self, waktu_mulai):
	        query = '''SELECT * FROM jadwal WHERE waktu_mulai = ?'''
	        self._cursor.execute(query, [waktu_mulai])
	        records = self._cursor.fetchall()
	        return(records)

	# fungsi untuk melihat data berdasakan waktu selesai
	def getWaktuSelesai(self, waktu_selesai):
	        query = '''SELECT * FROM jadwal WHERE waktu_selesai = ?'''
	        self._cursor.execute(query, [waktu_selesai])
	        records = self._cursor.fetchall()
	        return(records)

	# fungsi untuk melihat data berdasakan tanggal
	def getTanggal(self, tanggal):
	        query = '''SELECT * FROM jadwal WHERE tanggal = ?'''
	        self._cursor.execute(query, [tanggal])
	        records = self._cursor.fetchall()
	        return(records)

	# fungsi untuk melihat data berdasakan id lorong
	def getIdLorong(self, id):
	        query = '''SELECT * FROM jadwal WHERE id_lorong = ?'''
	        self._cursor.execute(query, [id])
	        records = self._cursor.fetchall()
	        return(records)

	# fungsi untuk melihat data berdasakan id penggunaan
	def getIdPenggunaan(self, id):
	        query = '''SELECT * FROM jadwal WHERE id_penggunaan = ?'''
	        self._cursor.execute(query, [id])
	        records = self._cursor.fetchall()
	        return(records)

	# fungsi untuk update data
	def update(self, id_jadwal, tanggal, id_lorong, id_penggunaan):
		try:
			validasi = '''SELECT * FROM jadwal WHERE tanggal = ?'''
			self._cursor.execute(query, [tanggal])
			records = self._conn.fetchall()
			if count(records) > 2:
				return("\nMaaf tanggal tersebut telah full")
			elif count(records) == 1 and records[1] == "06.00":
				waktu_mulai = "12.00"
				waktu_selesai = "17.00"
			else:
				waktu_mulai = "06.00"
				waktu_selesai = "11.00"
			query = '''UPDATE jadwal SET waktu_mulai = ?, waktu_selesai = ?, tanggal = ?, id_lorong = ?, id_penggunaan = ? WHERE id_jadwal = ?'''
			data = (waktu_mulai, waktu_selesai, tanggal, id_lorong, id_jadwal, id_penggunaan)
			self._cursor.execute(query, data)
			self._conn.commit()
			return("\nUpdate Data Sukses")
		except:
			return("\nKesalahan input, gagal update data")

	# fungsi untuk menghapus data
	def delete(self, id):
	    try:
	        query = '''DELETE FROM jadwal WHERE id_jadwal = ?'''
	        self._cursor.execute(query, [id])
	        self._conn.commit()
	        return("\nHapus Data Sukses")
	    except:
	    	return("\nKesalahan input, gagal hapus data")