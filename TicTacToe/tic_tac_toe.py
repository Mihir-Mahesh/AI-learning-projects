import os
command = "pip install pygame"
os.system(command)
import pygame as p
p.init()
from random import randrange
import minimax


EASY_MODE = False


blank_image = p.image.load('TicTacToe/Blank.png')
x_image = p.image.load('TicTacToe/X.png')
o_image = p.image.load('TicTacToe/O.png')
background_image = p.transform.scale(p.image.load('TicTacToe/Background.png'), (500, 500))
p.display.set_caption('Tic Tac Toe AI Project (learning Pygame)')
window = p.display.set_mode((500, 500))

turn = 0
not_over = True

box_group = p.sprite.Group()
boxes = []
state = []
board = [-1 for i in range(9)]


class Box(p.sprite.Sprite):
    def __init__(self, x_id, y_id, num):
        super().__init__()
        self.width = 120
        self.height = 120
        self.x = x_id * self.width
        self.y = y_id * self.height
        self.item = ''
        self.num = num
        self.play = -1
        self.image = p.transform.scale(blank_image, (self.width, self.height))
        self.rect = self.image.get_rect()
    
    def update(self):
        self.rect.center = (self.x, self.y)

    def clicked(self, x, y):
        global turn
        
        if (self.item == '' and self.rect.collidepoint(x, y)):
            self.item = turn
            self.play = turn % 2
            board[self.num - 1] = turn % 2
            if turn % 2 == 0:
                self.image = x_image
                self.image = p.transform.scale(self.image, (self.width, self.height))
                turn += 1
                if (check_win()):
                    change_screen(1)
                    return True
                if (turn > 8):
                    change_screen(0)
                    return True
                if (not EASY_MODE):
                    comp_click_hard()
                else:
                    comp_click()
                
            else:
                self.image = o_image
                self.image = p.transform.scale(self.image, (self.width, self.height))
                turn += 1
                if (check_win()):
                    change_screen(2)
                    return True
                if (turn > 8):
                    change_screen(0)
                    return True
            

            
            
            return True
        return False



def Update():
    window.blit(background_image, (0, 0))
    box_group.draw(window)
    box_group.update()
    p.display.update()


def comp_click():
    global boxes
    works = False
    while(not works):
        ind = randrange(0, 9)
        works = boxes[ind].clicked(boxes[ind].x, boxes[ind].y)
          
def comp_click_hard():
    global boxes, board, turn
    ind = minimax.minimax(board, turn)
    boxes[ind].clicked(boxes[ind].x, boxes[ind].y)    



def change_screen(state):
    global background_image, boxes, box_group
    Update()
    p.time.wait(1000)
    boxes.clear()
    box_group.empty()
    if (state == 0):
        background_image = p.transform.scale(p.image.load('TicTacToe/Tie Game.png'), (500, 500))
    elif (state==1):
        background_image = p.transform.scale(p.image.load('TicTacToe/X Wins.png'), (500, 500))
    else:
        background_image = p.transform.scale(p.image.load('TicTacToe/O Wins.png'), (500, 500))
        



def check_col_same():
    for i in range(3):
        if boxes[i].play != -1 and boxes[i].play == boxes[i + 3].play == boxes[i + 6].play:
            return True
    return False

def check_row_same():
    for i in range(0, 9, 3):
        if boxes[i].play != -1 and boxes[i].play == boxes[i+1].play == boxes[i+2].play:
            return True
    return False

def check_diag_same():
    if boxes[0].play != -1 and boxes[0].play == boxes[4].play == boxes[8].play:
        return True
    if boxes[2].play != -1 and boxes[2].play == boxes[4].play == boxes[6].play:
        return True
    return False

def check_win():
    return check_diag_same() or check_row_same() or check_col_same()


num = 1
for y in range(1, 4):
    for x in range(1, 4):
        box = Box(x, y, num)
        box_group.add(box)
        boxes.append(box)
        num += 1



run = True
clock = p.time.Clock()
while(run):
    clock.tick(60)
   
    for event in p.event.get():
        if (event.type == p.QUIT):
            run = False
        
        if (not_over and event.type == p.MOUSEBUTTONDOWN and turn % 2 == 0):
            x, y = p.mouse.get_pos()
            
            for b in boxes:
                b.clicked(x, y)
            
    Update()


