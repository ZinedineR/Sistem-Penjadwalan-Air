# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class loginPage
###########################################################################

class loginPage ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,227 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.plaintext = wx.StaticText( self, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.plaintext.Wrap( -1 )

		bSizer1.Add( self.plaintext, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		sbSizer11 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"password" ), wx.VERTICAL )

		self.text_password = wx.TextCtrl( sbSizer11.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

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

	def __del__( self ):
		pass


