import controller

# class main
class main:
	def __init__(self):
		self.astri = controller.astri()
		self.jadwal = controller.jadwal()
		print("Selamat Datang di Sistem Penjadwalan Air Astri Pondok Pesantren \n===============================================================")
	def mainMenu(self):
		print("\n---------------------------")
		print("MENU UTAMA\n1. Penjadwalan Air\n2. Biodata Astri\n3. Selesai")
		pilihMenu = int(input("Pilih : "))
		if pilihMenu == 1:
			self.penjadwalanMenu()
		elif pilihMenu == 2:
			self.astriMenu()
		elif pilihMenu == 3:
			print("Terima Kasih...")
			exit()
		else:
			print("PILIHAN SALAH")
			self.mainMenu()
	def penjadwalanMenu(self):
		print("\n---------------------------")
		print("MENU PENJADWALAN AIR\n1. Lihat Semua Jadwal\n2. Lihat Jadwal berdasarkan Id Jadwal\n3. Lihat Jadwal berdasarkan Id Astri\n4. Lihat Jadwal berdasarkan Hari\n5. Lihat Jadwal berdasarkan Tanggal\n6. Lihat Jadwal berdasarkan Kegiatan\n7. Tulis Jadwal\n8. Ubah Jadwal\n9. Hapus Jadwal\n10. Kembali\n11. Selesai")
		pilihMenu = int(input("Pilih : "))
		if pilihMenu == 1:
			self.jadwal.get()
			self.penjadwalanEndMenu()
		elif pilihMenu == 2:
			self.jadwal.getId()
			self.penjadwalanEndMenu()
		elif pilihMenu == 3:
			self.jadwal.getIdAstri()
			self.penjadwalanEndMenu()
		elif pilihMenu == 4:
			self.jadwal.getHari()
			self.penjadwalanEndMenu()
		elif pilihMenu == 5:
			self.jadwal.getTanggal()
			self.penjadwalanEndMenu()
		elif pilihMenu == 6:
			self.jadwal.getKegiatan()
			self.penjadwalanEndMenu()
		elif pilihMenu == 7:
			print(self.jadwal.insert())
			self.penjadwalanEndMenu()
		elif pilihMenu == 8:
			print(self.jadwal.update())
			self.penjadwalanEndMenu()
		elif pilihMenu == 9:
			print(self.jadwal.delete())
			self.penjadwalanEndMenu()
		elif pilihMenu == 10:
			self.mainMenu()
		elif pilihMenu == 11:
			print("Terima Kasih...")
			exit()
		else:
			print("PILIHAN SALAH")
			self.penjadwalanMenu()
	def astriMenu(self):
		print("\n---------------------------")
		print("MENU BIODATA ASTRI\n1. Lihat Semua Astri\n2. Lihat Astri berdasarkan Id Astri\n3. Lihat Astri berdasarkan Nama Astri\n4. Lihat Astri berdasarkan Semester\n5. Tulis Astri\n6. Ubah Astri\n7. Hapus Astri\n8. Kembali\n9. Selesai")
		pilihMenu = int(input("Pilih : "))
		if pilihMenu == 1:
			self.astri.get()
			self.astriEndMenu()
		elif pilihMenu == 2:
			self.astri.getId()
			self.astriEndMenu()
		elif pilihMenu == 3:
			self.astri.getNama()
			self.astriEndMenu()
		elif pilihMenu == 4:
			self.astri.getSemester()
			self.astriEndMenu()
		elif pilihMenu == 5:
			print(self.astri.insert())
			self.astriEndMenu()
		elif pilihMenu == 6:
			print(self.astri.update())
			self.astriEndMenu()
		elif pilihMenu == 7:
			print(self.astri.delete())
			self.astriEndMenu()
		elif pilihMenu == 8:
			self.mainMenu()
		elif pilihMenu == 9:
			print("Terima Kasih...")
			exit()
		else:
			print("PILIHAN SALAH")
			self.astriMenu()
	def penjadwalanEndMenu(self):
		print("\n--------")
		print("MENU\n1. Kembali\n2. Selesai")
		pilih = int(input("Pilih : "))
		if pilih == 1:
			self.penjadwalanMenu()
		elif pilih == 2:
			print("Terima Kasih...")
			self.selesaiPenjadwalan()
		else:
			print("Pilihan Salah, Anda Keluar")
			self.selesaiPenjadwalan()
	def astriEndMenu(self):
		print("\n--------")
		print("MENU\n1. Kembali\n2. Selesai")
		pilih = int(input("Pilih : "))
		if pilih == 1:
			self.astriMenu()
		elif pilih == 2:
			print("Terima Kasih...")
			self.selesaiAstri()
		else:
			print("Pilihan Salah, Anda Keluar")
			self.selesaiAstri()
	def selesaiAstri(self):
		self.astri.close()
		exit()
	def selesaiPenjadwalan(self):
		self.jadwal.close()
		exit()


main = main()
main.mainMenu()