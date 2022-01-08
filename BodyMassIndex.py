import wx


#class frame 
class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title =title, size = (600, 400))
        
        #Create a white panel so it doesnt look ugly
        panel = wx.Panel(self)
        panel.SetSize((600, 400))
        
        panel.label = wx.StaticText(panel, label = "Body Mass Index:  ")

        btn = wx.Button(panel, label = "Close", pos = (230, 250))

        self.Bind(wx.EVT_BUTTON, self.OnCloseMe, btn)
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
        
        btn2 = wx.Button(panel, label = "Calculate", pos = (320, 250))
        panel.Bind(wx.EVT_BUTTON, self.Calculate, btn2)
        
        #The first spinner is for the weight
        self.spinControl = wx.SpinCtrl(panel, -1, "", (300, 100))
        self.spinControl.SetRange(1, 300)
        self.spinControl.SetValue(1)

        self.label = wx.StaticText(panel, label = "Weight:", pos = (30,100))
        
        #The second spinner is for the height
        self.spinControl2 = wx.SpinCtrl(panel, -1, "", (300, 200))
        self.spinControl2.SetRange(1, 300)
        self.spinControl2.SetValue(1)

        self.label = wx.StaticText(panel, label = "Height", pos = (30,200))

           #the link between the closing window function and the button
    def OnCloseMe(self, event):
        self.Close(True)
       #Function that closes the window
    def OnCloseWindow(self, event):
        self.Destroy()
        
    #function that calculates the Body mass index
    def Calculate(self,event):
        spinVal_1 = self.spinControl.GetValue()
        spinVal_2 = self.spinControl2.GetValue()
        bmi = round((spinVal_1 / ((spinVal_2)*(spinVal_2))) * 10000,2)
        self.label  = wx.StaticText(self, label = "BMI is: " + str(bmi) + ".", pos =(300,150)) 
        
class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(parent=None, title="Spin Control")
        self.frame.Show()
        return True

app = MyApp()
app.MainLoop() 