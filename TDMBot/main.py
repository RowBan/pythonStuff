import cv2 as cv
from time import time
from windowcap import WindowCapture

#WindowCapture.window_names()

wincap = WindowCapture('Paladins (64-bit, DX11)')


# FPS Meter start
loop_time = time()
while(True):
    
    screenshot = wincap.getScreenshot()
    
    cv.imshow('Computer Vision', screenshot)
    
    # FPS Meter end
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()
    
    # press q with the output window focused to exit.
    # waits 1 ms every loop to check for keypresses
    if cv.waitKey(1) == ord('q'):
        break


cv.destroyAllWindows
print('Done')