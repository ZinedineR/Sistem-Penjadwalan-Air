from model import Model
import gui

class jadwal(Model):
    def __init__(self):
        super().__init__("jadwal",["jadwal_id","tangki_id","kategori_id","lorong_id","tangki_tanggal"])
    def fiturjadwal(self):
        super().__init__("jadwal",["tangki_id","kategori_id","lorong_id","tangki_tanggal"])
    def viewjadwal(self):
        super().__init__("viewjadwal",["jadwal_id","tangki_id","lorong_id","penggunaan","tangki_tanggal"])
        
class tangki(Model):
    def __init__(self):
        super().__init__("tangki",["tangki_id","tangki_tanggal","jumlahairliter"])
    def liter(self):
        super().__init__("tangki","jumlahairliter")
    def historytangki(self):
        super().__init__("history_tangki","pass")
        
class penggunaan(Model):
    def __init__(self):
        super().__init__("penggunaan",["penggunaan_id","penghuni_id","kategori_id","tanggal_penggunaan"])
    def fiturpenggunaan(self):
        super().__init__("penggunaan",["penghuni_id","kategori_id","tanggal_penggunaan"])
    def viewpenggunaan(self):
        super().__init__("viewpenggunaan",["penggunaan_id","namapenghuni","penggunaan","tanggal_penggunaan"]) 

class lorong(Model):
    def __init__(self):
        super().__init__("lorong",["lorong_id","penghuni_id","namapenghuni"])
    def orderedlorong(self):
        super().__init__("orderedlorong",["lorong_id","penghuni_id","namapenghuni"])
    def idlorong(self):
        super().__init__("IDLORONG","lorong_id")

class penghuni(Model):
    def __init__(self):
        super().__init__("penghuni",["penghuni_id","namapenghuni"])
    def fiturpenghuni(self):
        super().__init__("penghuni","namapenghuni")

class kategori(Model):
    def __init__(self):
        super().__init__("kategori",["kategori_id","deskripsi"])

global saver
saver = []            
def saving(data):
    saver.append(data)
    return saver
def delete():
    saver.clear()
    return saver

class userview():
    def showKategori():
        model = kategori()
        data = model.view()
        return data
    
    def showPenghuni():
        model = penghuni()
        data = model.view()
        return data
            
    def showLorong():
        model = lorong()
        model.orderedlorong()
        data = model.view()
        return data
    
    def showIDLorong():
        model = lorong()
        model.idlorong()
        data = model.view()
        return data
            
    def showTangki():
        model = tangki()
        data = model.view()
        return data
    
    def showHistoryTangki():
        model = tangki()
        model.historytangki()
        data = model.view()
        return data
            
    def showviewPenggunaan():
        model = penggunaan()
        model.viewpenggunaan()
        data = model.view()
        return data
            
    def showviewJadwal():
        model = jadwal()
        model.viewjadwal()
        data = model.view()
        return data       
   
    def updateTangki():
        model = tangki()
        model.liter()
        userview.showTangki()
        wherekey = "tangki_id"
        model.update(saver[1],wherekey,saver[0])
        delete()
        
    def insertPenggunaan():
        model = penggunaan()
        model.fiturpenggunaan()
        model.insert(saver)
        delete()
        
    def insertJadwal():
        model = jadwal()
        model.fiturjadwal()
        model.insert(saver)
        delete()
        
    def insertPenghuni():
        model = penghuni()
        model.fiturpenghuni()
        model.insert_single(str(saver[0]))
        delete()
    
    def insertLorong():
        model = lorong()
        model.insert(saver)
        delete()
