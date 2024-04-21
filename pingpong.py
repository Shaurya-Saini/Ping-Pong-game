import os
import time
import keyboard

modes=['E','C','A']
mode='lol'
while mode not in modes:
    mode=input("PLAYER 1 plays with 'w' and 's' keys\nPLAYER 2 plays with 'up' and 'down' keys\nTHE GAME WILL BE OF 5 POINTS\nEnter the difficulty level of the game\n'E' for easy\t'C' for challenging\t'A' for increasing difficulty\nENTER = ")
    mode=mode.upper()

def setting(diff,sec):
    if diff=='E':
        sec=0.175
    elif diff=='C':
        sec=0.05
    elif diff=='A':
        if sec>=0.05:
            sec-=0.00075
    return sec

def print_board(player10,player11,player20,player21,ball):
    os.system('cls')
    up_border=''
    for i in range(0,40):
        up_border+='-'
    print(up_border)
    #seats=15 and row=38+2(|)
    for row in range(0,15):
        line=''
        for seat in range(0,40):
            if seat==0 or seat==39:
                line+='|'
            elif player10==[row,seat] or player11==[row,seat] or player20==[row,seat] or player21==[row,seat]:
                line+='|'
            elif ball==[row,seat]:
                line+='o'
            else:
                line+=' '
        print(line)
    print(up_border)

def keyboard_input(pl10,pl11,pl20,pl21):
    if keyboard.is_pressed('w'):
        if pl11[0]!=0:
            pl11[0]-=1
            pl10[0]-=1
    elif keyboard.is_pressed('s'):
        if pl10[0]!=14:
            pl10[0]+=1
            pl11[0]+=1
    if keyboard.is_pressed('up'):
        if pl21[0]!=0:
            pl21[0]-=1
            pl20[0]-=1
    elif keyboard.is_pressed('down'):
        if pl20[0]!=14:
            pl20[0]+=1
            pl21[0]+=1
    return pl10,pl11,pl20,pl21

score1=0
score2=0
while True:
    player10=[7,1]
    player11=[6,1]
    player20=[7,38]
    player21=[6,38]
    ball=[7,20]
    motion=[1,1]
    sec=0.175
    sec=setting(mode,sec)
    print_board(player10,player11,player20,player21,ball)
    while True:
        player10,player11,player20,player21=keyboard_input(player10,player11,player20,player21)
        print_board(player10,player11,player20,player21,ball)
        if ball[0]==14:
            motion[0]=-1
        elif ball[0]==0:
            motion[0]=+1
        if ball[1]==2 and ball[0]==player10[0]:
            motion[1]=1
        elif ball[1]==2 and ball[0]==player11[0]:
            motion[1]=1
        elif ball[1]==2 and ball[0]!=player10[0] and ball[0]!=player11[0]:
            score2+=1
            break
        if ball[1]==37 and ball[0]==player20[0]:
            motion[1]=-1
        elif ball[1]==37 and ball[0]==player21[0]:
            motion[1]=-1
        elif ball[1]==37 and ball[0]!=player20[0] and ball[0]!=player21[0]:
            score1+=1
            break
        ball[0]+=motion[0]
        ball[1]+=motion[1]
        time.sleep(sec)
        sec=setting(mode,sec)
    os.system('cls')
    print('player 1 = ',score1)
    print('player 2 = ',score2)
    time.sleep(2)
    if score1==5:
        print('Player 1 won')
        break
    elif score2==5:
        print('Player 2 won')
        break
time.sleep(100)