from pygame import Surface,init,mixer,image,Color,transform,math,font

init()
mixer.init()
class SpriteSheet:
    def __init__(self, filename):
        self.spritesheet = image.load(filename)
    def get_image(self, x, y, width, height):
        image = Surface((width, height))
        image.blit(self.spritesheet, (0, 0), (x, y, width, height))
        image.set_colorkey(Color('black'))
        return image
#cac bien luu cac thong so se duoc viet hoa
FPS=60
TITLE='MINI GAME'
SIZE_EASY=3
SIZE_NORMAL=4
SIZE_HARD=5
SIZE_INSANE=6
SIZE_DESTROY=7
WIDTH_GAME=420
HEIGH_GAME=420
WIDTH=700
HEIGHT=544
POS_GAME=[60,60]
ICON=transform.scale(image.load('image/icon.jpg'),(30,30))
EVENT=['left','up','right','down']
BUTTON=SpriteSheet('image/button.png')
LOLRANK=SpriteSheet('image/lolrank.png')
MOVE=SpriteSheet('image/move.png')
CHECK=SpriteSheet('image/check.png')
EASY_IMG=[[],[],[],[]]
NORMAL_IMG=[[],[],[],[]]
HARD_IMG=[[],[],[],[]]
INSANE_IMG=[[],[],[],[]]
DESTROY_IMG=[[],[],[],[]]
EASY=[]
NORMAL=[]
HARD=[]
INSANE=[]
DESTROY=[]
LEVEL_IMG=[]
IMG=[]
IMG1=[]
for count in range(1,5):
    EASY.append(SpriteSheet('image/lol/EASY{}.png'.format(count)))
    NORMAL.append(SpriteSheet('image/lol/NORMAL{}.png'.format(count)))
    HARD.append(SpriteSheet('image/lol/HARD{}.png'.format(count)))
    INSANE.append(SpriteSheet('image/lol/INSANE{}.png'.format(count)))
    DESTROY.append(SpriteSheet('image/lol/DESTROY{}.png'.format(count)))
    #luu anh cua mang

    for i in range(SIZE_EASY*SIZE_EASY-1):
        EASY_IMG[count-1].append(EASY[count-1].get_image((i%SIZE_EASY)*(WIDTH_GAME//SIZE_EASY),(i//SIZE_EASY)*(HEIGH_GAME//SIZE_EASY),WIDTH_GAME//SIZE_EASY,HEIGH_GAME//SIZE_EASY))
    for i in range(SIZE_NORMAL*SIZE_NORMAL-1):
        NORMAL_IMG[count-1].append(NORMAL[count-1].get_image((i%SIZE_NORMAL)*(WIDTH_GAME//SIZE_NORMAL),i//SIZE_NORMAL*(HEIGH_GAME//SIZE_NORMAL),WIDTH_GAME//SIZE_NORMAL,HEIGH_GAME//SIZE_NORMAL))

    for i in range(SIZE_HARD*SIZE_HARD-1):
        HARD_IMG[count-1].append(HARD[count-1].get_image((i%SIZE_HARD)*(WIDTH_GAME//SIZE_HARD),i//SIZE_HARD*(HEIGH_GAME//SIZE_HARD),WIDTH_GAME//SIZE_HARD,HEIGH_GAME//SIZE_HARD))

    for i in range(SIZE_INSANE*SIZE_INSANE-1):
        INSANE_IMG[count-1].append(INSANE[count-1].get_image((i%SIZE_INSANE)*(WIDTH_GAME//SIZE_INSANE),i//SIZE_INSANE*(HEIGH_GAME//SIZE_INSANE),WIDTH_GAME//SIZE_INSANE,HEIGH_GAME//SIZE_INSANE))

    for i in range(SIZE_DESTROY*SIZE_DESTROY-1):
        DESTROY_IMG[count-1].append(DESTROY[count-1].get_image((i%SIZE_DESTROY)*(WIDTH_GAME//SIZE_DESTROY),i//SIZE_DESTROY*(HEIGH_GAME//SIZE_DESTROY),WIDTH_GAME//SIZE_DESTROY,HEIGH_GAME//SIZE_DESTROY))

    LEVEL_IMG.append([EASY_IMG[count-1],NORMAL_IMG[count-1],HARD_IMG[count-1],INSANE_IMG[count-1],DESTROY_IMG[count-1]])
    IMG.append([transform.scale(image.load('image/lol/EASY{}.png'.format(count)),(200,200)),
         transform.scale(image.load('image/lol/NORMAL{}.png'.format(count)),(200,200)),
         transform.scale(image.load('image/lol/HARD{}.png'.format(count)),(200,200)),
         transform.scale(image.load('image/lol/INSANE{}.png'.format(count)),(200,200)),
         transform.scale(image.load('image/lol/DESTROY{}.png'.format(count)),(200,200))])
    IMG1.append([transform.scale(image.load('image/lol/EASY{}.png'.format(count)), (300, 300)),
                transform.scale(image.load('image/lol/NORMAL{}.png'.format(count)), (300, 300)),
                transform.scale(image.load('image/lol/HARD{}.png'.format(count)), (300, 300)),
                transform.scale(image.load('image/lol/INSANE{}.png'.format(count)), (300, 300)),
                transform.scale(image.load('image/lol/DESTROY{}.png'.format(count)), (300, 300))])

KHUNG=transform.scale(image.load('image/lol/2.png'),(330,320))

RANK_IMG=[]
for i in range(7):
    RANK_IMG.append(LOLRANK.get_image(i*90,0,90,70))
RECORD=image.load('image/record.png')
RECORDCLICK=image.load('image/recordclick.png')
MOUSE=image.load('image/mouse.png')
MOUSECLICK=image.load('image/mouseclick.png')
BACKGROUND=image.load('image/background.png')
TIME=image.load('image/time.png')
RANK=image.load('image/rank.png')
LEVEL=image.load('image/level.png')
HOME=image.load('image/lol/about.png')
MUSIC=mixer.Sound('sound/sound_track.ogg')
STARTBUTTON=BUTTON.get_image(60,60,60,60)
STOPBUTTON=BUTTON.get_image(0,60,60,60)
RANDOMBUTTON=BUTTON.get_image(0,0,60,60)
RANDOMCLICKBUTTON=BUTTON.get_image(120,0,60,60)
HOMEBUTTON=BUTTON.get_image(180,0,60,60)
HOMECLICKBUTTON=BUTTON.get_image(60,0,60,60)
MUSICBUTTON=BUTTON.get_image(120,60,60,60)
MUSICOFFBUTTON=BUTTON.get_image(180,60,60,60)
GAMEBUTTON=BUTTON.get_image(0,120,60,60)
GAMECLICKBUTTON=BUTTON.get_image(60,120,60,60)
OPTIONBUTTON=BUTTON.get_image(120,120,60,60)
OPTIONCLICKBUTTON=BUTTON.get_image(180,120,60,60)
RECORDBUTTON=BUTTON.get_image(0,180,60,60)
RECORDCLICKBUTTON=BUTTON.get_image(60,180,60,60)
QUITBUTTON=BUTTON.get_image(120,180,60,60)
QUITCLICKBUTTON=BUTTON.get_image(180,180,60,60)
MOVERIGHTCLICK=MOVE.get_image(0,0,60,60)
MOVERIGHT=MOVE.get_image(60,0,60,60)
MOVELEFTCLICK=MOVE.get_image(0,60,60,60)
MOVELEFT=MOVE.get_image(60,60,60,60)
CHECKOK=CHECK.get_image(60,0,60,60)
CHECKOKCLICK=CHECK.get_image(0,0,60,60)
VEC=math.Vector2
FONT=font.Font('font/VnArabia.TTF',20)

