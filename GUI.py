from tkinter import *
from tkinter import ttk

GUI_WIDTH = 1200
GUI_HEIGHT = 1000

class VerticalScrolledFrame(Frame):

    def __init__(self, parent, *args, **kw):
        Frame.__init__(self, parent, *args, **kw)            

        # create a canvas object and a vertical scrollbar for scrolling it
        vscrollbar = Scrollbar(self, orient=VERTICAL)
        vscrollbar.pack(fill=Y, side=RIGHT, expand=TRUE)
        canvas = Canvas(self, bd=0, highlightthickness=0,
                        yscrollcommand=vscrollbar.set, height = GUI_HEIGHT - 100, width = GUI_WIDTH / 6)
        canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
        vscrollbar.config(command=canvas.yview)

        # reset the view
        canvas.xview_moveto(0)
        canvas.yview_moveto(0)

        # create a frame inside the canvas which will be scrolled with it
        self.interior = interior = Frame(canvas)
        interior_id = canvas.create_window(0, 0, window=interior,
                                           anchor=NW)

        # track changes to the canvas and frame width and sync them,
        # also updating the scrollbar
        def _configure_interior(event):
            # update the scrollbars to match the size of the inner frame
            size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
            canvas.config(scrollregion="0 0 %s %s" % size)
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the canvas's width to fit the inner frame
                canvas.config(width=interior.winfo_reqwidth())
        interior.bind('<Configure>', _configure_interior)
        def _configure_canvas(event):
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the inner frame's width to fill the canvas
                canvas.itemconfigure(interior_id, width=canvas.winfo_width())
        canvas.bind('<Configure>', _configure_canvas)


def startUP():
    root = Tk()
    panedWindow = ttk.Panedwindow(root, orient = HORIZONTAL, width = GUI_WIDTH, height = GUI_HEIGHT)
    panedWindow.pack(fill = BOTH, expand = True)
    frame1 = ttk.Frame(panedWindow, width = GUI_WIDTH / 6, height = GUI_HEIGHT, relief = SUNKEN)
    frame2 = ttk.Frame(panedWindow, width = GUI_WIDTH * 5 / 6, height = GUI_HEIGHT, relief = SUNKEN)
    
    panedWindow.add(frame1, weight = 1)
    panedWindow.add(frame2, weight = 4)
    label1 = ttk.Label(frame1, text = "モンスター情報")
    label2 = ttk.Label(frame1, text = "クエスト情報")
    label3 = ttk.Label(frame1, text = "採取情報")
    empty_line = ttk.Label(frame1, text = "")
    top = ttk.Button(frame1, text = "TOPページ")
    skill_calculator = ttk.Button(frame1, text = "スキルシミュレータ")
    damage_calculator = ttk.Button(frame1, text = "ダメージシミュレータ")
    weapons = ttk.Button(frame1, text = "武器一覧", command = lambda: weapon_button_action(frame2))
    armor = ttk.Button(frame1, text = "防具一覧")
    loot_info = ttk.Button(frame1, text = "剥ぎ取り")
    old_quests = ttk.Button(frame1, text = "下位/上位/凄腕")
    new_quests = ttk.Button(frame1, text = "Ｇ")
    old_loot = ttk.Button(frame1, text = "G ")
    item_search = ttk.Button(frame1, text = "素材検索")
    armor_search = ttk.Button(frame1, text = "装備")
    food_info = ttk.Button(frame1, text = "食事一覧")
    special = ttk.Button(frame1, text = "くじ/特別報酬")
    my_garden = ttk.Button(frame1, text = "マイガーデン")
    my_cat = ttk.Button(frame1, text = "マイトレ")
    my_gallary = ttk.Button(frame1, text = "マイギャラリー")
    my_support = ttk.Button(frame1, text = "マイサポート")
    my_mission = ttk.Button(frame1, text = "マイミッション")
    
    top.pack(fill = X)
    skill_calculator.pack()
    damage_calculator.pack()
    weapons.pack()
    armor.pack()
    label1.pack()
    loot_info.pack()
    label2.pack()
    old_quests.pack()
    new_quests.pack()
    label3.pack()
    old_loot.pack()
    empty_line.pack()
    item_search.pack()
    food_info.pack()
    my_garden.pack()
    my_cat.pack()
    my_gallary.pack()
    my_support.pack()
    my_mission.pack()

def weapon_button_action(frame):
    if len(frame.winfo_children()) == 0:
        frame_width = GUI_WIDTH * 5 / 6
        weapon_frame = ttk.Frame(frame, width = GUI_WIDTH * 5 / 6, height = GUI_HEIGHT / 10, relief = SUNKEN)
        weapon_frame.grid(row = 0, column = 0, columnspan = 10)
        great_sword = ttk.Button(weapon_frame, text = "大剣", width = frame_width / 24).grid(row = 0, column = 0)
        great_sword_G = ttk.Button(weapon_frame, text = "G", width = frame_width / 24).grid(row = 0, column = 1)
        great_sword_involve = ttk.Button(weapon_frame, text = "進化", width = frame_width / 24).grid(row = 1, column = 0)
        great_sword_cat = ttk.Button(weapon_frame, text = "猫", width = frame_width / 24).grid(row = 1, column = 1)
        tachi = ttk.Button(weapon_frame, text = "太刀", width = frame_width / 24).grid(row = 0, column = 2)
        tachi_G = ttk.Button(weapon_frame, text = "G", width = frame_width / 24).grid(row = 0, column = 3)
        tachi_involve = ttk.Button(weapon_frame, text = "進化", width = frame_width / 24).grid(row = 1, column = 2)
        tachi_cat = ttk.Button(weapon_frame, text = "猫", width = frame_width / 24).grid(row = 1, column = 3)
        sword_shield = ttk.Button(weapon_frame, text = "片手剣", width = frame_width / 24).grid(row = 0, column = 4)
        sword_shield_G = ttk.Button(weapon_frame, text = "G", width = frame_width / 24).grid(row = 0, column = 5)
        sword_shield_involve = ttk.Button(weapon_frame, text = "進化", width = frame_width / 24).grid(row = 1, column = 4)
        sword_shield_cat = ttk.Button(weapon_frame, text = "猫", width = frame_width / 24).grid(row = 1, column = 5)
        double_sword = ttk.Button(weapon_frame, text = "双剣", width = frame_width / 24).grid(row = 0, column = 6)
        double_sword_G = ttk.Button(weapon_frame, text = "G", width = frame_width / 24).grid(row = 0, column = 7)
        double_sword_involve = ttk.Button(weapon_frame, text = "進化", width = frame_width / 24).grid(row = 1, column = 6)
        double_sword_cat = ttk.Button(weapon_frame, text = "猫", width = frame_width / 24).grid(row = 1, column = 7)
        hammer = ttk.Button(weapon_frame, text = "ハンマー", width = frame_width / 24).grid(row = 0, column = 8)
        hammer_G = ttk.Button(weapon_frame, text = "G", width = frame_width / 24).grid(row = 0, column = 9)
        hammer_involve = ttk.Button(weapon_frame, text = "進化", width = frame_width / 24).grid(row = 1, column = 8)
        hammer_cat = ttk.Button(weapon_frame, text = "猫", width = frame_width / 24).grid(row = 1, column = 9)
        horn = ttk.Button(weapon_frame, text = "狩猟笛", width = frame_width / 24).grid(row = 0, column = 10)
        horn_G = ttk.Button(weapon_frame, text = "G", width = frame_width / 24).grid(row = 0, column = 11)
        horn_involve = ttk.Button(weapon_frame, text = "進化", width = frame_width / 24).grid(row = 1, column = 10)
        horn_cat = ttk.Button(weapon_frame, text = "猫", width = frame_width / 24).grid(row = 1, column = 11)
        lance = ttk.Button(weapon_frame, text = "ランス", width = frame_width / 24).grid(row = 0, column = 12)
        lance_G = ttk.Button(weapon_frame, text = "G", width = frame_width / 24).grid(row = 0, column = 13)
        lance_involve = ttk.Button(weapon_frame, text = "進化", width = frame_width / 24).grid(row = 1, column = 12)
        lance_cat = ttk.Button(weapon_frame, text = "猫", width = frame_width / 24).grid(row = 1, column = 13)
        gunlance = ttk.Button(weapon_frame, text = "ガンランス", width = frame_width / 24).grid(row = 0, column = 14)
        gunlance_G = ttk.Button(weapon_frame, text = "G", width = frame_width / 24).grid(row = 0, column = 15)
        gunlance_involve = ttk.Button(weapon_frame, text = "進化", width = frame_width / 24).grid(row = 1, column = 14)
        gunlance_cat = ttk.Button(weapon_frame, text = "猫", width = frame_width / 24).grid(row = 1, column = 15)
        tonfa = ttk.Button(weapon_frame, text = "穿龍棍", width = frame_width / 24, command = lambda: display_weapons(frame)).grid(row = 0, column = 16)
        tonfa_G = ttk.Button(weapon_frame, text = "G", width = frame_width / 24).grid(row = 0, column = 17)
        light = ttk.Button(weapon_frame, text = "ライト", width = frame_width / 24).grid(row = 0, column = 18)
        light_G = ttk.Button(weapon_frame, text = "G", width = frame_width / 24).grid(row = 0, column = 19)
        light_involve = ttk.Button(weapon_frame, text = "進化", width = frame_width / 24).grid(row = 1, column = 18)
        light_cat = ttk.Button(weapon_frame, text = "猫", width = frame_width / 24).grid(row = 1, column = 19)
        heavy = ttk.Button(weapon_frame, text = "ヘビィ", width = frame_width / 24).grid(row = 0, column = 20)
        heavy_G = ttk.Button(weapon_frame, text = "G", width = frame_width / 24).grid(row = 0, column = 21)
        heavy_involve = ttk.Button(weapon_frame, text = "進化", width = frame_width / 24).grid(row = 1, column = 20)
        heavy_cat = ttk.Button(weapon_frame, text = "猫", width = frame_width / 24).grid(row = 1, column = 21)
        bow = ttk.Button(weapon_frame, text = "弓", width = frame_width / 24).grid(row = 0, column = 22)
        bow_G = ttk.Button(weapon_frame, text = "G", width = frame_width / 24).grid(row = 0, column = 23)
        bow_involve = ttk.Button(weapon_frame, text = "進化", width = frame_width / 24).grid(row = 1, column = 22)
        bow_cat = ttk.Button(weapon_frame, text = "猫", width = frame_width / 24).grid(row = 1, column = 23)

    
def display_weapons(frame):
    file = open("tonf_names.txt", 'r')
    reg = []
    G = []
    S = []
    W = []
    N = []
    T = []
    E = []
    inFrame = VerticalScrolledFrame(frame, height = GUI_HEIGHT * 8 / 10, width = GUI_WIDTH / 6)
    inFrame.grid(row = 5, column = 0, rowspan = 50)
    data = file.readlines()
    for i in range(len(data) // 5 + 1):
        if data[i * 5][0] == "G":
            G.append(ttk.Button(inFrame.interior, text = data[i * 5].strip()))
        elif data[i * 5][0] == "S":
            S.append(ttk.Button(inFrame.interior, text = data[i * 5].strip()))
        elif data[i * 5][0] == "W":
            W.append(ttk.Button(inFrame.interior, text = data[i * 5].strip()))
        elif data[i * 5][0] == "N":
            N.append(ttk.Button(inFrame.interior, text = data[i * 5].strip()))
        elif data[i * 5][0] == "T":
            T.append(ttk.Button(inFrame.interior, text = data[i * 5].strip()))
        elif data[i * 5][0] == "E":
            E.append(ttk.Button(inFrame.interior, text = data[i * 5].strip()))
        else:
            reg.append(ttk.Button(inFrame.interior, text = data[i * 5].strip()))
    print(len(T))
    for i in range(len(reg)):
        reg[i].pack(fill = X)
    ttk.Label(inFrame.interior, text = "・歌姫").pack()
    for i in range(len(G)):
        G[i].pack(fill = X)
    ttk.Label(inFrame.interior, text = "・狩人祭").pack()
    for i in range(len(S)):
        S[i].pack(fill = X)
    ttk.Label(inFrame.interior, text = "・韋駄天").pack()
    for i in range(len(W)):
        W[i].pack(fill = X)
    ttk.Label(inFrame.interior, text = "・カフェ").pack()
    for i in range(len(N)):
        N[i].pack(fill = X)
    ttk.Label(inFrame.interior, text = "・天廊").pack()
    for i in range(len(T)):
        T[i].pack(fill = X)
    ttk.Label(inFrame.interior, text = "・イベント").pack()
    for i in range(len(E)):
        E[i].pack(fill = X)
            
        
    
        
    
startUP()



