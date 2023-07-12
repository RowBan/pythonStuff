import cv2 as cv
import numpy as np

class Vision:
    width = 0
    height = 0
    method = 0
    result = 0
    
    def findClickPos(needle, haystack, threshhold=0.9, debug_mode=None):
        needle = cv.imread(needle, cv.IMREAD_UNCHANGED)
        
        # Dimensions of Needle
        width = needle.shape[1]
        height = needle.shape[0]
        
        # Methods for comparing images
        method = cv.TM_CCOEFF_NORMED
        result = cv.matchTemplate(haystack, needle, method)
        
        # Get all positions on screen matching fed image
        locations = np.where(result >= threshhold)
        
        # Unpack locations, repack as x,y tuple
        locations = list(zip(*locations[::-1]))
        
        rectangles = []
        for loc in locations:
            rectangle = [int(loc[0]), int(loc[1]), width, height]
            rectangles.append(rectangle)
            rectangles.append(rectangle)
            
            if debug_mode == 'rectangles':
                # Determine box position
                top_left = (x, y)
                bottom_left = (x + w, y + h)