import wx
from wx import *
app = wx.App()
win = wx.Frame(None,title = 'Simple',size = (410,335))
win.Show()
loadbtn = wx.Button(win,label = 'Open',pos = (225,5),size = (80,25))
savebtn = wx.Button(win, label = 'Save',pos =(315,5),size = (80,25))
filename = wx.TextCtrl(win,pos(5,5),size = (210,5))
contents = wx.TextCtrl(win,pos =(5,35),size = (390,260),style = wx.TE_MULTILINE | wx.HSCROLL )
app.MainLoop()
