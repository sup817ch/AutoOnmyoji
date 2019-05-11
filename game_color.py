class GameColor():
    '''
    region:((x1,y1),(x2,y2))
        搜索区域
    color:(r,g,b)
        欲搜索的颜色
    '''
    def __init__(self,region,color,tolerance=0):
        self.region=region
        self.color=color
        self.tolerance=tolerance

class TansuoColor():
    exp_icon=GameColor(((2,205),(1127,545)),(46,112,126),2) #怪物经验图标
    ready_btn=GameColor(((1006,526),(1058,549)),(242,215,165),0) #准备按钮变亮时
    man1_icon=GameColor(((380,200),(480,400)),(251,237,2),3) #狗粮1满经验
    man2_icon=GameColor(((630,250),(730,450)),(251,237,2),3) #狗粮2满经验