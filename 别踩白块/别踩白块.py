import pyautogui
import wx
import time
def run(event):
    time.sleep(3)
    t = 0.05
    while True:
        if pyautogui.pixelMatchesColor(960, 530, (29, 29, 29)):
            pyautogui.moveTo(960, 530, duration=t)
            pyautogui.click(960, 530)
        if pyautogui.pixelMatchesColor(1060, 530, (29, 29, 29)):
            pyautogui.moveTo(1060, 530, duration=t)
            pyautogui.click(1060, 530)
        if pyautogui.pixelMatchesColor(1160, 530, (29, 29, 29)):
            pyautogui.moveTo(1160, 530, duration=t)
            pyautogui.click(1160, 530)
        if pyautogui.pixelMatchesColor(1260, 530, (29, 29, 29)):
            pyautogui.moveTo(1260, 530, duration=t)
            pyautogui.click(1260, 530)

app = wx.App()
win = wx.Frame(None, title="别踩白块外挂", size=(300, 200))
bkg = wx.Panel(win)
runButton = wx.Button(bkg, label="运行", pos=(100, 70), size=(100, 30))
runButton.Bind(wx.EVT_BUTTON, run)

win.Show()
app.MainLoop()