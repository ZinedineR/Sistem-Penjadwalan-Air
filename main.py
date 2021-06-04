from Post import userview, saving
import gui
import wx
#halaman awal
class thegui(gui.loginPage):
    def __init__(self, parent):
        gui.loginPage.__init__(self, parent)
        self.Show()
    
    def clickLogin(self, event):
        # pwd = str(self.text_password.GetValue())
        pwd = self.text_password.GetValue()
        if pwd == "root":
            adminMenuFrame = adminGui(None)
            adminMenuFrame.Show()
            self.Hide()
    
    def userClickLogin(self, event):
        self.Hide()
        userMenuFrame = userGui(None)
        userMenuFrame.Show()
                                     
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
        for row in range(len(data)):
            for col in range(len(data[row])):
                self.m_grid6.SetCellValue(row,col,str(data[row][col]))
        self.Show()
    def clickKembali(self, event):
        self.Hide()
        JadwalPenggunaanFrame = adminJadwalPenggunaan(None)
        JadwalPenggunaanFrame.Show()
class admintambahPenjadwalanAirone(gui.tambahPenjadwalanAirone):
    def __init__(self, parent):
        gui.tambahPenjadwalanAirone.__init__(self, parent)
        data = userview.showTangki()
        for row in range(len(data)):
            for col in range(len(data[row])):
                self.m_grid4.SetCellValue(row,col,str(data[row][col]))
        self.Show()
    def clickSelanjutnya(self, event):
        idtangki = int(self.m_textCtrl4.GetValue())
        saving(int(idtangki))
        self.Hide()
        tambahPenjadwalanAirtwoFrame = admintambahPenjadwalanAirtwo(None)
        tambahPenjadwalanAirtwoFrame.Show()
class admintambahPenjadwalanAirtwo(gui.tambahPenjadwalanAirtwo):
    def __init__(self, parent):
        gui.tambahPenjadwalanAirtwo.__init__(self, parent)
        data = userview.showKategori()
        for row in range(len(data)):
            for col in range(len(data[row])):
                self.m_grid3.SetCellValue(row,col,str(data[row][col]))
        self.Show()
    def clickSelanjutnya(self, event):
        idkategori = int(self.m_textCtrl3.GetValue())
        saving(int(idkategori))
        self.Hide()
        tambahPenjadwalanAirthreeFrame = admintambahPenjadwalanAirthree(None)
        tambahPenjadwalanAirthreeFrame.Show()
class admintambahPenjadwalanAirthree(gui.tambahPenjadwalanAirthree):
    def __init__(self, parent):
        gui.tambahPenjadwalanAirthree.__init__(self, parent)
        data = userview.showIDLorong()
        for row in range(len(data)):
            for col in range(len(data[row])):
                self.m_grid5.SetCellValue(row,col,str(data[row][col]))
        self.Show()
    def clickSelesai(self, event):
        idlorong = int(self.m_textCtrl4.GetValue())
        saving(int(idlorong))
        saving('date()')
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
        data = userview.showTangki()
        for row in range(len(data)):
            for col in range(len(data[row])):
                self.m_grid3.SetCellValue(row,col,str(data[row][col]))
        self.Show()
    def clickKembali(self, event):
        self.Hide()
        menuTangkiFrame = adminmenuTangki(None)
        menuTangkiFrame.Show()
class adminpengisianpenguranganLiter(gui.pengisianpenguranganLiter):
    def __init__(self, parent):
        gui.pengisianpenguranganLiter.__init__(self, parent)
        data = userview.showTangki()
        for row in range(len(data)):
            for col in range(len(data[row])):
                self.m_grid7.SetCellValue(row,col,str(data[row][col]))
        self.Show()
    def clickSelesai(self, event):
        idtangki = int(self.m_textCtrl5.GetValue())
        liter = int(self.m_textCtrl6.GetValue())
        saving(idtangki)
        saving(liter)
        self.Hide()   
        userview.updateTangki()
        lihatTangkiFrame = adminlihatTangki(None)
        lihatTangkiFrame.Show()
class adminHistoryTangki(gui.HistoryTangki):
    def __init__(self, parent):
        gui.HistoryTangki.__init__(self, parent)
        data = userview.showHistoryTangki()
        for row in range(len(data)):
            for col in range(len(data[row])):
                self.m_grid8.SetCellValue(row,col,str(data[row][col]))
        self.Show()
    def clickKembali(self, event):
        self.Hide()
        menuTangkiFrame = adminmenuTangki(None)
        menuTangkiFrame.Show()                                  
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
        data = userview.showLorong()
        for row in range(len(data)):
            for col in range(len(data[row])):
                self.m_grid10.SetCellValue(row,col,str(data[row][col]))
        self.Show()
    def clickKembali(self, event):
        self.Hide()
        lorongPageFrame = adminlorongPage(None)
        lorongPageFrame.Show()
class adminpenambahanPenghunione(gui.penambahanPenghunione):
    def __init__(self, parent):
        gui.penambahanPenghunione.__init__(self, parent)
        data = userview.showIDLorong()
        for row in range(len(data)):
            for col in range(len(data[row])):
                self.m_grid11.SetCellValue(row,col,str(data[row][col]))
        self.Show()
    def clickSelanjutnya(self, event):
        idlorong = int(self.m_textCtrl7.GetValue())
        saving(idlorong)
        self.Hide()
        adminpenambahanPenghunitwoFrame = adminpenambahanPenghunitwo(None)
        adminpenambahanPenghunitwoFrame.Show()        
class adminpenambahanPenghunitwo(gui.penambahanPenghunitwo):
    def __init__(self, parent):
        gui.penambahanPenghunitwo.__init__(self, parent)
        data = userview.showPenghuni()
        for row in range(len(data)):
            for col in range(len(data[row])):
                self.m_grid12.SetCellValue(row,col,str(data[row][col]))
        self.Show()
    def clickSelesai(self, event):
        idpenghuni = int(self.m_textCtrl8.GetValue())
        saving(idpenghuni)
        saving('pass')
        self.Hide()   
        userview.insertLorong()
        lihatLorongFrame = adminlihatLorong(None)
        lihatLorongFrame.Show()                
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
        data = userview.showPenghuni()
        for row in range(len(data)):
            for col in range(len(data[row])):
                self.m_grid13.SetCellValue(row,col,str(data[row][col]))
        self.Show()
    def clickKembali(self, event):
        self.Hide()
        penghuniPageFrame = adminpenghuniPage(None)
        penghuniPageFrame.Show()        
class adminpenambahanPenghuni(gui.penambahanPenghuni):
    def __init__(self, parent):
        gui.penambahanPenghuni.__init__(self, parent)
        self.Show()
    def clickSelesai(self, event):
        namapenghuni = str(self.m_textCtrl9.GetValue())
        saving(namapenghuni)
        self.Hide()   
        userview.insertPenghuni()
        lihatPenghuniFrame = adminlihatPenghuni(None)
        lihatPenghuniFrame.Show() 

#halaman awal user
class userGui(gui.userMenu):
    def __init__(self, parent):
        gui.userMenu.__init__(self, parent)
        self.Show()

    def ClickLihatPenggunaan(self, event):
        self.Hide()
        lihatPenggunaanFrame = userlihatPenggunaan(None)
        lihatPenggunaanFrame.Show()
    
    def ClickLihatJadwal(self, event):
        self.Hide()
        lihatJadwalFrame = userlihatJadwal(None)
        lihatJadwalFrame.Show()
        
    def ClickTambahPenggunaan(self, event):
        self.Hide()
        penambahanPenggunaanoneFrame = userpenambahanPenggunaanone(None)
        penambahanPenggunaanoneFrame.Show()
class userlihatPenggunaan(gui.lihatPenggunaan):
    def __init__(self, parent):
        gui.lihatPenggunaan.__init__(self, parent)
        data = userview.showviewPenggunaan()
        for row in range(len(data)):
            for col in range(len(data[row])):
                self.m_grid14.SetCellValue(row,col,str(data[row][col]))
        self.Show()
    def clickKembali(self, event):
        self.Hide()
        userMenuFrame = userGui(None)
        userMenuFrame.Show()
class userlihatJadwal(gui.lihatJadwal):
    def __init__(self, parent):
        gui.lihatJadwal.__init__(self, parent)
        data = userview.showviewJadwal()
        for row in range(len(data)):
            for col in range(len(data[row])):
                self.m_grid15.SetCellValue(row,col,str(data[row][col]))
        self.Show()
    def clickKembali(self, event):
        self.Hide()
        userMenuFrame = userGui(None)
        userMenuFrame.Show()
class userpenambahanPenggunaanone(gui.penambahanPenggunaanone):
    def __init__(self, parent):
        gui.penambahanPenggunaanone.__init__(self, parent)
        data = userview.showPenghuni()
        for row in range(len(data)):
            for col in range(len(data[row])):
                self.m_grid16.SetCellValue(row,col,str(data[row][col]))
        self.Show()
    def clickSelanjutnya(self, event):
        idpengguna = int(self.m_textCtrl10.GetValue())
        saving(idpengguna)
        self.Hide()
        penambahanPenggunaantwoFrame = userpenambahanPenggunaantwo(None)
        penambahanPenggunaantwoFrame.Show()
class userpenambahanPenggunaantwo(gui.penambahanPenggunaantwo):
    def __init__(self, parent):
        gui.penambahanPenggunaantwo.__init__(self, parent)
        data = userview.showKategori()
        for row in range(len(data)):
            for col in range(len(data[row])):
                self.m_grid17.SetCellValue(row,col,str(data[row][col]))
        self.Show()
    def clickSelesai(self, event):
        idkategori = int(self.m_textCtrl11.GetValue())
        saving(idkategori)
        saving('date()')
        self.Hide()
        userview.insertPenggunaan()
        lihatPenggunaanFrame = userlihatPenggunaan(None)
        lihatPenggunaanFrame.Show()                 
app = wx.App()
loginframe = thegui(None)
loginframe.Show()
app.MainLoop()