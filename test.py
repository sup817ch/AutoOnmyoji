import cv2
import os
import game_ctl
import win32gui
import time
import find_color as fd

'''
img_src = cv2.imread('test2.png', 0)
img_template = cv2.imread('exp.png', 0)
res = cv2.matchTemplate(img_src, img_template, cv2.TM_CCOEFF_NORMED)
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(res)
'''

yys=game_ctl.GameControl(u'阴阳师-网易游戏')
yys.active_window()
img_part=yys.window_part_shot((4,173),(1123,559))
x,y=fd.find_color(img_part,[43,103,119],1)
yys.mouse_move((x+4,y+173))
#yys.mouse_click()
print(x, y)
