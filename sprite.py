from pygame import sprite,mouse
from setting import *

class StartButton(sprite.Sprite):
    def __init__(self,parent):
        self.parent=parent
        sprite.Sprite.__init__(self)
        self.image=STARTBUTTON
        self.rect=self.image.get_rect()
        self.rect.x=0
        self.rect.y=0
        self.start=True
    def update(self):

        if not self.parent.stop:
            if self.start:
                self.image=STARTBUTTON
            else:
                self.image=STOPBUTTON
        else:
            self.image=STARTBUTTON
    def click(self):
        if not self.parent.option and not self.parent.record:
            if self.start and not self.parent.stop:
                self.start=False
            elif not self.start and not self.parent.stop:
                self.start=True
            if not self.parent.stop:
                if self.parent.start :
                    self.parent.start=False
                else:
                    self.parent.start=True
class RandomButton(sprite.Sprite):
    def __init__(self,parent):
        self.parent=parent
        sprite.Sprite.__init__(self)
        self.image=RANDOMBUTTON
        self.rect=self.image.get_rect()
        self.rect.x=70
        self.rect.y=0
    def update(self):
        m=VEC(mouse.get_pos())
        if -30<=m.x-self.rect.center[0]<=30 and -30<=m.y-self.rect.center[1]<=30 and not self.parent.chooselvl and not self.parent.option and not self.parent.record:
            self.image=RANDOMCLICKBUTTON
        else:
            self.image=RANDOMBUTTON
    def click(self):
        if not self.parent.start and not self.parent.stop:
            self.parent.board=self.parent.RandomBoard()
        if self.parent.stop:
            self.parent.stop=False
            self.parent.board=self.parent.RandomBoard()
            self.parent.score=0
            self.parent.startbutton.start=True
            self.parent.start=False

class HomeButton(sprite.Sprite):
    def __init__(self,parent):
        self.parent=parent
        sprite.Sprite.__init__(self)
        self.image=HOMEBUTTON
        self.rect=self.image.get_rect()
        self.rect.x=140
        self.rect.y=0
    def update(self):
        m = VEC(mouse.get_pos())
        if -30 <= m.x - self.rect.center[0] <= 30 and -30 <= m.y - self.rect.center[1] <= 30 and not self.parent.chooselvl and not self.parent.option and not self.parent.record:
            self.image = HOMECLICKBUTTON
        else:
            self.image = HOMEBUTTON
    def click(self):
        if self.parent.about:
            self.parent.about=False
        else:
            self.parent.about=True
class MusicButton(sprite.Sprite):
    def __init__(self,parent):
        self.parent=parent
        sprite.Sprite.__init__(self)
        self.image=MUSICBUTTON
        self.rect=self.image.get_rect()
        self.rect.x=210
        self.rect.y=0
        self.mute=False
    def update(self):
        if self.mute:
            self.image=MUSICOFFBUTTON
        else:
            self.image=MUSICBUTTON
    def click(self):
        if self.mute:
            self.mute=False
        else:
            self.mute=True
        if self.parent.sound:
            self.parent.sound=False
        else:
            self.parent.sound=True

class OptionButton(sprite.Sprite):
    def __init__(self,parent):
        self.parent=parent
        sprite.Sprite.__init__(self)
        self.image=OPTIONBUTTON
        self.rect=self.image.get_rect()
        self.rect.x=280
        self.rect.y=0
    def update(self):
        m = VEC(mouse.get_pos())
        if -30 <= m.x - self.rect.center[0] <= 30 and -30 <= m.y - self.rect.center[1] <= 30 and not self.parent.chooselvl and not self.parent.option and not self.parent.record:
            self.image = OPTIONCLICKBUTTON
        else:
            self.image = OPTIONBUTTON
    def click(self):
        self.parent.option=True
class RecordButton(sprite.Sprite):
    def __init__(self,parent):
        self.parent=parent
        sprite.Sprite.__init__(self)
        self.image=RECORDBUTTON
        self.rect=self.image.get_rect()
        self.rect.x=350
        self.rect.y=0
    def update(self):
        m = VEC(mouse.get_pos())
        if -30 <= m.x - self.rect.center[0] <= 30 and -30 <= m.y - self.rect.center[1] <= 30 and not self.parent.chooselvl and not self.parent.option and not self.parent.record:
            self.image = RECORDCLICKBUTTON
        else:
            self.image = RECORDBUTTON
    def click(self):
        self.parent.record=True
class GameButton(sprite.Sprite):
    def __init__(self,parent):
        self.parent=parent
        sprite.Sprite.__init__(self)
        self.image=GAMEBUTTON
        self.rect=self.image.get_rect()
        self.rect.x=520
        self.rect.y=0
    def update(self):
        m = VEC(mouse.get_pos())
        if -30 <= m.x - self.rect.center[0] <= 30 and -30 <= m.y - self.rect.center[1] <= 30 and not self.parent.chooselvl and not self.parent.option and not self.parent.record:
            self.image = GAMECLICKBUTTON
        else:
            self.image = GAMEBUTTON
    def click(self):
        self.parent.chooselvl=True
class QuitButton(sprite.Sprite):
    def __init__(self,parent):
        sprite.Sprite.__init__(self)
        self.parent=parent
        self.image=QUITBUTTON
        self.rect=self.image.get_rect()
        self.rect.x=595
        self.rect.y=0
    def update(self):
        m = VEC(mouse.get_pos())
        if -30 <= m.x - self.rect.center[0] <= 30 and -30 <= m.y - self.rect.center[1] <= 30 and not self.parent.option and not self.parent.record  and not self.parent.chooselvl:
            self.image = QUITCLICKBUTTON
        else:
            self.image = QUITBUTTON
    def click(self):
        quit()
        exit()

class Mouse(sprite.Sprite):
    def __init__(self,parent):
        sprite.Sprite.__init__(self)
        self.parent=parent
        self.image=MOUSE
        self.rect=self.image.get_rect()
        self.rect.x=0
        self.rect.y=0
    def update(self):
        self.rect.center=mouse.get_pos()
        hit=sprite.spritecollide(self,self.parent.sprites,False,None)
        if hit:
            self.image=MOUSECLICK
        else:
            self.image=MOUSE