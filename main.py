from Post import userview

class main:
    def __init__(self):
        print("Selamat Datang di Sistem Penjadwalan Air Astri Pondok Pesantren \n===============================================================")
    def mainmenu(self):
        print("Program Sistem Penjadwalan Air")
        print("""
        1. Jadwal Penggunaan
        2. Tangki
        3. Penggunaan
        4. Exit
        """)
        inputan = int(input("Masukan Pilihan : "))
        if  inputan == 1:
            self.menujadwal()
        elif  inputan == 2:
            self.menutangki()
        elif  inputan == 3:
            self.menupenggunaan()
        elif  inputan == 4:
            exit()
            
    def menujadwal(self):
        print("Menu Jadwal")
        print("""
        1. Lihat Penjadwalan Air
        2. Penambahan Jadwal Penggunaan Air
        3. Kembali menu awal
        """)
        inputan = int(input("Masukan Pilihan : "))
        if inputan == 1:
            userview.showJadwal()
            print("Program selesai, kembali ke menu sebelumnya")
            self.menujadwal()
        elif inputan == 2:
            userview.insertJadwal()
            print("Program selesai, kembali ke menu sebelumnya")
            self.menujadwal()
        elif inputan == 3:
            self.mainmenu()
        else:
            print("Anda salah input, kembali lagi ke program jadwal")
            self.mainmenu()
        
    def menutangki(self):
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
            self.menutangki()
        elif inputan == 2:
            userview.updateTangki()
            print("Program selesai, kembali ke menu sebelumnya")
            self.menutangki()
        elif inputan == 3:
            userview.showHistoryTangki()
            print("Program selesai, kembali ke menu sebelumnya")
            self.menutangki()
        elif inputan == 4:
            self.mainmenu()
        else:
            print("Anda salah input, kembali lagi ke program jadwal")
            self.mainmenu()    
        
    def menupenggunaan(self):
        print("Menu Penggunaan")
        print("""
        1. Lihat Penggunaan
        2. Penambahan Penggunaan
        3. Kembali menu awal
        """)
        inputan = int(input("Masukan Pilihan : "))
        if inputan == 1:
            userview.showPenggunaan()
            print("Program selesai, kembali ke menu sebelumnya")
            self.menupenggunaan()
        elif inputan == 2:
            userview.insertPenggunaan()
            print("Program selesai, kembali ke menu sebelumnya")
            self.menupenggunaan()
        elif inputan == 3:
            self.mainmenu()
        else:
            print("Anda salah input, kembali lagi ke program jadwal")
            self.mainmenu()

main = main()
main.mainmenu()







