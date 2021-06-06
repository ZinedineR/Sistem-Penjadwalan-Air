# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class loginPage
###########################################################################

class loginPage ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Halaman Login", pos = wx.DefaultPosition, size = wx.Size( 500,227 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.plaintext = wx.StaticText( self, wx.ID_ANY, u"Login ", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.plaintext.Wrap( -1 )

		bSizer1.Add( self.plaintext, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		sbSizer11 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"password = root" ), wx.VERTICAL )

		self.text_password = wx.TextCtrl( sbSizer11.GetStaticBox(), wx.ID_ANY, u"root", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer11.Add( self.text_password, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer1.Add( sbSizer11, 1, wx.EXPAND, 5 )

		self.but_login = wx.Button( self, wx.ID_ANY, u"login", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.but_login, 0, wx.ALL, 5 )

		sbSizer111 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Bukan admin?" ), wx.VERTICAL )

		self.m_button4 = wx.Button( sbSizer111.GetStaticBox(), wx.ID_ANY, u"login as user", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer111.Add( self.m_button4, 0, wx.ALL, 5 )


		bSizer1.Add( sbSizer111, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.but_login.Bind( wx.EVT_BUTTON, self.clickLogin )
		self.m_button4.Bind( wx.EVT_BUTTON, self.userClickLogin )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def clickLogin( self, event ):
		event.Skip()

	def userClickLogin( self, event ):
		event.Skip()


###########################################################################
## Class adminMenu
###########################################################################

class adminMenu ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Halaman Admin", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Mengatur jadwal penggunaan air per lorong", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		bSizer4.Add( self.m_staticText4, 0, wx.ALL, 5 )

		self.m_button11 = wx.Button( self, wx.ID_ANY, u"Jadwal Penggunaan", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_button11, 0, wx.ALL, 5 )


		bSizer3.Add( bSizer4, 1, wx.EXPAND, 5 )

		bSizer41 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText41 = wx.StaticText( self, wx.ID_ANY, u"Menambah atau mengurangi liter air tangki", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText41.Wrap( -1 )

		bSizer41.Add( self.m_staticText41, 0, wx.ALL, 5 )

		self.m_button111 = wx.Button( self, wx.ID_ANY, u"tangki", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer41.Add( self.m_button111, 0, wx.ALL, 5 )


		bSizer3.Add( bSizer41, 1, wx.EXPAND, 5 )

		bSizer42 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText42 = wx.StaticText( self, wx.ID_ANY, u"Mengatur pengaturan penghuni pada lorong", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText42.Wrap( -1 )

		bSizer42.Add( self.m_staticText42, 0, wx.ALL, 5 )

		self.m_button112 = wx.Button( self, wx.ID_ANY, u"Lorong", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer42.Add( self.m_button112, 0, wx.ALL, 5 )


		bSizer3.Add( bSizer42, 1, wx.EXPAND, 5 )

		bSizer43 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText43 = wx.StaticText( self, wx.ID_ANY, u"Menambah penghuni ke lorong", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText43.Wrap( -1 )

		bSizer43.Add( self.m_staticText43, 0, wx.ALL, 5 )

		self.m_button113 = wx.Button( self, wx.ID_ANY, u"Penghuni", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer43.Add( self.m_button113, 0, wx.ALL, 5 )


		bSizer3.Add( bSizer43, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer3 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button11.Bind( wx.EVT_BUTTON, self.clickJadwalPenggunaan )
		self.m_button111.Bind( wx.EVT_BUTTON, self.clickTangki )
		self.m_button112.Bind( wx.EVT_BUTTON, self.clickLorong )
		self.m_button113.Bind( wx.EVT_BUTTON, self.clickPenghuni )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def clickJadwalPenggunaan( self, event ):
		event.Skip()

	def clickTangki( self, event ):
		event.Skip()

	def clickLorong( self, event ):
		event.Skip()

	def clickPenghuni( self, event ):
		event.Skip()


###########################################################################
## Class JadwalPenggunaan
###########################################################################

class JadwalPenggunaan ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Jadwal Penggunaan", pos = wx.DefaultPosition, size = wx.Size( 481,197 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		self.lihatJadwal = wx.StaticText( self, wx.ID_ANY, u"Lihat Penjadwalan Air", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lihatJadwal.Wrap( -1 )

		bSizer7.Add( self.lihatJadwal, 0, wx.ALL, 5 )

		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Lihat Penjadwalan Air", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		fgSizer1.Add( self.m_staticText7, 0, wx.ALL, 5 )

		self.m_button9 = wx.Button( self, wx.ID_ANY, u"Lihat", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_button9, 0, wx.ALL, 5 )

		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Penambahan Jadwal Penggunaan Air", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		fgSizer1.Add( self.m_staticText8, 0, wx.ALL, 5 )

		self.m_button10 = wx.Button( self, wx.ID_ANY, u"Tambah", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_button10, 0, wx.ALL, 5 )

		self.m_button11 = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_button11, 0, wx.ALL, 5 )


		bSizer7.Add( fgSizer1, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer7 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button9.Bind( wx.EVT_BUTTON, self.clickLihat )
		self.m_button10.Bind( wx.EVT_BUTTON, self.clickTambah )
		self.m_button11.Bind( wx.EVT_BUTTON, self.clickKembali )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def clickLihat( self, event ):
		event.Skip()

	def clickTambah( self, event ):
		event.Skip()

	def clickKembali( self, event ):
		event.Skip()


###########################################################################
## Class lihatPenjadwalanAir
###########################################################################

class lihatPenjadwalanAir ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Lihat Penjadwalan Air", pos = wx.DefaultPosition, size = wx.Size( 569,289 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		self.lihatJadwal = wx.StaticText( self, wx.ID_ANY, u"Lihat Jadwal ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lihatJadwal.Wrap( -1 )

		bSizer8.Add( self.lihatJadwal, 0, wx.ALL, 5 )

		bSizer9 = wx.BoxSizer( wx.VERTICAL )


		bSizer8.Add( bSizer9, 1, wx.EXPAND, 5 )

		self.m_grid6 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL )

		# Grid
		self.m_grid6.CreateGrid( 0, 5 )
		self.m_grid6.EnableEditing( False )
		self.m_grid6.EnableGridLines( True )
		self.m_grid6.EnableDragGridSize( False )
		self.m_grid6.SetMargins( 0, 0 )

		# Columns
		self.m_grid6.SetColSize( 0, 80 )
		self.m_grid6.SetColSize( 1, 80 )
		self.m_grid6.SetColSize( 2, 80 )
		self.m_grid6.SetColSize( 3, 99 )
		self.m_grid6.SetColSize( 4, 130 )
		self.m_grid6.EnableDragColMove( False )
		self.m_grid6.EnableDragColSize( True )
		self.m_grid6.SetColLabelSize( 30 )
		self.m_grid6.SetColLabelValue( 0, u"Jadwal ID" )
		self.m_grid6.SetColLabelValue( 1, u"Tangki ID" )
		self.m_grid6.SetColLabelValue( 2, u"Lorong ID" )
		self.m_grid6.SetColLabelValue( 3, u"Penggunaan" )
		self.m_grid6.SetColLabelValue( 4, u"Tangki_Tanggal" )
		self.m_grid6.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid6.EnableDragRowSize( False )
		self.m_grid6.SetRowLabelSize( 80 )
		self.m_grid6.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid6.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer8.Add( self.m_grid6, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		fgSizer8 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer8.SetFlexibleDirection( wx.BOTH )
		fgSizer8.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.kembali = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.kembali, 0, wx.ALL, 5 )


		bSizer8.Add( fgSizer8, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer8 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.kembali.Bind( wx.EVT_BUTTON, self.clickKembali )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def clickKembali( self, event ):
		event.Skip()


###########################################################################
## Class tambahPenjadwalanAirone
###########################################################################

class tambahPenjadwalanAirone ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Penambahan Penjadwalan Air", pos = wx.DefaultPosition, size = wx.Size( 621,291 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		self.TambahPenjadwalanAir = wx.StaticText( self, wx.ID_ANY, u"Tambah Penjadwalan Air", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.TambahPenjadwalanAir.Wrap( -1 )

		bSizer10.Add( self.TambahPenjadwalanAir, 0, wx.ALL, 5 )

		bSizer15 = wx.BoxSizer( wx.VERTICAL )

		self.m_grid4 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid4.CreateGrid( 4, 3 )
		self.m_grid4.EnableEditing( True )
		self.m_grid4.EnableGridLines( True )
		self.m_grid4.EnableDragGridSize( False )
		self.m_grid4.SetMargins( 0, 0 )

		# Columns
		self.m_grid4.SetColSize( 0, 80 )
		self.m_grid4.SetColSize( 1, 109 )
		self.m_grid4.SetColSize( 2, 117 )
		self.m_grid4.EnableDragColMove( False )
		self.m_grid4.EnableDragColSize( True )
		self.m_grid4.SetColLabelSize( 30 )
		self.m_grid4.SetColLabelValue( 0, u"Tangki ID" )
		self.m_grid4.SetColLabelValue( 1, u"Tangki Tanggal" )
		self.m_grid4.SetColLabelValue( 2, u"Jumlah Air Liter" )
		self.m_grid4.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid4.EnableDragRowSize( True )
		self.m_grid4.SetRowLabelSize( 80 )
		self.m_grid4.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid4.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer15.Add( self.m_grid4, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		fgSizer4 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.inputTangki = wx.StaticText( self, wx.ID_ANY, u"Input Tangki Yang Akan Digunakan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.inputTangki.Wrap( -1 )

		fgSizer4.Add( self.inputTangki, 0, wx.ALL, 5 )

		self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_textCtrl4, 0, wx.ALL, 5 )

		self.next = wx.Button( self, wx.ID_ANY, u"Selanjutnya", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.next, 0, wx.ALL, 5 )


		bSizer15.Add( fgSizer4, 1, wx.EXPAND, 5 )


		bSizer10.Add( bSizer15, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer10 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_grid4.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.selectCell )
		self.next.Bind( wx.EVT_BUTTON, self.clickSelanjutnya )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def selectCell( self, event ):
		event.Skip()

	def clickSelanjutnya( self, event ):
		event.Skip()


###########################################################################
## Class tambahPenjadwalanAirtwo
###########################################################################

class tambahPenjadwalanAirtwo ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Tambah Penjadwalan Air", pos = wx.DefaultPosition, size = wx.Size( 501,272 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer14 = wx.BoxSizer( wx.VERTICAL )

		self.tambahPenjadwalanAir = wx.StaticText( self, wx.ID_ANY, u"Tambah Penjadwalan Air", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tambahPenjadwalanAir.Wrap( -1 )

		bSizer14.Add( self.tambahPenjadwalanAir, 0, wx.ALL, 5 )

		bSizer15 = wx.BoxSizer( wx.VERTICAL )

		self.m_grid3 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid3.CreateGrid( 3, 2 )
		self.m_grid3.EnableEditing( True )
		self.m_grid3.EnableGridLines( True )
		self.m_grid3.EnableDragGridSize( False )
		self.m_grid3.SetMargins( 0, 0 )

		# Columns
		self.m_grid3.SetColSize( 0, 84 )
		self.m_grid3.SetColSize( 1, 80 )
		self.m_grid3.EnableDragColMove( False )
		self.m_grid3.EnableDragColSize( True )
		self.m_grid3.SetColLabelSize( 30 )
		self.m_grid3.SetColLabelValue( 0, u"Kategori ID" )
		self.m_grid3.SetColLabelValue( 1, u"Deskripsi" )
		self.m_grid3.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid3.EnableDragRowSize( True )
		self.m_grid3.SetRowLabelSize( 80 )
		self.m_grid3.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid3.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer15.Add( self.m_grid3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		fgSizer4 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.inputDigunakanUntukApa = wx.StaticText( self, wx.ID_ANY, u"Digunakan Untuk Apa", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.inputDigunakanUntukApa.Wrap( -1 )

		fgSizer4.Add( self.inputDigunakanUntukApa, 0, wx.ALL, 5 )

		self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_textCtrl3, 0, wx.ALL, 5 )

		self.m_button16 = wx.Button( self, wx.ID_ANY, u"Selanjutnya", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_button16, 0, wx.ALL, 5 )


		bSizer15.Add( fgSizer4, 1, wx.EXPAND, 5 )


		bSizer14.Add( bSizer15, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer14 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button16.Bind( wx.EVT_BUTTON, self.clickSelanjutnya )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def clickSelanjutnya( self, event ):
		event.Skip()


###########################################################################
## Class tambahPenjadwalanAirthree
###########################################################################

class tambahPenjadwalanAirthree ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Tambah Penjadwalan Air", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer16 = wx.BoxSizer( wx.VERTICAL )

		self.tambahPenjadwalanAir = wx.StaticText( self, wx.ID_ANY, u"Tambah Penjadwalan Air", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tambahPenjadwalanAir.Wrap( -1 )

		bSizer16.Add( self.tambahPenjadwalanAir, 0, wx.ALL, 5 )

		bSizer17 = wx.BoxSizer( wx.VERTICAL )

		self.m_grid5 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid5.CreateGrid( 4, 1 )
		self.m_grid5.EnableEditing( True )
		self.m_grid5.EnableGridLines( True )
		self.m_grid5.EnableDragGridSize( False )
		self.m_grid5.SetMargins( 0, 0 )

		# Columns
		self.m_grid5.EnableDragColMove( False )
		self.m_grid5.EnableDragColSize( True )
		self.m_grid5.SetColLabelSize( 30 )
		self.m_grid5.SetColLabelValue( 0, u"Lorong ID" )
		self.m_grid5.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid5.EnableDragRowSize( True )
		self.m_grid5.SetRowLabelSize( 80 )
		self.m_grid5.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid5.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer17.Add( self.m_grid5, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		fgSizer7 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer7.SetFlexibleDirection( wx.BOTH )
		fgSizer7.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.digunakanUntukLorong = wx.StaticText( self, wx.ID_ANY, u"Digunakan Untuk Lorong Berapa", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.digunakanUntukLorong.Wrap( -1 )

		fgSizer7.Add( self.digunakanUntukLorong, 0, wx.ALL, 5 )

		self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.m_textCtrl4, 0, wx.ALL, 5 )

		self.selesai = wx.Button( self, wx.ID_ANY, u"Selesai", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.selesai, 0, wx.ALL, 5 )


		bSizer17.Add( fgSizer7, 1, wx.EXPAND, 5 )


		bSizer16.Add( bSizer17, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer16 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.selesai.Bind( wx.EVT_BUTTON, self.clickSelesai )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def clickSelesai( self, event ):
		event.Skip()


###########################################################################
## Class menuTangki
###########################################################################

class menuTangki ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Halaman Tangki", pos = wx.DefaultPosition, size = wx.Size( 384,224 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizer3 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.lihatTangki = wx.StaticText( self, wx.ID_ANY, u"Lihat Tangki", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lihatTangki.Wrap( -1 )

		fgSizer3.Add( self.lihatTangki, 0, wx.ALL, 5 )

		self.Lihat = wx.Button( self, wx.ID_ANY, u"Lihat", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.Lihat, 0, wx.ALL, 5 )

		self.pengisianpengurangan = wx.StaticText( self, wx.ID_ANY, u"Pengisian/Pengurangan Liter Tangki", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pengisianpengurangan.Wrap( -1 )

		fgSizer3.Add( self.pengisianpengurangan, 0, wx.ALL, 5 )

		self.m_button14 = wx.Button( self, wx.ID_ANY, u"Update Tangki", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_button14, 0, wx.ALL, 5 )

		self.HistoriTangki = wx.StaticText( self, wx.ID_ANY, u"Histori Tangki", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.HistoriTangki.Wrap( -1 )

		fgSizer3.Add( self.HistoriTangki, 0, wx.ALL, 5 )

		self.m_button15 = wx.Button( self, wx.ID_ANY, u"Histori", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_button15, 0, wx.ALL, 5 )

		self.m_button16 = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_button16, 0, wx.ALL, 5 )


		self.SetSizer( fgSizer3 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Lihat.Bind( wx.EVT_BUTTON, self.clickLihat )
		self.m_button14.Bind( wx.EVT_BUTTON, self.clickCek )
		self.m_button15.Bind( wx.EVT_BUTTON, self.clickHistori )
		self.m_button16.Bind( wx.EVT_BUTTON, self.clickKembali )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def clickLihat( self, event ):
		event.Skip()

	def clickCek( self, event ):
		event.Skip()

	def clickHistori( self, event ):
		event.Skip()

	def clickKembali( self, event ):
		event.Skip()


###########################################################################
## Class lihatTangki
###########################################################################

class lihatTangki ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Lihat Tangki", pos = wx.DefaultPosition, size = wx.Size( 500,243 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer12 = wx.BoxSizer( wx.VERTICAL )

		self.lihatTangki = wx.StaticText( self, wx.ID_ANY, u"Lihat Tangki", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lihatTangki.Wrap( -1 )

		bSizer12.Add( self.lihatTangki, 0, wx.ALL, 5 )

		bSizer14 = wx.BoxSizer( wx.VERTICAL )

		self.m_grid3 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid3.CreateGrid( 4, 3 )
		self.m_grid3.EnableEditing( True )
		self.m_grid3.EnableGridLines( True )
		self.m_grid3.EnableDragGridSize( False )
		self.m_grid3.SetMargins( 0, 0 )

		# Columns
		self.m_grid3.EnableDragColMove( False )
		self.m_grid3.EnableDragColSize( True )
		self.m_grid3.SetColLabelSize( 30 )
		self.m_grid3.SetColLabelValue( 0, u"Tangki ID" )
		self.m_grid3.SetColLabelValue( 1, u"Tangki Tanggal" )
		self.m_grid3.SetColLabelValue( 2, u"Jumlah Air Liter" )
		self.m_grid3.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid3.EnableDragRowSize( True )
		self.m_grid3.SetRowLabelSize( 80 )
		self.m_grid3.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid3.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer14.Add( self.m_grid3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.Kembali = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.Kembali, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )


		bSizer12.Add( bSizer14, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer12 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Kembali.Bind( wx.EVT_BUTTON, self.clickKembali )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def clickKembali( self, event ):
		event.Skip()


###########################################################################
## Class pengisianpenguranganLiter
###########################################################################

class pengisianpenguranganLiter ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Pengisian/Pengurangan Liter Tangki", pos = wx.DefaultPosition, size = wx.Size( 530,335 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer18 = wx.BoxSizer( wx.VERTICAL )

		self.PengisianPenguranganLiterTangki = wx.StaticText( self, wx.ID_ANY, u"Pengisian/Pengurangan Liter Tangki", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PengisianPenguranganLiterTangki.Wrap( -1 )

		bSizer18.Add( self.PengisianPenguranganLiterTangki, 0, wx.ALL, 5 )

		bSizer19 = wx.BoxSizer( wx.VERTICAL )

		self.m_grid7 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid7.CreateGrid( 4, 3 )
		self.m_grid7.EnableEditing( True )
		self.m_grid7.EnableGridLines( True )
		self.m_grid7.EnableDragGridSize( False )
		self.m_grid7.SetMargins( 0, 0 )

		# Columns
		self.m_grid7.EnableDragColMove( False )
		self.m_grid7.EnableDragColSize( True )
		self.m_grid7.SetColLabelSize( 30 )
		self.m_grid7.SetColLabelValue( 0, u"Tangki ID" )
		self.m_grid7.SetColLabelValue( 1, u"Tangki Tanggal" )
		self.m_grid7.SetColLabelValue( 2, u"Jumlah Air Liter" )
		self.m_grid7.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid7.EnableDragRowSize( True )
		self.m_grid7.SetRowLabelSize( 80 )
		self.m_grid7.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid7.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer19.Add( self.m_grid7, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_LEFT|wx.ALL, 5 )

		fgSizer9 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer9.SetFlexibleDirection( wx.BOTH )
		fgSizer9.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.inputIDTangki = wx.StaticText( self, wx.ID_ANY, u"Input ID Tangki yang Ingin Diisi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.inputIDTangki.Wrap( -1 )

		fgSizer9.Add( self.inputIDTangki, 0, wx.ALL, 5 )

		self.m_textCtrl5 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer9.Add( self.m_textCtrl5, 0, wx.ALL, 5 )

		self.m_staticText23 = wx.StaticText( self, wx.ID_ANY, u"Tambahkan Jumlah Liter (Gunakan - Untuk Mengurangi)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )

		fgSizer9.Add( self.m_staticText23, 0, wx.ALL, 5 )

		self.m_textCtrl6 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer9.Add( self.m_textCtrl6, 0, wx.ALL, 5 )

		self.selesai = wx.Button( self, wx.ID_ANY, u"Selesai", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer9.Add( self.selesai, 0, wx.ALL, 5 )


		bSizer19.Add( fgSizer9, 1, wx.EXPAND, 5 )


		bSizer18.Add( bSizer19, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer18 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.selesai.Bind( wx.EVT_BUTTON, self.clickSelesai )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def clickSelesai( self, event ):
		event.Skip()


###########################################################################
## Class HistoryTangki
###########################################################################

class HistoryTangki ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"History Tangki", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer20 = wx.BoxSizer( wx.VERTICAL )

		self.HistoryTangki = wx.StaticText( self, wx.ID_ANY, u"History Tangki", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.HistoryTangki.Wrap( -1 )

		bSizer20.Add( self.HistoryTangki, 0, wx.ALL, 5 )

		bSizer21 = wx.BoxSizer( wx.VERTICAL )

		self.m_grid8 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid8.CreateGrid( 0, 4 )
		self.m_grid8.EnableEditing( True )
		self.m_grid8.EnableGridLines( True )
		self.m_grid8.EnableDragGridSize( False )
		self.m_grid8.SetMargins( 0, 170 )

		# Columns
		self.m_grid8.EnableDragColMove( False )
		self.m_grid8.EnableDragColSize( True )
		self.m_grid8.SetColLabelSize( 30 )
		self.m_grid8.SetColLabelValue( 0, u"History ID" )
		self.m_grid8.SetColLabelValue( 1, u"Tangki ID" )
		self.m_grid8.SetColLabelValue( 2, u"Tanggal Tangki" )
		self.m_grid8.SetColLabelValue( 3, u"Jumlah Air Liter" )
		self.m_grid8.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid8.EnableDragRowSize( True )
		self.m_grid8.SetRowLabelSize( 80 )
		self.m_grid8.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid8.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer21.Add( self.m_grid8, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		fgSizer10 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer10.SetFlexibleDirection( wx.BOTH )
		fgSizer10.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.kembali = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer10.Add( self.kembali, 0, wx.ALL, 5 )


		bSizer21.Add( fgSizer10, 1, wx.EXPAND, 5 )


		bSizer20.Add( bSizer21, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer20 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.kembali.Bind( wx.EVT_BUTTON, self.clickKembali )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def clickKembali( self, event ):
		event.Skip()


###########################################################################
## Class lorongPage
###########################################################################

class lorongPage ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Menu Lorong", pos = wx.DefaultPosition, size = wx.Size( 500,208 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer22 = wx.BoxSizer( wx.VERTICAL )

		self.MenuLorong = wx.StaticText( self, wx.ID_ANY, u"Menu Lorong", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.MenuLorong.Wrap( -1 )

		bSizer22.Add( self.MenuLorong, 0, wx.ALL, 5 )

		fgSizer11 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer11.SetFlexibleDirection( wx.BOTH )
		fgSizer11.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.lihatLorong = wx.StaticText( self, wx.ID_ANY, u"Lihat Lorong", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lihatLorong.Wrap( -1 )

		fgSizer11.Add( self.lihatLorong, 0, wx.ALL, 5 )

		self.Lihat = wx.Button( self, wx.ID_ANY, u"Lihat", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer11.Add( self.Lihat, 0, wx.ALL, 5 )

		self.penambahanPenghuniLorong = wx.StaticText( self, wx.ID_ANY, u"Penambahan Penghuni Lorong", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.penambahanPenghuniLorong.Wrap( -1 )

		fgSizer11.Add( self.penambahanPenghuniLorong, 0, wx.ALL, 5 )

		self.tambah = wx.Button( self, wx.ID_ANY, u"Tambah", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer11.Add( self.tambah, 0, wx.ALL, 5 )

		self.kembali = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer11.Add( self.kembali, 0, wx.ALL, 5 )


		bSizer22.Add( fgSizer11, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer22 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Lihat.Bind( wx.EVT_BUTTON, self.clickLihat )
		self.tambah.Bind( wx.EVT_BUTTON, self.clickTambah )
		self.kembali.Bind( wx.EVT_BUTTON, self.clickKembali )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def clickLihat( self, event ):
		event.Skip()

	def clickTambah( self, event ):
		event.Skip()

	def clickKembali( self, event ):
		event.Skip()


###########################################################################
## Class lihatLorong
###########################################################################

class lihatLorong ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Lihat Lorong", pos = wx.DefaultPosition, size = wx.Size( 500,416 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer23 = wx.BoxSizer( wx.VERTICAL )

		self.lihatLorong = wx.StaticText( self, wx.ID_ANY, u"Lihat Lorong", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lihatLorong.Wrap( -1 )

		bSizer23.Add( self.lihatLorong, 0, wx.ALL, 5 )

		bSizer24 = wx.BoxSizer( wx.VERTICAL )

		self.m_grid10 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid10.CreateGrid( 0, 3 )
		self.m_grid10.EnableEditing( True )
		self.m_grid10.EnableGridLines( True )
		self.m_grid10.EnableDragGridSize( False )
		self.m_grid10.SetMargins( 0, 0 )

		# Columns
		self.m_grid10.EnableDragColMove( False )
		self.m_grid10.EnableDragColSize( True )
		self.m_grid10.SetColLabelSize( 30 )
		self.m_grid10.SetColLabelValue( 0, u"Lorong ID" )
		self.m_grid10.SetColLabelValue( 1, u"Penghuni ID" )
		self.m_grid10.SetColLabelValue( 2, u"Nama Penghuni" )
		self.m_grid10.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid10.EnableDragRowSize( True )
		self.m_grid10.SetRowLabelSize( 80 )
		self.m_grid10.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid10.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer24.Add( self.m_grid10, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		fgSizer13 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer13.SetFlexibleDirection( wx.BOTH )
		fgSizer13.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.kembali = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer13.Add( self.kembali, 0, wx.ALL, 5 )


		bSizer24.Add( fgSizer13, 1, wx.EXPAND, 5 )


		bSizer23.Add( bSizer24, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer23 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.kembali.Bind( wx.EVT_BUTTON, self.clickKembali )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def clickKembali( self, event ):
		event.Skip()


###########################################################################
## Class penambahanPenghunione
###########################################################################

class penambahanPenghunione ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Penambahan Penghuni Lorong", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer25 = wx.BoxSizer( wx.VERTICAL )

		self.PenambahanPenghuniLorong = wx.StaticText( self, wx.ID_ANY, u"Penambahan Penghuni Lorong", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PenambahanPenghuniLorong.Wrap( -1 )

		bSizer25.Add( self.PenambahanPenghuniLorong, 0, wx.ALL, 5 )

		bSizer26 = wx.BoxSizer( wx.VERTICAL )

		self.m_grid11 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid11.CreateGrid( 4, 1 )
		self.m_grid11.EnableEditing( True )
		self.m_grid11.EnableGridLines( True )
		self.m_grid11.EnableDragGridSize( False )
		self.m_grid11.SetMargins( 0, 0 )

		# Columns
		self.m_grid11.EnableDragColMove( False )
		self.m_grid11.EnableDragColSize( True )
		self.m_grid11.SetColLabelSize( 30 )
		self.m_grid11.SetColLabelValue( 0, u"Lorong ID" )
		self.m_grid11.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid11.EnableDragRowSize( True )
		self.m_grid11.SetRowLabelSize( 80 )
		self.m_grid11.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid11.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer26.Add( self.m_grid11, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		fgSizer14 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer14.SetFlexibleDirection( wx.BOTH )
		fgSizer14.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.inputLorong = wx.StaticText( self, wx.ID_ANY, u"Inputkan Lorong Yang Ingin Ditambahkan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.inputLorong.Wrap( -1 )

		fgSizer14.Add( self.inputLorong, 0, wx.ALL, 5 )

		self.m_textCtrl7 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer14.Add( self.m_textCtrl7, 0, wx.ALL, 5 )

		self.Selanjutnya = wx.Button( self, wx.ID_ANY, u"Selanjutnya", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer14.Add( self.Selanjutnya, 0, wx.ALL, 5 )


		bSizer26.Add( fgSizer14, 1, wx.EXPAND, 5 )


		bSizer25.Add( bSizer26, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer25 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Selanjutnya.Bind( wx.EVT_BUTTON, self.clickSelanjutnya )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def clickSelanjutnya( self, event ):
		event.Skip()


###########################################################################
## Class penambahanPenghunitwo
###########################################################################

class penambahanPenghunitwo ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Penambahan Penghuni Lorong", pos = wx.DefaultPosition, size = wx.Size( 555,403 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer27 = wx.BoxSizer( wx.VERTICAL )

		self.m_grid12 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid12.CreateGrid( 0, 2 )
		self.m_grid12.EnableEditing( True )
		self.m_grid12.EnableGridLines( True )
		self.m_grid12.EnableDragGridSize( False )
		self.m_grid12.SetMargins( 0, 0 )

		# Columns
		self.m_grid12.EnableDragColMove( False )
		self.m_grid12.EnableDragColSize( True )
		self.m_grid12.SetColLabelSize( 30 )
		self.m_grid12.SetColLabelValue( 0, u"Penghuni ID" )
		self.m_grid12.SetColLabelValue( 1, u"Nama Penghuni" )
		self.m_grid12.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid12.EnableDragRowSize( True )
		self.m_grid12.SetRowLabelSize( 80 )
		self.m_grid12.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid12.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer27.Add( self.m_grid12, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		fgSizer15 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer15.SetFlexibleDirection( wx.BOTH )
		fgSizer15.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText32 = wx.StaticText( self, wx.ID_ANY, u"Inputkan ID Penghuni Yang Ingin Ditambahkan Di Lorong", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )

		fgSizer15.Add( self.m_staticText32, 0, wx.ALL, 5 )

		self.m_textCtrl8 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer15.Add( self.m_textCtrl8, 0, wx.ALL, 5 )

		self.selesai = wx.Button( self, wx.ID_ANY, u"Selesai", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer15.Add( self.selesai, 0, wx.ALL, 5 )


		bSizer27.Add( fgSizer15, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer27 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.selesai.Bind( wx.EVT_BUTTON, self.clickSelesai )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def clickSelesai( self, event ):
		event.Skip()


###########################################################################
## Class penghuniPage
###########################################################################

class penghuniPage ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Halaman Penghuni", pos = wx.DefaultPosition, size = wx.Size( 335,238 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer28 = wx.BoxSizer( wx.VERTICAL )

		self.penghuniPage = wx.StaticText( self, wx.ID_ANY, u"Halaman Penghuni", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.penghuniPage.Wrap( -1 )

		bSizer28.Add( self.penghuniPage, 0, wx.ALL, 5 )

		fgSizer16 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer16.SetFlexibleDirection( wx.BOTH )
		fgSizer16.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.lihatPenghuni = wx.StaticText( self, wx.ID_ANY, u"Lihat Penghuni", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lihatPenghuni.Wrap( -1 )

		fgSizer16.Add( self.lihatPenghuni, 0, wx.ALL, 5 )

		self.lihat = wx.Button( self, wx.ID_ANY, u"Lihat", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer16.Add( self.lihat, 0, wx.ALL, 5 )

		self.PenambahanPenghuni = wx.StaticText( self, wx.ID_ANY, u"Penambahan Penghuni", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PenambahanPenghuni.Wrap( -1 )

		fgSizer16.Add( self.PenambahanPenghuni, 0, wx.ALL, 5 )

		self.tambah = wx.Button( self, wx.ID_ANY, u"Tambah", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer16.Add( self.tambah, 0, wx.ALL, 5 )

		self.kembali = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer16.Add( self.kembali, 0, wx.ALL, 5 )


		bSizer28.Add( fgSizer16, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer28 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.lihat.Bind( wx.EVT_BUTTON, self.clickLihat )
		self.tambah.Bind( wx.EVT_BUTTON, self.clickTambah )
		self.kembali.Bind( wx.EVT_BUTTON, self.clickKembali )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def clickLihat( self, event ):
		event.Skip()

	def clickTambah( self, event ):
		event.Skip()

	def clickKembali( self, event ):
		event.Skip()


###########################################################################
## Class lihatPenghuni
###########################################################################

class lihatPenghuni ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Lihat Penghuni", pos = wx.DefaultPosition, size = wx.Size( 500,441 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer29 = wx.BoxSizer( wx.VERTICAL )

		self.lihatPenghuni = wx.StaticText( self, wx.ID_ANY, u"Lihat Penghuni", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lihatPenghuni.Wrap( -1 )

		bSizer29.Add( self.lihatPenghuni, 0, wx.ALL, 5 )

		bSizer30 = wx.BoxSizer( wx.VERTICAL )

		self.m_grid13 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid13.CreateGrid( 0, 2 )
		self.m_grid13.EnableEditing( True )
		self.m_grid13.EnableGridLines( True )
		self.m_grid13.EnableDragGridSize( False )
		self.m_grid13.SetMargins( 0, 0 )

		# Columns
		self.m_grid13.EnableDragColMove( False )
		self.m_grid13.EnableDragColSize( True )
		self.m_grid13.SetColLabelSize( 30 )
		self.m_grid13.SetColLabelValue( 0, u"Penghuni ID" )
		self.m_grid13.SetColLabelValue( 1, u"Nama Penghuni" )
		self.m_grid13.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid13.EnableDragRowSize( True )
		self.m_grid13.SetRowLabelSize( 80 )
		self.m_grid13.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid13.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer30.Add( self.m_grid13, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		bSizer31 = wx.BoxSizer( wx.VERTICAL )

		self.kembali = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer31.Add( self.kembali, 0, wx.ALL, 5 )


		bSizer30.Add( bSizer31, 1, wx.EXPAND, 5 )


		bSizer29.Add( bSizer30, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer29 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.kembali.Bind( wx.EVT_BUTTON, self.clickKembali )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def clickKembali( self, event ):
		event.Skip()


###########################################################################
## Class penambahanPenghuni
###########################################################################

class penambahanPenghuni ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Penambahan Penghuni", pos = wx.DefaultPosition, size = wx.Size( 500,146 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer32 = wx.BoxSizer( wx.VERTICAL )

		self.TambahPenghuni = wx.StaticText( self, wx.ID_ANY, u"Tambah Penghuni", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.TambahPenghuni.Wrap( -1 )

		bSizer32.Add( self.TambahPenghuni, 0, wx.ALL, 5 )

		fgSizer17 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer17.SetFlexibleDirection( wx.BOTH )
		fgSizer17.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.inputNama = wx.StaticText( self, wx.ID_ANY, u"Masukkan Nama Penghuni", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.inputNama.Wrap( -1 )

		fgSizer17.Add( self.inputNama, 0, wx.ALL, 5 )

		self.m_textCtrl9 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer17.Add( self.m_textCtrl9, 0, wx.ALL, 5 )

		self.selesai = wx.Button( self, wx.ID_ANY, u"Selesai", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer17.Add( self.selesai, 0, wx.ALL, 5 )


		bSizer32.Add( fgSizer17, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer32 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.selesai.Bind( wx.EVT_BUTTON, self.clickSelesai )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def clickSelesai( self, event ):
		event.Skip()


###########################################################################
## Class userMenu
###########################################################################

class userMenu ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"User Menu", pos = wx.DefaultPosition, size = wx.Size( 363,228 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer33 = wx.BoxSizer( wx.VERTICAL )

		self.userMenu = wx.StaticText( self, wx.ID_ANY, u"Menu User", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.userMenu.Wrap( -1 )

		bSizer33.Add( self.userMenu, 0, wx.ALL, 5 )

		fgSizer18 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer18.SetFlexibleDirection( wx.BOTH )
		fgSizer18.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.LihatJadwal = wx.StaticText( self, wx.ID_ANY, u"Lihat Jadwal", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LihatJadwal.Wrap( -1 )

		fgSizer18.Add( self.LihatJadwal, 0, wx.ALL, 5 )

		self.lihatJadwal = wx.Button( self, wx.ID_ANY, u"Lihat Jadwal", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer18.Add( self.lihatJadwal, 0, wx.ALL, 5 )

		self.LihatPenggunaan = wx.StaticText( self, wx.ID_ANY, u"Lihat Penggunaan ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LihatPenggunaan.Wrap( -1 )

		fgSizer18.Add( self.LihatPenggunaan, 0, wx.ALL, 5 )

		self.lihat = wx.Button( self, wx.ID_ANY, u"Lihat Penggunaan", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer18.Add( self.lihat, 0, wx.ALL, 5 )

		self.penambahanPenggunaan = wx.StaticText( self, wx.ID_ANY, u"Penambahan Penggunaan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.penambahanPenggunaan.Wrap( -1 )

		fgSizer18.Add( self.penambahanPenggunaan, 0, wx.ALL, 5 )

		self.tambah = wx.Button( self, wx.ID_ANY, u"Tambah Penggunaan", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer18.Add( self.tambah, 0, wx.ALL, 5 )


		bSizer33.Add( fgSizer18, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer33 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.lihatJadwal.Bind( wx.EVT_BUTTON, self.ClickLihatJadwal )
		self.lihat.Bind( wx.EVT_BUTTON, self.ClickLihatPenggunaan )
		self.tambah.Bind( wx.EVT_BUTTON, self.ClickTambahPenggunaan )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def ClickLihatJadwal( self, event ):
		event.Skip()

	def ClickLihatPenggunaan( self, event ):
		event.Skip()

	def ClickTambahPenggunaan( self, event ):
		event.Skip()


###########################################################################
## Class lihatPenggunaan
###########################################################################

class lihatPenggunaan ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Lihat Penggunaan", pos = wx.DefaultPosition, size = wx.Size( 500,368 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer34 = wx.BoxSizer( wx.VERTICAL )

		self.lihatPenggunaan = wx.StaticText( self, wx.ID_ANY, u"Lihat Penggunaan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lihatPenggunaan.Wrap( -1 )

		bSizer34.Add( self.lihatPenggunaan, 0, wx.ALL, 5 )

		bSizer35 = wx.BoxSizer( wx.VERTICAL )

		self.m_grid14 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid14.CreateGrid( 0, 4 )
		self.m_grid14.EnableEditing( True )
		self.m_grid14.EnableGridLines( True )
		self.m_grid14.EnableDragGridSize( False )
		self.m_grid14.SetMargins( 0, 0 )

		# Columns
		self.m_grid14.EnableDragColMove( False )
		self.m_grid14.EnableDragColSize( True )
		self.m_grid14.SetColLabelSize( 30 )
		self.m_grid14.SetColLabelValue( 0, u"Pengguna ID" )
		self.m_grid14.SetColLabelValue( 1, u"Nama Penghuni" )
		self.m_grid14.SetColLabelValue( 2, u"Penggunaan" )
		self.m_grid14.SetColLabelValue( 3, u"Tanggal Penggunaan" )
		self.m_grid14.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid14.EnableDragRowSize( True )
		self.m_grid14.SetRowLabelSize( 80 )
		self.m_grid14.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid14.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer35.Add( self.m_grid14, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		bSizer36 = wx.BoxSizer( wx.VERTICAL )

		self.kembali = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer36.Add( self.kembali, 0, wx.ALL, 5 )


		bSizer35.Add( bSizer36, 1, wx.EXPAND, 5 )


		bSizer34.Add( bSizer35, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer34 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.kembali.Bind( wx.EVT_BUTTON, self.clickKembali )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def clickKembali( self, event ):
		event.Skip()


###########################################################################
## Class lihatJadwal
###########################################################################

class lihatJadwal ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Lihat Jadwal", pos = wx.DefaultPosition, size = wx.Size( 500,343 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer37 = wx.BoxSizer( wx.VERTICAL )

		self.lihatJadwal = wx.StaticText( self, wx.ID_ANY, u"Lihat Jadwal", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lihatJadwal.Wrap( -1 )

		bSizer37.Add( self.lihatJadwal, 0, wx.ALL, 5 )

		bSizer38 = wx.BoxSizer( wx.VERTICAL )

		self.m_grid15 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid15.CreateGrid( 0, 5 )
		self.m_grid15.EnableEditing( True )
		self.m_grid15.EnableGridLines( True )
		self.m_grid15.EnableDragGridSize( False )
		self.m_grid15.SetMargins( 0, 0 )

		# Columns
		self.m_grid15.EnableDragColMove( False )
		self.m_grid15.EnableDragColSize( True )
		self.m_grid15.SetColLabelSize( 30 )
		self.m_grid15.SetColLabelValue( 0, u"Jadwal ID" )
		self.m_grid15.SetColLabelValue( 1, u"Tangki ID" )
		self.m_grid15.SetColLabelValue( 2, u"Lorong ID" )
		self.m_grid15.SetColLabelValue( 3, u"Penggunaan" )
		self.m_grid15.SetColLabelValue( 4, u"Tangki_Tanggal" )
		self.m_grid15.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid15.EnableDragRowSize( True )
		self.m_grid15.SetRowLabelSize( 80 )
		self.m_grid15.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid15.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer38.Add( self.m_grid15, 0, wx.ALL, 5 )

		bSizer39 = wx.BoxSizer( wx.VERTICAL )

		self.kembali = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer39.Add( self.kembali, 0, wx.ALL, 5 )


		bSizer38.Add( bSizer39, 1, wx.EXPAND, 5 )


		bSizer37.Add( bSizer38, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer37 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.kembali.Bind( wx.EVT_BUTTON, self.clickKembali )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def clickKembali( self, event ):
		event.Skip()


###########################################################################
## Class penambahanPenggunaanone
###########################################################################

class penambahanPenggunaanone ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Penambahan Penggunaan", pos = wx.DefaultPosition, size = wx.Size( 500,453 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer40 = wx.BoxSizer( wx.VERTICAL )

		self.penambahanPenggunaan = wx.StaticText( self, wx.ID_ANY, u"Penambahan Penggunaan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.penambahanPenggunaan.Wrap( -1 )

		bSizer40.Add( self.penambahanPenggunaan, 0, wx.ALL, 5 )

		bSizer41 = wx.BoxSizer( wx.VERTICAL )

		self.m_grid16 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid16.CreateGrid( 0, 2 )
		self.m_grid16.EnableEditing( True )
		self.m_grid16.EnableGridLines( True )
		self.m_grid16.EnableDragGridSize( False )
		self.m_grid16.SetMargins( 0, 0 )

		# Columns
		self.m_grid16.EnableDragColMove( False )
		self.m_grid16.EnableDragColSize( True )
		self.m_grid16.SetColLabelSize( 30 )
		self.m_grid16.SetColLabelValue( 0, u"Penghuni ID" )
		self.m_grid16.SetColLabelValue( 1, u"Nama Penghuni" )
		self.m_grid16.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid16.EnableDragRowSize( True )
		self.m_grid16.SetRowLabelSize( 80 )
		self.m_grid16.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid16.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer41.Add( self.m_grid16, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		fgSizer19 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer19.SetFlexibleDirection( wx.BOTH )
		fgSizer19.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.inputIDPenghuni = wx.StaticText( self, wx.ID_ANY, u"Inputkan ID Penghuni Anda", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.inputIDPenghuni.Wrap( -1 )

		fgSizer19.Add( self.inputIDPenghuni, 0, wx.ALL, 5 )

		self.m_textCtrl10 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer19.Add( self.m_textCtrl10, 0, wx.ALL, 5 )

		self.selanjutnya = wx.Button( self, wx.ID_ANY, u"Selanjutnya", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer19.Add( self.selanjutnya, 0, wx.ALL, 5 )


		bSizer41.Add( fgSizer19, 1, wx.EXPAND, 5 )


		bSizer40.Add( bSizer41, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer40 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.selanjutnya.Bind( wx.EVT_BUTTON, self.clickSelanjutnya )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def clickSelanjutnya( self, event ):
		event.Skip()


###########################################################################
## Class penambahanPenggunaantwo
###########################################################################

class penambahanPenggunaantwo ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Penambahan Penggunaan", pos = wx.DefaultPosition, size = wx.Size( 500,260 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer42 = wx.BoxSizer( wx.VERTICAL )

		self.PenambahanPenggunaan = wx.StaticText( self, wx.ID_ANY, u"Penambahan Penggunaan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PenambahanPenggunaan.Wrap( -1 )

		bSizer42.Add( self.PenambahanPenggunaan, 0, wx.ALL, 5 )

		bSizer43 = wx.BoxSizer( wx.VERTICAL )

		self.m_grid17 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid17.CreateGrid( 3, 2 )
		self.m_grid17.EnableEditing( True )
		self.m_grid17.EnableGridLines( True )
		self.m_grid17.EnableDragGridSize( False )
		self.m_grid17.SetMargins( 0, 0 )

		# Columns
		self.m_grid17.EnableDragColMove( False )
		self.m_grid17.EnableDragColSize( True )
		self.m_grid17.SetColLabelSize( 30 )
		self.m_grid17.SetColLabelValue( 0, u"Kategori ID" )
		self.m_grid17.SetColLabelValue( 1, u"Deskripsi" )
		self.m_grid17.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid17.EnableDragRowSize( True )
		self.m_grid17.SetRowLabelSize( 80 )
		self.m_grid17.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid17.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer43.Add( self.m_grid17, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		fgSizer20 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer20.SetFlexibleDirection( wx.BOTH )
		fgSizer20.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.inputPenggunaan = wx.StaticText( self, wx.ID_ANY, u"Inputkan Kategori Penggunaan Anda", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.inputPenggunaan.Wrap( -1 )

		fgSizer20.Add( self.inputPenggunaan, 0, wx.ALL, 5 )

		self.m_textCtrl11 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer20.Add( self.m_textCtrl11, 0, wx.ALL, 5 )

		self.selesai = wx.Button( self, wx.ID_ANY, u"Selesai", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer20.Add( self.selesai, 0, wx.ALL, 5 )


		bSizer43.Add( fgSizer20, 1, wx.EXPAND, 5 )


		bSizer42.Add( bSizer43, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer42 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.selesai.Bind( wx.EVT_BUTTON, self.clickSelesai )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def clickSelesai( self, event ):
		event.Skip()


