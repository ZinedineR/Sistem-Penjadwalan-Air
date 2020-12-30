import controller

# class main
class main:
	def __init__(self):
		self.penghuni = controller.penghuni()
		self.jadwal = controller.jadwal()
		self.lorong = controller.lorong()
		self.penggunaan = controller.penggunaan()
		self.admin = controller.admin()
		print("Selamat Datang di Sistem Penjadwalan Air Pondok Pesantren Syafiurrahman\n===============================================================")
	def login(self):
		print("\n------------LOGIN------------")
		email = input("Email : ")
		password = input("Password : ")
		self.akunAdmin = self.admin.cekLogin(email, password)
		self.akunPenghuni = self.penghuni.cekLogin(email, password)
		if self.akunAdmin == 0 and self.akunPenghuni == 0:
			print("Email atau Password Salah!")
			self.selesaiAdmin()
		elif self.akunAdmin == 0:
			self.mainMenu()
		else:
			self.mainMenu()
	def mainMenu(self):
		print("\n---------------------------")
		print("MENU UTAMA\n1. Penjadwalan Air\n2. Penghuni\n3. Lorong\n4. Penggunaan Air\n5. Admin\n6. Keluar")
		pilihMenu = int(input("Pilih : "))
		if pilihMenu == 1:
			self.penjadwalanMenu()
		elif pilihMenu == 2:
			self.penghuniMenu()
		elif pilihMenu == 3:
			self.lorongMenu()
		elif pilihMenu == 4:
			self.penggunaanMenu()
		elif pilihMenu == 5:
			self.adminMenu()
		elif pilihMenu == 6:
			print("Anda Telah Keluar")
			self.selesaiAdmin()
		else:
			print("PILIHAN SALAH")
			self.mainMenu()
	def penjadwalanMenu(self):
		print("\n---------------------------")
		print("MENU PENJADWALAN AIR\n1. Lihat Semua Jadwal\n2. Lihat Jadwal berdasarkan Id Jadwal\n3. Lihat Jadwal berdasarkan Id Penghuni\n4. Lihat Jadwal berdasarkan Id Lorong\n5. Lihat Jadwal berdasarkan Tanggal\n6. Lihat Jadwal berdasarkan Waktu Mulai\n7. Tulis Jadwal Baru\n8. Ubah Jadwal\n9. Hapus Jadwal\n10. Kembali\n11. Keluar")
		pilihMenu = int(input("Pilih : "))
		if pilihMenu == 1:
			self.jadwal.get()
			self.penjadwalanEndMenu()
		elif pilihMenu == 2:
			self.jadwal.getId()
			self.penjadwalanEndMenu()
		elif pilihMenu == 3:
			self.jadwal.getIdPenghuni()
			self.penjadwalanEndMenu()
		elif pilihMenu == 4:
			self.jadwal.getIdLorong()
			self.penjadwalanEndMenu()
		elif pilihMenu == 5:
			self.jadwal.getTanggal()
			self.penjadwalanEndMenu()
		elif pilihMenu == 6:
			self.jadwal.getWaktuMulai()
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
			print("Anda Telah Keluar")
			self.selesaiPenjadwalan()
		else:
			print("PILIHAN SALAH")
			self.penjadwalanMenu()
	def penghuniMenu(self):
		print("\n---------------------------")
		print("MENU PENGHUNI\n1. Lihat Semua Penghuni\n2. Lihat Penghuni berdasarkan Id Penghuni\n3. Lihat Penghuni berdasarkan Nama Penghuni\n4. Lihat Penghuni berdasarkan Semester\n5. Tulis Penghuni Baru\n6. Ubah Penghuni\n7. Hapus Penghuni\n8. Kembali\n9. Keluar")
		pilihMenu = int(input("Pilih : "))
		if pilihMenu == 1:
			self.penghuni.get()
			self.penghuniEndMenu()
		elif pilihMenu == 2:
			self.penghuni.getId()
			self.penghuniEndMenu()
		elif pilihMenu == 3:
			self.penghuni.getNama()
			self.penghuniEndMenu()
		elif pilihMenu == 4:
			self.penghuni.getSemester()
			self.penghuniEndMenu()
		elif pilihMenu == 5:
			print(self.penghuni.insert())
			self.penghuniEndMenu()
		elif pilihMenu == 6:
			print(self.penghuni.update())
			self.penghuniEndMenu()
		elif pilihMenu == 7:
			print(self.penghuni.delete())
			self.penghuniEndMenu()
		elif pilihMenu == 8:
			self.mainMenu()
		elif pilihMenu == 9:
			print("Anda Keluar")
			self.selesaiPenghuni()
		else:
			print("PILIHAN SALAH")
			self.penghuniMenu()
	def lorongMenu(self):
		print("\n---------------------------")
		print("MENU LORONG\n1. Lihat Semua Lorong\n2. Lihat Lorong berdasarkan Id Lorong\n3. Lihat Lorong berdasarkan Nama Lorong\n4. Tulis Lorong Baru\n5. Ubah Lorong\n6. Hapus Lorong\n7. Kembali\n8. Keluar")
		pilihMenu = int(input("Pilih : "))
		if pilihMenu == 1:
			self.lorong.get()
			self.lorongEndMenu()
		elif pilihMenu == 2:
			self.lorong.getId()
			self.lorongEndMenu()
		elif pilihMenu == 3:
			self.lorong.getNama()
			self.lorongEndMenu()
		elif pilihMenu == 4:
			print(self.lorong.insert())
			self.lorongEndMenu()
		elif pilihMenu == 5:
			print(self.lorong.update())
			self.lorongEndMenu()
		elif pilihMenu == 6:
			print(self.lorong.delete())
			self.lorongEndMenu()
		elif pilihMenu == 7:
			self.mainMenu()
		elif pilihMenu == 8:
			print("Anda Keluar")
			self.selesaiLorong()
		else:
			print("PILIHAN SALAH")
			self.lorongMenu()
	def penggunaanMenu(self):
		print("\n---------------------------")
		print("MENU PENGGUNAAN AIR\n1. Lihat Semua Penggunaan\n2. Lihat Penggunaan berdasarkan Id Penggunaan\n3. Lihat Penggunaan berdasarkan Deskripsi\n5. Tulis Penggunaan Baru\n6. Ubah Penggunaan\n7. Hapus Penggunaan\n8. Kembali\n9. Keluar")
		pilihMenu = int(input("Pilih : "))
		if pilihMenu == 1:
			self.penggunaan.get()
			self.penggunaanEndMenu()
		elif pilihMenu == 2:
			self.penggunaan.getId()
			self.penggunaanEndMenu()
		elif pilihMenu == 3:
			self.penggunaan.getNama()
			self.penggunaanEndMenu()
		elif pilihMenu == 4:
			print(self.penggunaan.insert())
			self.penggunaanEndMenu()
		elif pilihMenu == 5:
			print(self.penggunaan.update())
			self.penggunaanEndMenu()
		elif pilihMenu == 6:
			print(self.penggunaan.delete())
			self.penggunaanEndMenu()
		elif pilihMenu == 7:
			self.mainMenu()
		elif pilihMenu == 8:
			print("Anda Keluar")
			self.selesaiPenggunaan()
		else:
			print("PILIHAN SALAH")
			self.penggunaanMenu()
	def adminMenu(self):
		print("\n---------------------------")
		print("MENU ADMIN\n1. Lihat Semua Admin\n2. Lihat Admin berdasarkan Id Admin\n3. Lihat Admin berdasarkan Email\n4. Tulis Admin Baru\n5. Ubah Admin\n6. Hapus Admin\n7. Kembali\n8. Keluar")
		pilihMenu = int(input("Pilih : "))
		if pilihMenu == 1:
			self.admin.get()
			self.adminEndMenu()
		elif pilihMenu == 2:
			self.admin.getId()
			self.adminEndMenu()
		elif pilihMenu == 3:
			self.admin.getEmail()
			self.adminEndMenu()
		elif pilihMenu == 4:
			print(self.admin.insert())
			self.adminEndMenu()
		elif pilihMenu == 5:
			print(self.admin.update())
			self.adminEndMenu()
		elif pilihMenu == 6:
			print(self.admin.delete())
			self.adminEndMenu()
		elif pilihMenu == 7:
			self.mainMenu()
		elif pilihMenu == 8:
			print("Anda Keluar")
			self.selesaiAdmin()
		else:
			print("PILIHAN SALAH")
			self.adminMenu()
	def penjadwalanEndMenu(self):
		print("\n--------")
		print("MENU\n1. Kembali\n2. Keluar")
		pilih = int(input("Pilih : "))
		if pilih == 1:
			self.penjadwalanMenu()
		elif pilih == 2:
			print("Anda Keluar")
			self.selesaiPenjadwalan()
		else:
			print("Pilihan Salah, Anda Keluar")
			self.selesaiPenjadwalan()
	def penghuniEndMenu(self):
		print("\n--------")
		print("MENU\n1. Kembali\n2. Keluar")
		pilih = int(input("Pilih : "))
		if pilih == 1:
			self.penghuniMenu()
		elif pilih == 2:
			print("Anda Keluar")
			self.selesaiPenghuni()
		else:
			print("Pilihan Salah, Anda Keluar")
			self.selesaiPenghuni()
	def lorongEndMenu(self):
		print("\n--------")
		print("MENU\n1. Kembali\n2. Keluar")
		pilih = int(input("Pilih : "))
		if pilih == 1:
			self.lorongMenu()
		elif pilih == 2:
			print("Anda Keluar")
			self.selesaiLorong()
		else:
			print("Pilihan Salah, Anda Keluar")
			self.selesaiLorong()
	def penggunaanEndMenu(self):
		print("\n--------")
		print("MENU\n1. Kembali\n2. Keluar")
		pilih = int(input("Pilih : "))
		if pilih == 1:
			self.penggunaanMenu()
		elif pilih == 2:
			print("Anda Keluar")
			self.selesaiPenggunaan()
		else:
			print("Pilihan Salah, Anda Keluar")
			self.selesaiPenggunaan()
	def adminEndMenu(self):
		print("\n--------")
		print("MENU\n1. Kembali\n2. Keluar")
		pilih = int(input("Pilih : "))
		if pilih == 1:
			self.adminMenu()
		elif pilih == 2:
			print("Anda Keluar")
			self.selesaiAdmin()
		else:
			print("Pilihan Salah, Anda Keluar")
			self.selesaiAdmin()
	def selesaiPenjadwalan(self):
		self.jadwal.close()
		exit()
	def selesaiPenghuni(self):
		self.penghuni.close()
		exit()
	def selesaiLorong(self):
		self.lorong.close()
		exit()
	def selesaiPenggunaan(self):
		self.penggunaan.close()
		exit()
	def selesaiAdmin(self):
		self.admin.close()
		exit()


main = main()
main.mainMenu()