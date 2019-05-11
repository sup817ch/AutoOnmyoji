import sys
import game_ctl
import time
from game_pos import *
from game_color import *

yys=None #game_ctl初始化
fight_count=0 #战斗次数统计

def find_exp_monster():
    exp_pos=yys.find_color(TansuoColor.exp_icon.region,TansuoColor.exp_icon.color,TansuoColor.exp_icon.tolerance)
    if exp_pos==-1:
        return -1
    fight_pos=yys.find_color(((exp_pos[0]-150,exp_pos[1]-250),(exp_pos[0]+150,exp_pos[1]-50)),(35,38,84),3)
    if fight_pos==-1:
        return -1
    return fight_pos
    
def next_scene():
    yys.mouse_drag_bg((1130,118),(20,118))
    yys.mouse_drag_bg((1130,118),(20,118))

def check_exp_full():
    gouliang1=False
    gouliang2=False
    if yys.find_color(TansuoColor.man1_icon.region,TansuoColor.man1_icon.color,TansuoColor.man1_icon.tolerance)!=-1:
        gouliang1=True
    if yys.find_color(TansuoColor.man2_icon.region,TansuoColor.man2_icon.color,TansuoColor.man2_icon.tolerance)!=-1:
        gouliang2=True
    if not gouliang1 and not gouliang2:
        return
    #开始换狗粮
    while True:
        yys.mouse_click_bg(TansuoPos.change_monster.pos,TansuoPos.change_monster.pos_end)
        if yys.wait_game_img('img\\quanbu_btn.png',3,False):
            break
    time.sleep(2)
    yys.mouse_click_bg(TansuoPos.quanbu_btn.pos,TansuoPos.quanbu_btn.pos_end)
    time.sleep(1)
    yys.mouse_click_bg(TansuoPos.n_tab_btn.pos,TansuoPos.n_tab_btn.pos_end)
    time.sleep(1)
    if gouliang1:
        yys.mouse_drag_bg((309,520),(554,315))
    if gouliang2:
        time.sleep(1)
        yys.mouse_drag_bg((191,520),(187,315))

def fight_monster():
    while True:
        global fight_count
        yys.wait_game_img('img\\house.png')
        fight_pos=find_exp_monster()
        if fight_pos==-1:
            break
        yys.mouse_click_bg(fight_pos)
        if not yys.wait_game_color(TansuoColor.ready_btn.region,TansuoColor.ready_btn.color,TansuoColor.ready_btn.tolerance,quit=False):
            break
        fight_count+=1
        print('进入战斗 战斗次数%d' % fight_count)
        check_exp_full()
        while True:
            if yys.wait_game_img('img\\fight_end.png',2,False):
                break
            yys.mouse_click_bg(TansuoPos.ready_btn.pos,TansuoPos.ready_btn.pos_end)
        time.sleep(1)
        yys.mouse_click_bg(TansuoPos.fight_quit.pos,TansuoPos.fight_quit.pos_end)
        time.sleep(1)
        
def tansuo_loop():
    while True:
        yys.wait_game_img('img\\ts_btn.png')
        yys.mouse_click_bg(TansuoPos.tansuo_btn.pos,TansuoPos.tansuo_btn.pos_end)
        fight_monster()
        next_scene()
        fight_monster()
        while True:
            yys.mouse_click_bg(TansuoPos.quit_btn.pos,TansuoPos.quit_btn.pos_end)
            if yys.wait_game_img('img\\confirm_quit.png',3,False):
                break
        yys.mouse_click_bg(TansuoPos.confirm_btn.pos,TansuoPos.confirm_btn.pos_end)
        

def main():
    global yys
    yys=game_ctl.GameControl(u'阴阳师-网易游戏')
    yys.activate_window()
    time.sleep(1) #防止截图失败
    tansuo_loop()
    

if __name__=='__main__':
    main()