import model

# class abstract controller
class controller:
	# method abstract
	def insert(self):
		pass
	# method abstract
	def get(self):
		pass
	# method abstract
	def getId(self):
		pass
	# method abstract
	def update(self):
		pass
	# method abstract
	def delete(self):
		pass
	# method abstract
	def close(self):
		pass

# class penghuni
class admin(controller):
	__model_admin = model.modelAdmin()
	def __init__(self):
		self.__model_admin = model.modelAdmin()
	# overriding
	def cekLogin(self, email, password):
		login = self.__model_admin.cekLogin(email, password)
		if login == None:
			return("0")
		else:
			return(login)
	def insert(self):
		email = input("Masukkan Email Admin : ")
		password = input("Masukkan Password Admin : ")
		return(self.__model_admin.insert(email, password))
	# overriding
	def get(self):
		records = self.__model_admin.get()
		print("Id Admin     Email     Password")
		for n in records:
			print("  ",n[0],"    ",n[1],"    ",n[2])
	# overriding
	def getId(self):
		id_admin = input("Masukkan Id Admin : ")
		records = self.__model_admin.getId(id_admin)
		print("Id admin     Email     Password")
		for n in records:
			print("  ",n[0],"    ",n[1],"    ",n[2])
	def getEmail(self):
		email = input("Masukkan Email Admin : ")
		records = self.__model_admin.getEmail(email)
		print("Id admin     Email     Password")
		for n in records:
			print("  ",n[0],"    ",n[1],"    ",n[2])
	def update(self):
		self.get()
		id_admin = input("Masukkan Id Admin : ")
		email = input("Masukkan Email Admin : ")
		password = input("Masukkan Password Admin : ")
		return(self.__model_admin.update(id_admin, email, password))
	# overriding
	def delete(self):
		self.get()
		id_admin = input("Masukkan Id Admin yg ingin dihapus : ")
		return(self.__model_admin.delete(id_admin))
	# overriding
	def close(self):
		self.__model_admin.close()

# class penghuni
class penghuni(controller):
	__model_penghuni = model.modelPenghuni()
	def __init__(self):
		self.__model_penghuni = model.modelPenghuni()
	# overriding
	def cekLogin(self, email, password):
		login = self.__model_penghuni.cekLogin(email, password)
		if login == None:
			return("0")
		else:
			return(login)
	def insert(self):
		nama = input("Masukkan Nama Penghuni : ")
		semester = input("Masukkan Semester Penghuni : ")
		id_lorong = input("Masukkan Id Lorong : ")
		return(self.__model_penghuni.insert(nama, semester, id_lorong))
	# overriding
	def get(self):
		records = self.__model_penghuni.get()
		print("Id Penghuni     Nama     Semester    Id Lorong")
		for n in records:
			print("  ",n[0],"    ",n[1],"    ",n[2],"    ",n[3])
	# overriding
	def getId(self):
		id_penghuni = input("Masukkan Id Penghuni : ")
		records = self.__model_penghuni.getId(id_penghuni)
		print("Id Penghuni     Nama     Semester    Id Lorong")
		for n in records:
			print("  ",n[0],"    ",n[1],"    ",n[2],"    ",n[3])
	def getNama(self):
		nama = input("Masukkan NamaPenghuni : ")
		records = self.__model_penghuni.getNama(nama)
		print("Id Penghuni     Nama     Semester")
		for n in records:
			print("  ",n[0],"    ",n[1],"    ",n[2])
	def getSemester(self):
		semester = input("Masukkan Semester Penghuni : ")
		records = self.__model_penghuni.getSemester(semester)
		print("Id Penghuni     Nama     Semester    Id Lorong")
		for n in records:
			print("  ",n[0],"    ",n[1],"    ",n[2],"    ",n[3])
	def getIdLorong(self):
		id_lorong = input("Masukkan Id Lorong : ")
		records = self.__model_penghuni.getIdLorong(id_lorong)
		print("Id Penghuni     Nama     Semester    Id Lorong")
		for n in records:
			print("  ",n[0],"    ",n[1],"    ",n[2],"    ",n[3])
	def update(self):
		self.get()
		id_penghuni = input("Masukkan Id penghuni : ")
		nama = input("Masukkan Nama Penghuni : ")
		semester = input("Masukkan Semester Penghuni : ")
		id_lorong = input("Masukkan Id Lorong : ")
		return(self.__model_penghuni.update(id_penghuni, nama, semester, id_lorong))
	# overriding
	def delete(self):
		self.get()
		id_penghuni = input("Masukkan Id penghuni yg ingin dihapus : ")
		return(self.__model_penghuni.delete(id_penghuni))
	# overriding
	def close(self):
		self.__model_penghuni.close()

# class lorong
class lorong(controller):
	__model_lorong = model.modelLorong()
	def __init__(self):
		self.__model_lorong = model.modelLorong()
	# overriding
	def insert(self):
		nama = input("Masukkan Nama Lorong : ")
		return(self.__model_lorong.insert(nama))
	# overriding
	def get(self):
		records = self.__model_lorong.get()
		print("Id Lorong     Nama Lorong")
		for n in records:
			print("  ",n[0],"    ",n[1])
	# overriding
	def getId(self):
		id_lorong = input("Masukkan Id Lorong : ")
		records = self.__model_lorong.getId(id_lorong)
		print("Id Lorong     Nama Lorong")
		for n in records:
			print("  ",n[0],"    ",n[1])
	def getNama(self):
		nama = input("Masukkan Nama Lorong : ")
		records = self.__model_lorong.getNamaLorong(nama)
		print("Id Lorong     Nama Lorong")
		for n in records:
			print("  ",n[0],"    ",n[1])
	def update(self):
		self.get()
		id_lorong = input("Masukkan Id lorong : ")
		nama = input("Masukkan Nama lorong : ")
		return(self.__model_lorong.update(id_lorong, nama))
	# overriding
	def delete(self):
		self.get()
		id_lorong = input("Masukkan Id Lorong yg ingin dihapus : ")
		return(self.__model_lorong.delete(id_lorong))
	# overriding
	def close(self):
		self.__model_lorong.close()

# class penggunaan
class penggunaan(controller):
	__model_penggunaan = model.modelPenggunaan()
	def __init__(self):
		self.__model_penggunaan = model.modelPenggunaan()
	# overriding
	def insert(self):
		deskripsi = input("Masukkan Deskripsi Penggunaan : ")
		return(self.__model_penggunaan.insert(deskripsi))
	# overriding
	def get(self):
		records = self.__model_penggunaan.get()
		print("Id penggunaan     Deskripsi")
		for n in records:
			print("  ",n[0],"    ",n[1])
	# overriding
	def getId(self):
		id_penggunaan = input("Masukkan Id Penggunaan : ")
		records = self.__model_penggunaan.getId(id_penggunaan)
		print("Id penggunaan     Deskripsi")
		for n in records:
			print("  ",n[0],"    ",n[1])
	def getDeskripsi(self):
		deskripsi = input("Masukkan deskripsi penggunaan : ")
		records = self.__model_penggunaan.getDeskripsi(deskripsi)
		print("Id penggunaan     Deskripsi")
		for n in records:
			print("  ",n[0],"    ",n[1])
	def update(self):
		self.get()
		id_penggunaan = input("Masukkan Id Penggunaan : ")
		deskripsi = input("Masukkan Deskripsi : ")
		return(self.__model_penggunaan.update(id_penggunaan, deskripsi))
	# overriding
	def delete(self):
		self.get()
		id_penggunaan = input("Masukkan Id penggunaan yg ingin dihapus : ")
		return(self.__model_penggunaan.delete(id_penggunaan))
	# overriding
	def close(self):
		self.__model_penggunaan.close()

# class jadwal
class jadwal(controller):
	__model_jadwal = model.modelJadwal()
	def __init__(self):
		self.__model_jadwal = model.modelJadwal()
	# overriding
	def insert(self):
		Tanggal = input("Masukkan Tanggal : ")
		id_lorong = input("Masukkan Id Penghuni : ")
		id_penggunaan = input("Masukkan Id Penggunaan : ")
		return(self.__model_jadwal.insert(waktu_mulai, tanggal, id_lorong, id_penggunaan))
	# overriding
	def get(self):
		records = self.__model_jadwal.get()
		print("Id Jadwal      Waktu Mulai      Waktu Selesai       Tanggal       Id Lorong    Id Penggunaan")
		for n in records:
			print("  ",n[0],"    ",n[1],"    ",n[2],"    ",n[3],"    ",n[4],"    ",n[5])
	# overriding
	def getId(self):
		id_jadwal = input("Masukkan Id Jadwal : ")
		records = self.__model_jadwal.getId(id_jadwal)
		print("Id Jadwal      Waktu Mulai      Waktu Selesai       Tanggal       Id Lorong    Id Penggunaan")
		for n in records:
			print("  ",n[0],"    ",n[1],"    ",n[2],"    ",n[3],"    ",n[4],"    ",n[5])
	def getWaktuMulai(self):
		waktu = input("Masukkan Waktu Mulai : ")
		records = self.__model_jadwal.getWaktuMulai(waktu)
		print("Id Jadwal      Waktu Mulai      Waktu Selesai       Tanggal       Id Lorong    Id Penggunaan")
		for n in records:
			print("  ",n[0],"    ",n[1],"    ",n[2],"    ",n[3],"    ",n[4],"    ",n[5])
	def getWaktuSelesai(self):
		waktu = input("Masukkan Waktu Selesai : ")
		records = self.__model_jadwal.getWaktuSelesai(waktu)
		print("Id Jadwal      Waktu Mulai      Waktu Selesai       Tanggal       Id Lorong    Id Penggunaan")
		for n in records:
			print("  ",n[0],"    ",n[1],"    ",n[2],"    ",n[3],"    ",n[4],"    ",n[5])
	def getTanggal(self):
		tanggal = input("Masukkan Tanggal : ")
		records = self.__model_jadwal.getTanggal(tanggal)
		print("Id Jadwal      Waktu Mulai      Waktu Selesai       Tanggal       Id Lorong    Id Penggunaan")
		for n in records:
			print("  ",n[0],"    ",n[1],"    ",n[2],"    ",n[3],"    ",n[4],"    ",n[5])
	def getIdLorong(self):
		id_lorong = input("Masukkan Id Lorong : ")
		records = self.__model_jadwal.getIdLorong(id_lorong)
		print("Id Jadwal      Waktu Mulai      Waktu Selesai       Tanggal       Id Lorong    Id Penggunaan")
		for n in records:
			print("  ",n[0],"    ",n[1],"    ",n[2],"    ",n[3],"    ",n[4],"    ",n[5])
	def getIdPenggunaan(self):
		id_penggunaan = input("Masukkan Id Penggunaan : ")
		records = self.__model_jadwal.getIdPenggunaan(id_penggunaan)
		print("Id Jadwal      Waktu Mulai      Waktu Selesai       Tanggal       Id Lorong    Id Penggunaan")
		for n in records:
			print("  ",n[0],"    ",n[1],"    ",n[2],"    ",n[3],"    ",n[4],"    ",n[5])
	def update(self):
		self.get()
		Tanggal = input("Masukkan Tanggal : ")
		id_lorong = input("Masukkan Id Penghuni : ")
		id_penggunaan = input("Masukkan Id Penggunaan : ")
		return(self.__model_jadwal.update(id_jadwal, tanggal, id_lorong, id_penggunaan))
	# overriding
	def delete(self):
		self.get()
		id_penghuni = input("Masukkan Id Jadwal yg ingin dihapus : ")
		return(self.__model_jadwal.delete(id))
	# overriding
	def close(self):
		self.__model_jadwal.close()