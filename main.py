from Post import userview
import gui
import wx
saver =[]
#halaman awal
class thegui(gui.loginPage):
    def __init__(self, parent):
        gui.loginPage.__init__(self, parent)
        self.Show()
    
    def clickLogin(self, event):
        # pwd = str(self.text_password.GetValue())
        pwd = self.text_password.GetValue()
        print(pwd)
        if pwd == "root":
            adminMenuFrame = adminGui(None)
            adminMenuFrame.Show()
            self.Hide()
    
    def userClickLogin(self, event):
        self.Hide()
        adminMenuFrame = adminGui(None)
        adminMenuFrame.Show()

#halaman awal admin       
class adminGui(gui.adminMenu):
    def __init__(self, parent):
        gui.adminMenu.__init__(self, parent)
        self.Show()
        
    def clickJadwalPenggunaan(self, event):
        self.Hide()
        JadwalPenggunaanFrame = adminJadwalPenggunaan(None)
        JadwalPenggunaanFrame.Show()
    
    def clickTangki(self, event):
        self.Hide()
        menuTangkiFrame = adminmenuTangki(None)
        menuTangkiFrame.Show()
        
    def clickLorong(self, event):
        self.Hide()
        lorongPageFrame = adminlorongPage(None)
        lorongPageFrame.Show()
        
    def clickPenghuni(self, event):
        self.Hide()
        penghuniPageFrame = adminpenghuniPage(None)
        penghuniPageFrame.Show()
#halaman admin Jadwal Penggunaan         
class adminJadwalPenggunaan(gui.JadwalPenggunaan):
    def __init__(self, parent):
        gui.JadwalPenggunaan.__init__(self, parent)
        self.Show()
    def clickLihat(self, event):
        self.Hide()
        lihatPenjadwalanAirFrame = adminlihatPenjadwalanAir(None)
        lihatPenjadwalanAirFrame.Show()
    def clickTambah(self, event):
        self.Hide()
        tambahPenjadwalanAironeFrame = admintambahPenjadwalanAirone(None)
        tambahPenjadwalanAironeFrame.Show()
    def clickKembali(self, event):
        self.Hide()
        adminMenuFrame = adminGui(None)
        adminMenuFrame.Show()    
class adminlihatPenjadwalanAir(gui.lihatPenjadwalanAir):
    def __init__(self, parent):
        gui.lihatPenjadwalanAir.__init__(self, parent)
        data = userview.showviewJadwal()
        for n in range(len(data)):
            for i in range(len(data[n])):
                self.m_grid6.SetCellValue(n,i,str(data[n][i]))
        self.Show()
    def clickKembali(self, event):
        self.Hide()
        JadwalPenggunaanFrame = adminJadwalPenggunaan(None)
        JadwalPenggunaanFrame.Show()
class admintambahPenjadwalanAirone(gui.tambahPenjadwalanAirone):
    def __init__(self, parent):
        gui.tambahPenjadwalanAirone.__init__(self, parent)
        data = userview.showTangki()
        for n in range(len(data)):
            for i in range(len(data[n])):
                self.m_grid4.SetCellValue(n,i,str(data[n][i]))
        self.Show()
    def clickSelanjutnya(self, event):
        idtangki = int(self.m_textCtrl4.GetValue())
        saver.append(int(idtangki))
        self.Hide()
        tambahPenjadwalanAirtwoFrame = admintambahPenjadwalanAirtwo(None)
        tambahPenjadwalanAirtwoFrame.Show()
class admintambahPenjadwalanAirtwo(gui.tambahPenjadwalanAirtwo):
    def __init__(self, parent):
        gui.tambahPenjadwalanAirtwo.__init__(self, parent)
        data = userview.showKategori()
        for n in range(len(data)):
            for i in range(len(data[n])):
                self.m_grid3.SetCellValue(n,i,str(data[n][i]))
        self.Show()
    def clickSelanjutnya(self, event):
        idkategori = int(self.m_textCtrl3.GetValue())
        saver.append(int(idkategori))
        self.Hide()
        tambahPenjadwalanAirthreeFrame = admintambahPenjadwalanAirthree(None)
        tambahPenjadwalanAirthreeFrame.Show()
class admintambahPenjadwalanAirthree(gui.tambahPenjadwalanAirthree):
    def __init__(self, parent):
        gui.tambahPenjadwalanAirthree.__init__(self, parent)
        data = userview.showIDLorong()
        for n in range(len(data)):
            for i in range(len(data[n])):
                self.m_grid5.SetCellValue(n,i,str(data[n][i]))
        self.Show()
    def clickSelesai(self, event):
        idlorong = int(self.m_textCtrl4.GetValue())
        saver.append(int(idlorong))
        saver.append('date()')
        self.Hide()   
        userview.insertJadwal()
        lihatPenjadwalanAirFrame = adminlihatPenjadwalanAir(None)
        lihatPenjadwalanAirFrame.Show()            
#halaman admin Tangki
class adminmenuTangki(gui.menuTangki):
    def __init__(self, parent):
        gui.menuTangki.__init__(self, parent)
        self.Show()
    def clickLihat(self, event):
        self.Hide()
        lihatTangkiFrame = adminlihatTangki(None)
        lihatTangkiFrame.Show()
    def clickCek(self, event):
        self.Hide()
        pengisianpenguranganLiterFrame = adminpengisianpenguranganLiter(None)
        pengisianpenguranganLiterFrame.Show()
    def clickHistori(self, event):
        self.Hide()
        HistoryTangkiFrame = adminHistoryTangki(None)
        HistoryTangkiFrame.Show()    
    def clickKembali(self, event):
        self.Hide()
        adminMenuFrame = adminGui(None)
        adminMenuFrame.Show()
class adminlihatTangki(gui.lihatTangki):
    def __init__(self, parent):
        gui.lihatTangki.__init__(self, parent)
        self.Show()
class adminpengisianpenguranganLiter(gui.pengisianpenguranganLiter):
    def __init__(self, parent):
        gui.pengisianpenguranganLiter.__init__(self, parent)
        self.Show()
class adminHistoryTangki(gui.HistoryTangki):
    def __init__(self, parent):
        gui.HistoryTangki.__init__(self, parent)
        self.Show()                              
#halaman admin lorong page        
class adminlorongPage(gui.lorongPage):
    def __init__(self, parent):
        gui.lorongPage.__init__(self, parent)
        self.Show()
    def clickLihat(self, event):
        self.Hide()
        lihatLorongFrame = adminlihatLorong(None)
        lihatLorongFrame.Show()
    def clickTambah(self, event):
        self.Hide()
        penambahanPenghunioneFrame = adminpenambahanPenghunione(None)
        penambahanPenghunioneFrame.Show()
    def clickKembali(self, event):
        self.Hide()
        adminMenuFrame = adminGui(None)
        adminMenuFrame.Show()
class adminlihatLorong(gui.lihatLorong):
    def __init__(self, parent):
        gui.lihatLorong.__init__(self, parent)
        self.Show()
class adminpenambahanPenghunione(gui.penambahanPenghunione):
    def __init__(self, parent):
        gui.penambahanPenghunione.__init__(self, parent)
        self.Show()
#halaman admin penghuni page       
class adminpenghuniPage(gui.penghuniPage):
    def __init__(self, parent):
        gui.penghuniPage.__init__(self, parent)
        self.Show()
    def clickLihat(self, event):
        self.Hide()
        lihatPenghuniFrame = adminlihatPenghuni(None)
        lihatPenghuniFrame.Show()
    def clickTambah(self, event):
        self.Hide()
        penambahanPenghuniFrame = adminpenambahanPenghuni(None)
        penambahanPenghuniFrame.Show()
    def clickKembali(self, event):
        self.Hide()
        adminMenuFrame = adminGui(None)
        adminMenuFrame.Show()
class adminlihatPenghuni(gui.lihatPenghuni):
    def __init__(self, parent):
        gui.lihatPenghuni.__init__(self, parent)
        self.Show()
class adminpenambahanPenghuni(gui.penambahanPenghuni):
    def __init__(self, parent):
        gui.penambahanPenghuni.__init__(self, parent)
        self.Show()        
app = wx.App()
loginframe = thegui(None)
loginframe.Show()
app.MainLoop()
# class main:
#     def __init__(self):
#         print("Selamat Datang di Sistem Penjadwalan Air Astri Pondok Pesantren \n===============================================================")
#     def login(self):
#         print("Silahkan memilih login sebagai apa : ")
#         print("""
#         1. Admin
#         2. User
#         3. Exit
#         """)
#         inputan = int(input("Masukan Pilihan : "))
#         if  inputan == 1:
#             pwd = str(input("masukkan password login sebagai user : "))
#             if pwd == "root":
#                 self.adminmainmenu()
#             else:
#                 print("Anda salah password, kembali ke menu login")
#                 self.login()
#         elif  inputan == 2:
#             self.menuuser()
#         elif  inputan == 3:
#             print("Terima kasih!")
#             return None
#         else:
#             print("Anda memasukkan inputan yang salah, kembali ke menu login")
#             self.login()
        
#     def adminmainmenu(self):
#         print("Program Sistem Penjadwalan Air")
#         print("""
#         1. Jadwal Penggunaan
#         2. Tangki
#         3. lorong
#         4. Penghuni
#         5. Exit
#         """)
#         inputan = int(input("Masukan Pilihan : "))
#         if  inputan == 1:
#             self.menuadminjadwal()
#         elif  inputan == 2:
#             self.menuadmintangki()
#         elif  inputan == 3:
#             self.menuadminlorong()
#         elif  inputan == 4:
#             self.menuadminpenghuni()
#         elif  inputan == 5:
#             print("Terima kasih!")
#             return None
            
#     def menuadminjadwal(self):
#         print("Menu Jadwal")
#         print("""
#         1. Lihat Penjadwalan Air
#         2. Penambahan Jadwal Penggunaan Air
#         3. Kembali menu awal
#         """)
#         inputan = int(input("Masukan Pilihan : "))
#         if inputan == 1:
#             userview.showviewJadwal()
#             print("Program selesai, kembali ke menu sebelumnya")
#             self.menuadminjadwal()
#         elif inputan == 2:
#             userview.insertJadwal()
#             print("Program selesai, kembali ke menu sebelumnya")
#             self.menuadminjadwal()
#         elif inputan == 3:
#             self.adminmainmenu()
#         else:
#             print("Anda salah input, kembali lagi ke program jadwal")
#             self.menuadminjadwal()
        
#     def menuadmintangki(self):
#         print("Menu Tangki")
#         print("""
#         1. Lihat Tangki
#         2. Pengisian/Pengurangan liter tangki
#         3. History Tangki
#         4. Kembali menu awal
#         """)
#         inputan = int(input("Masukan Pilihan : "))
#         if inputan == 1:
#             userview.showTangki()
#             print("Program selesai, kembali ke menu sebelumnya")
#             self.menuadmintangki()
#         elif inputan == 2:
#             userview.updateTangki()
#             print("Program selesai, kembali ke menu sebelumnya")
#             self.menuadmintangki()
#         elif inputan == 3:
#             userview.showHistoryTangki()
#             print("Program selesai, kembali ke menu sebelumnya")
#             self.menuadmintangki()
#         elif inputan == 4:
#             self.adminmainmenu()
#         else:
#             print("Anda salah input, kembali lagi ke program tangki")
#             self.menuadmintangki()   
    
#     def menuadminlorong(self):
#         print("Menu Lorong")
#         print("""
#         1. Lihat Lorong
#         2. Penambahan Penghuni ke Lorong
#         3. Kembali menu awal
#         """)
#         inputan = int(input("Masukan Pilihan : "))
#         if inputan == 1:
#             userview.showLorong()
#             print("Program selesai, kembali ke menu sebelumnya")
#             self.menuadminlorong()
#         elif inputan == 2:
#             userview.insertLorong()
#             print("Program selesai, kembali ke menu sebelumnya")
#             self.menuadminlorong()
#         elif inputan == 3:
#             self.adminmainmenu()
#         else:
#             print("Anda salah input, kembali lagi ke program lorong")
#             self.menuadminlorong()
            
#     def menuadminpenghuni(self):
#         print("Menu Penghuni")
#         print("""
#         1. Lihat Penghuni
#         2. Penambahan Penghuni
#         3. Kembali menu awal
#         """)
#         inputan = int(input("Masukan Pilihan : "))
#         if inputan == 1:
#             userview.showPenghuni()
#             print("Program selesai, kembali ke menu sebelumnya")
#             self.menuadminpenghuni()
#         elif inputan == 2:
#             userview.insertPenghuni()
#             print("Program selesai, kembali ke menu sebelumnya")
#             self.menuadminpenghuni()
#         elif inputan == 3:
#             self.adminmainmenu()
#         else:
#             print("Anda salah input, kembali lagi ke program penghuni")
#             self.menuadminpenghuni()
            
#     def menuuser(self):
#         print("Menu Penggunaan")
#         print("""
#         1. Lihat Penggunaan
#         2. Lihat Jadwal
#         3. Penambahan Penggunaan
#         4. Exit
#         """)
#         inputan = int(input("Masukan Pilihan : "))
#         if inputan == 1:
#             userview.showviewPenggunaan()
#             print("Program selesai, kembali ke menu sebelumnya")
#             self.menuuser()
#         elif inputan == 2:
#             userview.showviewJadwal()
#             print("Program selesai, kembali ke menu sebelumnya")
#             self.menuuser()
#         elif inputan == 3:
#             userview.insertPenggunaan()
#             print("Program selesai, kembali ke menu sebelumnya")
#             self.menuuser()
#         elif inputan == 4:
#             print("Terima Kasih")
#             return None
#         else:
#             print("Anda salah input, kembali lagi ke program penggunaan")
#             self.menuuser()











