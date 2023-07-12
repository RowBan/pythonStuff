
import numpy as np
import win32gui, win32ui, win32con


class WindowCapture:
    
    # Properties
    w = 0
    h = 0
    hwnd = None
    croppedx = 0
    croppedy = 0
    offsetx = 0
    offsety = 0
    
    # Constructor
    def __init__(self, window_name=None):
        
        if window_name is None:
            self.hwnd = win32gui.GetDesktopWindow()
        else:        
            #Find the handle for the game window
            self.hwnd = win32gui.FindWindow(None, window_name)
            if not self.hwnd:
                raise Exception('Window not found: {}'.format(window_name))
        
        # Define screen resolution
        window = win32gui.GetWindowRect(self.hwnd)
        self.w = window[2] - window[0]
        self.h = window[3] - window[1]
        
        # Account for window border and titlebar, crop out
        borderpixels = 8
        titlepixels = 30
        self.w = self.w - (borderpixels * 2)
        self.h = self.h - titlepixels - borderpixels
        
        #shift screen to account for cropped pixels
        self.croppedx = borderpixels
        self.croppedy = titlepixels
        
        # set the cropped coordinates offset so we can translate
        # screenshot images into actual positions
        self.offsetx = window[0] + self.croppedx
        self.offsety = window[1] + self.croppedy
        
    
    def getScreenshot(self):
        
        # Get the Window image data
        wDC = win32gui.GetWindowDC(self.hwnd)
        dcObj = win32ui.CreateDCFromHandle(wDC)
        cDC = dcObj.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj, self.w, self.h)
        cDC.SelectObject(dataBitMap)
        cDC.BitBlt((0, 0), (self.w, self.h), dcObj, (self.croppedx, self.croppedy), win32con.SRCCOPY)
        
        #save screenshot
        signedIntsArray = dataBitMap.GetBitmapBits(True)
        img = np.fromstring(signedIntsArray, dtype='uint8')
        img.shape = (self.h, self.w, 4)
        
        # Free up resources
        dcObj.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(self.hwnd, wDC)
        win32gui.DeleteObject(dataBitMap.GetHandle())
        
        # Get rid of alpa channel
        img = img[...,:3]
        
        # make image C_CONTIGUOUS for overlay
        img = np.ascontiguousarray(img)
        
        return img
    
    @staticmethod
    def window_names():
        def winEnumHandler(hwnd, ctx):
            if win32gui.IsWindowVisible(hwnd):
                print(hex(hwnd), win32gui.GetWindowText(hwnd))
        win32gui.EnumWindows(winEnumHandler, None)
        
    def screen_pos(self, pos):
        return(pos[0] + self.offsetx, pos[1] + self.offsety)