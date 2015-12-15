__author__ = 'Administrator'

from pico2d import *

PlayerName = None

class UI:
    name = None
    Type = 0
    gold = 0
    boss_time = 30.0
    GameLevel = 0

    WeaponLevel = 0
    ArmorLevel = 0
    WeaponImage = list()
    WeaponIngame = list()
    MapImage = list()

    ArmorGauge = 0
    Bomb = 0
    item = None
    ArmorImage = None

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 4

    LEFT_RUN, RIGHT_RUN, STAND, UP_RUN, DOWN_RUN = 0, 1, 2, 3, 4
    font = None

    get_coin = None

    def __init__(self, name):
        UI.boss_time = 30.0

        if name != None:
            UI.name = name
        self.x, self.y = 192, 60
        self.frame = 0
        self.total_frames = 0
        self.state = self.STAND
        self.xSize = 128/2
        self.ySize = 106/2
        self.get_coin = load_wav('get_coin.wav')
        self.get_coin.set_volume(32)

    def Init(none):
        UI.WeaponLevel = 0
        UI.ArmorLevel = 0
        UI.gold = 200
        UI.boss_time = 30.0
        UI.GameLevel = 0
        UI.Bomb = 0

    def __del__(self):
        pass
        #UI.DeleteImage(None)

    def DeleteImage(none):
        for i in UI.WeaponImage :
            UI.WeaponImage.remove(i)
            del(i)
        del(UI.WeaponImage)

        for i in UI.WeaponIngame :
            UI.WeaponIngame.remove(i)
            del(i)
        del(UI.WeaponIngame)

        for i in UI.MapImage:
            UI.MapImage.remove(i)
            del(i)
        del(UI.MapImage)

        del(UI.ArmorImage)

    def MakeImage(none):
        UI.DeleteImage(None)
        UI.WeaponIngame = list()
        UI.WeaponImage = list()
        UI.MapImage = list()
        if UI.font == None:
            UI.font = load_font('ConsolaMalgun.ttf')

        UI.WeaponImage.append(load_image('item1_1.png'))
        UI.WeaponImage.append(load_image('item2_1.png'))
        UI.WeaponImage.append(load_image('item1_2.png'))
        UI.WeaponImage.append(load_image('item2_2.png'))

        UI.WeaponIngame.append(load_image('bullet_sunny.png'))
        UI.WeaponIngame.append(load_image('bullet_raby.png'))
        UI.WeaponIngame.append(load_image('bullet_sunny_two.png'))
        UI.WeaponIngame.append(load_image('bullet_raby_two.png'))
        UI.WeaponIngame.append(load_image('bullet_sunny_three.png'))
        UI.WeaponIngame.append(load_image('bullet_raby_three.png'))

        UI.ArmorImage = load_image('shield.png')

        UI.MapImage.append(load_image('01.png'))
        UI.MapImage.append(load_image('02.png'))
        UI.MapImage.append(load_image('03.png'))
        UI.MapImage.append(load_image('04.png'))
        UI.MapImage.append(load_image('05.png'))

    def draw_font(frame_time):
        UI.font.draw(20, 780, "GOLD: %d, ArmorGauge: %d, Bomb: %d, Time: %f" % (UI.gold, UI.ArmorGauge, UI.Bomb, get_time()), (255,255,255))

    def draw(frame_time):
        UI.draw_font(frame_time)

    def AddArmor(none):
        if UI.gold >= 50:
            UI.gold -= 50
            UI.ArmorGauge += 1
            print("아머게이지 증가", UI.ArmorGauge)

    def AddBomb(none):
        if UI.gold >= 100:
            UI.gold -= 100
            UI.Bomb += 1
            print("폭탄 증가", UI.Bomb)

    def ChangeWeapon(Image):
        if UI.WeaponLevel > 0:
            Image =  UI.WeaponImage[(UI.Type % 2) + (2 * (UI.WeaponLevel-1))]
            return Image
        return None

    def GetWeaponInGame(none):
        return UI.WeaponIngame[(UI.Type % 2) + (2 * (UI.WeaponLevel))]

    def AddGold(money):
        global get_coin
        UI.gold += money
        print(UI.gold)

    def GetMapImage(none):
        return UI.MapImage[(UI.GameLevel)%5]

#self 쓰지말것*****************************************************************************
    def BuyItem(items):
        UI.item = items

    def Update(frame_time):
        if UI.boss_time > 0 :
            UI.boss_time -= frame_time

    def InitBoss(null):
        if UI.boss_time < 0 and UI.boss_time != -100:
            UI.boss_time = -100
            return True
        return False

    def handle_event(self, event):
        pass


def ItemBuy(type, Image):
    tempImage = Image
    cost = (UI.WeaponLevel + 50)
    if UI.WeaponLevel >= 1:
        cost = UI.WeaponLevel * 100
    if type == 'weapon' and UI.gold >= cost and UI.WeaponLevel < 2:
        UI.WeaponLevel += 1
        UI.gold -= cost
        return UI.ChangeWeapon(Image)

    return tempImage