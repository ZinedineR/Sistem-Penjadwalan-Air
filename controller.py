import model

# class abstract controller
class controller:
	def insert(self):
		pass
	def get(self):
		pass
	def getId(self):
		pass
	def delete(self):
		pass
	def close(self):
		pass

# class astri
class astri(controller):
	def __init__(self):
		self.model_astri = model.modelAstri()
	# overriding
	def insert(self):
		nama = input("Masukkan Nama Astri : ")
		semester = input("Masukkan Semester Astri : ")
		return(self.model_astri.insert(nama, semester))
	# overriding
	def get(self):
		records = self.model_astri.get()
		print("Id Astri     Nama     Semester")
		for n in records:
			print("  ",n[0],"    ",n[1],"    ",n[2])
	# overriding
	def getId(self):
		id_astri = input("Masukkan Id Astri : ")
		records = self.model_astri.getId(id_astri)
		print("Id Astri     Nama     Semester")
		for n in records:
			print("  ",n[0],"    ",n[1],"    ",n[2])
	def getNama(self):
		nama = input("Masukkan Nama Astri : ")
		records = self.model_astri.getNama(nama)
		print("Id Astri     Nama     Semester")
		for n in records:
			print("  ",n[0],"    ",n[1],"    ",n[2])
	def getSemester(self):
		semester = input("Masukkan Semester Astri : ")
		records = self.model_astri.getSemester(semester)
		print("Id Astri     Nama     Semester")
		for n in records:
			print("  ",n[0],"    ",n[1],"    ",n[2])
	def update(self, id_astri, nama, semester):
		id_astri = input("Masukkan Id Astri : ")
		nama = input("Masukkan Nama Astri : ")
		semester = input("Masukkan Semester Astri : ")
		return(self.model_astri.update(id_astri, nama, semester))
	# overriding
	def delete(self):
		id_astri = input("Masukkan Id Astri yg ingin dihapus : ")
		return(self.model_astri.delete(id_astri))
	# overriding
	def close(self):
		self.model_astri.close()

# class jadwal
class jadwal(controller):
	def __init__(self):
		self.model_jadwal = model.modelJadwal()
	# overriding
	def insert(self):
		hari = input("Masukkan Hari : ")
		tanggal = input("Masukkan Tanggal : ")
		kegiatan = input("Masukkan Kegiatan : ")
		id_astri = input("Masukkan Id Astri : ")
		return(self.model_jadwal.insert(hari, tanggal, kegiatan, id_astri))
	# overriding
	def get(self):
		records = self.model_jadwal.get()
		print("Id Jadwal      Hari      Tanggal       Kegiatan       Id Astri")
		for n in records:
			print("  ",n[0],"    ",n[1],"    ",n[2],"    ",n[3],"    ",n[4])
	# overriding
	def getId(self):
		id_jadwal = input("Masukkan Id Jadwal : ")
		records = self.model_jadwal.getId(id_jadwal)
		print("Id Jadwal      Hari      Tanggal       Kegiatan       Id Astri")
		for n in records:
			print("  ",n[0],"    ",n[1],"    ",n[2],"    ",n[3],"    ",n[4])
	def getHari(self):
		hari = input("Masukkan Hari : ")
		records = self.model_jadwal.getHari(hari)
		print("Id Jadwal      Hari      Tanggal       Kegiatan       Id Astri")
		for n in records:
			print("  ",n[0],"    ",n[1],"    ",n[2],"    ",n[3],"    ",n[4])
	def getTanggal(self):
		tanggal = input("Masukkan Tanggal : ")
		records = self.model_jadwal.getTanggal(tanggal)
		print("Id Jadwal      Hari      Tanggal       Kegiatan       Id Astri")
		for n in records:
			print("  ",n[0],"    ",n[1],"    ",n[2],"    ",n[3],"    ",n[4])
	def getKegiatan(self):
		kegiatan = input("Masukkan Kegiatan : ")
		records = self.model_jadwal.getKegiatan(kegiatan)
		print("Id Jadwal      Hari      Tanggal       Kegiatan       Id Astri")
		for n in records:
			print("  ",n[0],"    ",n[1],"    ",n[2],"    ",n[3],"    ",n[4])
	def getIdAstri(self):
		id_astri = input("Masukkan Id Astri : ")
		records = self.model_jadwal.getIdAstri(id_astri)
		print("Id Jadwal      Hari      Tanggal       Kegiatan       Id Astri")
		for n in records:
			print("  ",n[0],"    ",n[1],"    ",n[2],"    ",n[3],"    ",n[4])
	def update(self, id_jadwal, hari, tanggal, kegiatan, id_astri):
		id_jadwal = input("Masukkan Id Jadwal : ")
		hari = input("Masukkan Hari : ")
		tanggal = input("Masukkan Tanggal : ")
		kegiatan = input("Masukkan Kegiatan : ")
		id_astri = input("Masukkan Id Astri : ")
		return(self.model_jadwal.update(id_astri, nama, semester))
	# overriding
	def delete(self):
		id_astri = input("Masukkan Id Jadwal yg ingin dihapus : ")
		return(self.model_jadwal.delete(id))
	# overriding
	def close(self):
		self.model_jadwal.close()