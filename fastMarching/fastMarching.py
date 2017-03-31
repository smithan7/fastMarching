from fmm import FMM
import numpy as np
import cv2

map = np.zeros( (100, 100), np.uint8)
cv2.circle( map, (50, 25), 10, 255, -1)
cv2.circle( map, (10, 50), 10, 255, -1)
cv2.circle( map, (50, 50), 10, 255, -1)
      
start = [1,1]
goal = [90,90]

### for some reason the plotted path is flipped x and y, no clue as the time plot is perfect, probably in findPath

fmm = FMM( map, 1.0, 1.0, start, goal )
#fmm.displayMap()
fmm.inflateWalls_to_crashRadius()
fmm.inflateWalls_to_inflationRadius()
#fmm.displaySpeedMap()

fmm.wavePropagation( start, goal )
fmm.wavePropagation( start, [10, 80] )
#fmm.displayTime()

path = fmm.findPath(start, goal)
fmm.displayPath_over_map( path )
cv2.waitKey(0)
