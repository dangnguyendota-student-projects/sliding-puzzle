from pygame import time,display,K_RETURN,K_LEFT,K_RIGHT,K_UP,K_DOWN,K_SPACE,K_a,K_s,K_d,K_w,QUIT,event,K_ESCAPE,KEYDOWN,MOUSEBUTTONDOWN

from random import randint
from sprite import *

#ten ham va class viet hoa dau chu
class Game():
    def __init__(self):
        init()
        mixer.init()
        mouse.set_visible(False)
        self.level=3#chon level
        self.sound=True#bat/tat am thanh
        self.option=False
        self.chooselvl=False
        self.record=False
        self.clock=time.Clock()
        self.score=0#luu diem

    def New(self):#new game
        self.screen=display.set_mode((WIDTH,HEIGHT))
        display.set_icon(ICON)
        display.set_caption(TITLE)
        self.running = True#vong lap
        self.win=False#thang hay chua?
        self.start=False#bat dau choi hay chua?
        self.stop=False
        self.about=False
        self.skin=0
        self.board=self.RandomBoard()
        self.NewSprites()

    def Run(self):#game loop
        MUSIC.play(-1)
        MUSIC.set_volume(10)
        while(self.running):
            self.Event()
            self.Update()
            self.Draw()

    def Event(self):#xu ly su kien

        for e in event.get():#e la bien nhan biet su kien
            if e.type==QUIT:
                quit()
                exit()
            if e.type==KEYDOWN:
                if e.key==K_ESCAPE:
                    quit()
                    exit()
                if not self.option and not self.record and not self.chooselvl and not self.about:
                    if (e.key==K_LEFT or e.key==K_a) and  self.start and not self.stop:
                        self.board = self.Move(self.board,'left')
                    elif (e.key==K_RIGHT or e.key==K_d) and  self.start and not self.stop:
                        self.board=self.Move(self.board,'right')
                    elif (e.key==K_DOWN or e.key==K_s) and   self.start and not self.stop:
                        self.board=self.Move(self.board,'down')
                    elif (e.key==K_UP or e.key==K_w) and  self.start and not self.stop:
                        self.board=self.Move(self.board,'up')
                    elif (e.key==K_SPACE or e.key==K_RETURN) and not self.stop :
                        self.startbutton.click()
                elif self.option==True:
                    if e.key==K_RETURN:
                        self.option=False
                    if (e.key==K_LEFT or e.key==K_a) and self.skin>=1:
                        self.skin-=1
                    if (e.key==K_RIGHT or e.key==K_d) and self.skin<=2:
                        self.skin+=1
                elif self.chooselvl==True:
                    if e.key==K_RETURN:
                        self.chooselvl=False
                    if (e.key==K_LEFT or e.key==K_a) and self.level>=4:
                        self.level-=1
                        self.skin=0
                        self.board=self.RandomBoard()
                    if (e.key==K_RIGHT or e.key==K_d) and self.level<=6:
                        self.skin=0
                        self.level+=1
                        self.board=self.RandomBoard()
                elif self.about:
                    if e.key==K_RETURN:
                        self.about=False


            if e.type==MOUSEBUTTONDOWN:
                m=VEC(mouse.get_pos())
                if not self.option and not self.record  and not self.chooselvl :
                    if e.button==1:
                        if -30<=m.x-self.homebutton.rect.center[0]<=30 and -30<= m.y-self.homebutton.rect.center[1]<=30:
                            self.homebutton.click()
                        if  not self.about:
                            if -30<=m.x-self.startbutton.rect.center[0]<=30 and -30<= m.y-self.startbutton.rect.center[1]<=30:
                                self.startbutton.click()
                            if -30<=m.x-self.randombutton.rect.center[0]<=30 and -30<= m.y-self.randombutton.rect.center[1]<=30:
                                self.randombutton.click()
                            if -30<=m.x-self.musicbutton.rect.center[0]<=30 and -30<= m.y-self.musicbutton.rect.center[1]<=30:
                                self.musicbutton.click()
                            if -30<=m.x-self.optionbutton.rect.center[0]<=30 and -30<= m.y-self.optionbutton.rect.center[1]<=30:
                                self.optionbutton.click()
                            if -30<=m.x-self.gamebutton.rect.center[0]<=30 and -30<= m.y-self.gamebutton.rect.center[1]<=30:
                                self.gamebutton.click()
                            if -30<=m.x-self.quitbutton.rect.center[0]<=30 and -30<= m.y-self.quitbutton.rect.center[1]<=30:
                                self.quitbutton.click()
                            if -30<=m.x-self.recordbutton.rect.center[0]<=30 and -30<= m.y-self.recordbutton.rect.center[1]<=30:
                                self.recordbutton.click()
                elif self.record :
                    if e.button==1:
                        if 262<=m.x<=348 and 300<=m.y<=335:
                            self.record=False
                elif self.option:
                    if e.button==1:
                        if 140 <= m.x <= 200 and 220 <= m.y < 280 and self.skin>=1:
                            self.skin-=1
                        if 510 <= m.x <= 570 and 220 <= m.y <= 280 and self.skin<=2:
                            self.skin+=1
                        if 330 <= m.x <= 390 and 420 <= m.y < 480:
                            self.option=False
                elif self.chooselvl:
                    if e.button==1:
                        if 140 <= m.x <= 200 and 220 <= m.y < 280 and self.level>=4:
                            self.level-=1
                            self.skin=0
                            self.board=self.RandomBoard()
                            self.score=0
                        if 510 <= m.x <= 570 and 220 <= m.y <= 280 and self.level<=6:
                            self.level+=1
                            self.skin=0
                            self.score=0
                            self.board = self.RandomBoard()
                        if 330 <= m.x <= 390 and 420 <= m.y < 480:
                            self.chooselvl=False

    def Update(self):#update lai man hinh
        if not self.sound:
            MUSIC.set_volume(0)
        else:
            MUSIC.set_volume(10)
        self.sprites.update()
        self.mouses.update()
        # neu dang choi va chua dung game, diem tang len
        if self.start and not self.stop:
            self.score+=1
        #neu win dung game, luu diem
        if self.Win(self.board) and self.start:
            self.stop=True
            f=open('record/score'+str(self.level)+'.txt','r')
            temp = ''
            for i in f:
                if i != '\n':
                    temp += i
            Record = float(temp)
            if Record>int(self.score/0.6)/100:
                f = open('record/score' + str(self.level) + '.txt', 'w')
                f.writelines(str(int(self.score/0.6)/100))

    def Draw(self):#ve cac doi tuong ra man hinh
        m=VEC(mouse.get_pos())
        self.screen.blit(BACKGROUND,(0,0))
        self.screen.blit(IMG[self.skin][self.level-3],(500,60))
        self.DrawBoard()
        self.DrawScore()
        self.sprites.draw(self.screen)
        #neu trong khung diem cao
        if self.record:
            if 262 <= m.x <= 348 and 300 <= m.y <= 335:
                self.screen.blit(RECORDCLICK, (250, 200))
            else:
                self.screen.blit(RECORD,(250,200))
            f = open('record/score' + str(self.level) + '.txt', 'r')
            temp = ''
            for i in f:
                if i != '\n':
                    temp += i
            text=FONT.render(temp+"s",True,Color('black'),None)
            self.screen.blit(text,(300,250))
        # neu trong khung tuy chon
        if self.option:
            self.screen.blit(IMG1[self.skin][self.level - 3], (200, 100))
            self.screen.blit(KHUNG,(190,90))
            if 140<=m.x<=200 and 220<=m.y<280:
                self.screen.blit(MOVELEFTCLICK, (140, 220))
            else:
                self.screen.blit(MOVELEFT,(140,220))
            if 510<=m.x<=570 and 220<=m.y<=280:
                self.screen.blit(MOVERIGHTCLICK, (510, 220))
            else:
                self.screen.blit(MOVERIGHT, (510, 220))
            if 330<=m.x<=390 and 420<=m.y<480:
                self.screen.blit(CHECKOKCLICK,(330,420))
            else:
                self.screen.blit(CHECKOK, (330,420))
        #neu trong khung chon level
        if self.chooselvl:
            self.screen.blit(LEVEL,(300,200))
            text=FONT.render(str(self.level),True,Color('black'),None)
            self.screen.blit(text,(380,220))
            if 140<=m.x<=200 and 220<=m.y<280:
                self.screen.blit(MOVELEFTCLICK, (140, 220))
            else:
                self.screen.blit(MOVELEFT,(140,220))
            if 510<=m.x<=570 and 220<=m.y<=280:
                self.screen.blit(MOVERIGHTCLICK, (510, 220))
            else:
                self.screen.blit(MOVERIGHT, (510, 220))
            if 330<=m.x<=390 and 420<=m.y<480:
                self.screen.blit(CHECKOKCLICK,(330,420))
            else:
                self.screen.blit(CHECKOK, (330,420))
        if self.about:
            self.screen.blit(HOME,(100,200))
        self.mouses.draw(self.screen)

        display.update()
        self.clock.tick(FPS)

    def NewSprites(self):#tao moi cac sprite
        self.sprites=sprite.Group()
        self.mouses=sprite.Group()
        self.startbutton=StartButton(self)
        self.randombutton=RandomButton(self)
        self.homebutton=HomeButton(self)
        self.musicbutton=MusicButton(self)
        self.optionbutton=OptionButton(self)
        self.recordbutton=RecordButton(self)
        self.gamebutton=GameButton(self)
        self.quitbutton=QuitButton(self)
        self.mouse=Mouse(self)
        self.mouses.add(self.mouse)
        self.sprites.add(self.startbutton)
        self.sprites.add(self.randombutton)
        self.sprites.add(self.homebutton)
        self.sprites.add(self.musicbutton)
        self.sprites.add(self.optionbutton)
        self.sprites.add(self.recordbutton)
        self.sprites.add(self.gamebutton)
        self.sprites.add(self.quitbutton)

    def NewBoard(self):#tao moi 1 bang
        board=[]
        for i in range(self.level):
            board.append([])
            for j in range(self.level):
                board[i].append(i*self.level+j)
        board[self.level-1][self.level-1]=-1
        return board

    def RandomBoard(self):#tao mang ngau nhien
        board = []
        for i in range(self.level):
            board.append([])
            for j in range(self.level):
                board[i].append(i * self.level + j)
        board[self.level - 1][self.level - 1] = -1
        move=500#di 50 nuoc
        while(move>0):
            r=randint(0, 3)
            board=self.Move(board,EVENT[r])
            move-=1
        return board

    def Move(self,board,e):#move
        x=-1
        y=-1
        for i in range(self.level):
            for j in range(self.level):
                if board[i][j]==-1:
                    x=i
                    y=j
                    break
            if x!=-1 and y!=-1:
                break
        if e=='left' and y<self.level-1:
            board[x][y]=board[x][y+1]
            board[x][y+1]=-1
        elif e=='right' and y>=1:
            board[x][y]=board[x][y-1]
            board[x][y-1]=-1
        elif e=='up' and x<self.level-1:
            board[x][y]=board[x+1][y]
            board[x+1][y]=-1
        elif e=='down' and x>=1:
            board[x][y]=board[x-1][y]
            board[x-1][y]=-1
        return board

    def Win(self,board):
        for i in range(self.level):
            for j in range(self.level):
                if i!=self.level-1 or j!=self.level-1:
                    if board[i][j]!=i*self.level+j:
                        return False
        if board[self.level-1][self.level-1]!= -1:
            return False
        return True

    def DrawBoard(self):
        for i in range(self.level):
            for j in range(self.level):
                if self.board[i][j]!=-1:
                    self.screen.blit(LEVEL_IMG[self.skin][self.level-3][self.board[i][j]],(POS_GAME[0]+j*HEIGH_GAME//self.level,POS_GAME[1]+i*WIDTH_GAME//self.level))

    def DrawScore(self):
        text=FONT.render(str(int(self.score/0.6)/100),True,Color('red'),None)
        self.screen.blit(TIME,(550,300))
        self.screen.blit(text,(610,320))
        self.screen.blit(RANK,(550,380))
        if 0< (int(self.score/0.6)/100)<=2*self.level:
            self.screen.blit(RANK_IMG[6],(565,455))
        elif 2*self.level<(int(self.score/0.6)/100)<=4*self.level:
            self.screen.blit(RANK_IMG[5], (565, 455))
        elif 4*self.level<(int(self.score/0.6)/100)<=7*self.level:
            self.screen.blit(RANK_IMG[4], (565, 455))
        elif 7*self.level<(int(self.score/0.6)/100)<=11*self.level:
            self.screen.blit(RANK_IMG[3], (565, 455))
        elif 11*self.level<(int(self.score/0.6)/100)<=15*self.level:
            self.screen.blit(RANK_IMG[2], (565, 455))
        elif 15*self.level<(int(self.score/0.6)/100)<=21*self.level:
            self.screen.blit(RANK_IMG[1], (565, 455))
        elif self.level<(int(self.score/0.6)/100)>21*self.level:
            self.screen.blit(RANK_IMG[0], (565, 455))


#test
g=Game()
g.New()
g.Run()