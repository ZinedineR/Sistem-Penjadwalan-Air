from Post import userview

class main:
    def __init__(self):
        print("Selamat Datang di Sistem Penjadwalan Air Astri Pondok Pesantren \n===============================================================")
    def login(self):
        print("Silahkan memilih login sebagai apa : ")
        print("""
        1. Admin
        2. User
        3. Exit
        """)
        inputan = int(input("Masukan Pilihan : "))
        if  inputan == 1:
            pwd = str(input("masukkan password login sebagai user : "))
            if pwd == "root":
                self.adminmainmenu()
            else:
                print("Anda salah password, kembali ke menu login")
                self.login()
        elif  inputan == 2:
            self.menuuser()
        elif  inputan == 3:
            print("Terima kasih!")
            return None
        else:
            print("Anda memasukkan inputan yang salah, kembali ke menu login")
            self.login()
        
    def adminmainmenu(self):
        print("Program Sistem Penjadwalan Air")
        print("""
        1. Jadwal Penggunaan
        2. Tangki
        3. lorong
        4. Penghuni
        5. Exit
        """)
        inputan = int(input("Masukan Pilihan : "))
        if  inputan == 1:
            self.menuadminjadwal()
        elif  inputan == 2:
            self.menuadmintangki()
        elif  inputan == 3:
            self.menuadminlorong()
        elif  inputan == 4:
            self.menuadminpenghuni()
        elif  inputan == 5:
            print("Terima kasih!")
            return None
            
    def menuadminjadwal(self):
        print("Menu Jadwal")
        print("""
        1. Lihat Penjadwalan Air
        2. Penambahan Jadwal Penggunaan Air
        3. Kembali menu awal
        """)
        inputan = int(input("Masukan Pilihan : "))
        if inputan == 1:
            userview.showviewJadwal()
            print("Program selesai, kembali ke menu sebelumnya")
            self.menuadminjadwal()
        elif inputan == 2:
            userview.insertJadwal()
            print("Program selesai, kembali ke menu sebelumnya")
            self.menuadminjadwal()
        elif inputan == 3:
            self.adminmainmenu()
        else:
            print("Anda salah input, kembali lagi ke program jadwal")
            self.menuadminjadwal()
        
    def menuadmintangki(self):
        print("Menu Tangki")
        print("""
        1. Lihat Tangki
        2. Pengisian/Pengurangan liter tangki
        3. History Tangki
        4. Kembali menu awal
        """)
        inputan = int(input("Masukan Pilihan : "))
        if inputan == 1:
            userview.showTangki()
            print("Program selesai, kembali ke menu sebelumnya")
            self.menuadmintangki()
        elif inputan == 2:
            userview.updateTangki()
            print("Program selesai, kembali ke menu sebelumnya")
            self.menuadmintangki()
        elif inputan == 3:
            userview.showHistoryTangki()
            print("Program selesai, kembali ke menu sebelumnya")
            self.menuadmintangki()
        elif inputan == 4:
            self.adminmainmenu()
        else:
            print("Anda salah input, kembali lagi ke program tangki")
            self.menuadmintangki()   
    
    def menuadminlorong(self):
        print("Menu Lorong")
        print("""
        1. Lihat Lorong
        2. Penambahan Penghuni ke Lorong
        3. Kembali menu awal
        """)
        inputan = int(input("Masukan Pilihan : "))
        if inputan == 1:
            userview.showLorong()
            print("Program selesai, kembali ke menu sebelumnya")
            self.menuadminlorong()
        elif inputan == 2:
            userview.insertLorong()
            print("Program selesai, kembali ke menu sebelumnya")
            self.menuadminlorong()
        elif inputan == 3:
            self.adminmainmenu()
        else:
            print("Anda salah input, kembali lagi ke program lorong")
            self.menuadminlorong()
            
    def menuadminpenghuni(self):
        print("Menu Penghuni")
        print("""
        1. Lihat Penghuni
        2. Penambahan Penghuni
        3. Kembali menu awal
        """)
        inputan = int(input("Masukan Pilihan : "))
        if inputan == 1:
            userview.showPenghuni()
            print("Program selesai, kembali ke menu sebelumnya")
            self.menuadminpenghuni()
        elif inputan == 2:
            userview.insertPenghuni()
            print("Program selesai, kembali ke menu sebelumnya")
            self.menuadminpenghuni()
        elif inputan == 3:
            self.adminmainmenu()
        else:
            print("Anda salah input, kembali lagi ke program penghuni")
            self.menuadminpenghuni()
            
    def menuuser(self):
        print("Menu Penggunaan")
        print("""
        1. Lihat Penggunaan
        2. Lihat Jadwal
        3. Penambahan Penggunaan
        4. Exit
        """)
        inputan = int(input("Masukan Pilihan : "))
        if inputan == 1:
            userview.showviewPenggunaan()
            print("Program selesai, kembali ke menu sebelumnya")
            self.menuuser()
        elif inputan == 2:
            userview.showviewJadwal()
            print("Program selesai, kembali ke menu sebelumnya")
            self.menuuser()
        elif inputan == 3:
            userview.insertPenggunaan()
            print("Program selesai, kembali ke menu sebelumnya")
            self.menuuser()
        elif inputan == 4:
            print("Terima Kasih")
            return None
        else:
            print("Anda salah input, kembali lagi ke program penggunaan")
            self.menuuser()

main = main()
main.login()







