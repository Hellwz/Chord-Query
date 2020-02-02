import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from functools import partial

import Qchord
white_key = [1,3,5,6,8,10,12,13,15,17,18,20,22,24]
black_key = [2,4,7,9,11,14,16,19,21,23]

def setColor(ui,num):
    if num > 24: num -= 24
    if num in black_key: color = white
    else: color = black
    if num == 1: ui.key_1.setPixmap(color)
    elif num == 2: ui.key_2.setPixmap(color)
    elif num == 3: ui.key_3.setPixmap(color)
    elif num == 4: ui.key_4.setPixmap(color)
    elif num == 5: ui.key_5.setPixmap(color)
    elif num == 6: ui.key_6.setPixmap(color)
    elif num == 7: ui.key_7.setPixmap(color)
    elif num == 8: ui.key_8.setPixmap(color)
    elif num == 9: ui.key_9.setPixmap(color)
    elif num == 10: ui.key_10.setPixmap(color)
    elif num == 11: ui.key_11.setPixmap(color)
    elif num == 12: ui.key_12.setPixmap(color)
    elif num == 13: ui.key_13.setPixmap(color)
    elif num == 14: ui.key_14.setPixmap(color)
    elif num == 15: ui.key_15.setPixmap(color)
    elif num == 16: ui.key_16.setPixmap(color)
    elif num == 17: ui.key_17.setPixmap(color)
    elif num == 18: ui.key_18.setPixmap(color)
    elif num == 19: ui.key_19.setPixmap(color)
    elif num == 20: ui.key_20.setPixmap(color)
    elif num == 21: ui.key_21.setPixmap(color)
    elif num == 22: ui.key_22.setPixmap(color)
    elif num == 23: ui.key_23.setPixmap(color)
    elif num == 24: ui.key_24.setPixmap(color)
def init():
    ui.key_1.setPixmap(trans)
    ui.key_2.setPixmap(trans)
    ui.key_3.setPixmap(trans)
    ui.key_4.setPixmap(trans)
    ui.key_5.setPixmap(trans)
    ui.key_6.setPixmap(trans)
    ui.key_7.setPixmap(trans)
    ui.key_8.setPixmap(trans)
    ui.key_9.setPixmap(trans)
    ui.key_10.setPixmap(trans)
    ui.key_11.setPixmap(trans)
    ui.key_12.setPixmap(trans)
    ui.key_13.setPixmap(trans)
    ui.key_14.setPixmap(trans)
    ui.key_15.setPixmap(trans)
    ui.key_16.setPixmap(trans)
    ui.key_17.setPixmap(trans)
    ui.key_18.setPixmap(trans)
    ui.key_19.setPixmap(trans)
    ui.key_20.setPixmap(trans)
    ui.key_21.setPixmap(trans)
    ui.key_22.setPixmap(trans)
    ui.key_23.setPixmap(trans)
    ui.key_24.setPixmap(trans)

def get_start(input):
    if input[0] == 'C':
        start = 1
        input = input[1:]
    elif input[0:2] == '#C' or input[0:2] == 'bD':
        start = 2
        input = input[2:]
    elif input[0] == 'D':
        start = 3
        input = input[1:]
    elif input[0:2] == '#D' or input[0:2] == 'bE':
        start = 4
        input = input[2:]
    elif input[0] == 'E':
        start = 5
        input = input[1:]
    elif input[0] == 'F':
        start = 6
        input = input[1:]
    elif input[0:2] == '#F' or input[0:2] == 'bG':
        start = 7
        input = input[2:]
    elif input[0] == 'G':
        start = 8
        input = input[1:]
    elif input[0:2] == '#G' or input[0:2] == 'bA':
        start = 9
        input = input[2:]
    elif input[0] == 'A':
        start = 10
        input = input[1:]
    elif input[0:2] == '#A' or input[0:2] == 'bB':
        start = 11
        input = input[2:]
    elif input[0] == 'B':
        start = 12
        input = input[1:]
    return start , input

def showchord(ui):
    init()
    chord = [-1,-1,-1,-1,-1,-1,-1]
    start = 0
    new_start = 0
    input = ui.lineEdit.text()
    
    start,input = get_start(input)
    if start == 0: return
    new_start = start
    
    tmp = ''
    if input.find('sus') != -1 :
        loc = input.find('sus')
        tmp = input[loc:]
        input = input[:loc]
    if input.find('add') != -1 :
        loc = input.find('add')
        tmp = input[loc:]
        input = input[:loc]
    if input.find('/') != -1 :
        loc = input.find('/')
        tmp = input[loc:]
        input = input[:loc]

    if input == '': #大三和弦
        chord[0:3] = [0,4,7]
    elif input == 'm': #小三和弦
        chord[0:3] = [0,3,7]
    elif input == 'aug': #增三和弦
        chord[0:3] = [0,4,8]
    elif input == 'dim': #减三和弦
        chord[0:3] = [0,3,6]
    elif input == '7' or input == 'dom7': #属七和弦
        chord[0:4] = [0,4,7,10]
    elif input == 'm7': #小七和弦
        chord[0:4] = [0,3,7,10]
    elif input == 'maj7' or input == 'M7': #大七和弦
        chord[0:4] = [0,4,7,11]  
    elif input == 'aug7': #增七和弦
        chord[0:4] = [0,4,8,10]
    elif input == 'dim7': #减七和弦
        chord[0:4] = [0,3,6,9]
    elif input == '7b5' or input == '7-5': #七减五和弦
        chord[0:4] = [0,4,6,10]  
    elif input == 'm7b5' or input == 'm7-5': #小七减五和弦（半减七和弦）
        chord[0:4] = [0,3,6,10]  
    elif input == 'mM7': #小大七和弦
        chord[0:4] = [0,3,7,11]
    elif input == 'augM7': #增大七和弦
        chord[0:4] = [0,4,8,11]   
    elif input == '6' or input == 'maj6': #六和弦
        chord[0:4] = [0,4,7,9]     
    elif input == 'm6': #小六和弦
        chord[0:4] = [0,3,7,9] 
    elif input == '9': #（属）九和弦
        chord[0:4] = [0,4,7,10,14]     
    elif input == 'm9': #小九和弦
        chord[0:4] = [0,3,7,10,14] 
    elif input == 'maj9': #大九和弦
        chord[0:4] = [0,4,7,11,14] 
    elif input == '11': #（属）十一和弦
        chord[0:4] = [0,4,7,10,14,17]   
    elif input == 'm11': #小十一和弦
        chord[0:4] = [0,3,7,10,14,17]  
    elif input == 'maj11': #大十一和弦
        chord[0:4] = [0,4,7,11,14,17] 
    elif input == '13': #（属）十三和弦
        chord[0:4] = [0,4,7,10,14,17,21]   
    elif input == 'm13': #小十三和弦
        chord[0:4] = [0,3,7,10,14,17,21]  
    elif input == 'maj13': #大十三和弦
        chord[0:4] = [0,4,7,11,14,17,21] 

    if tmp[0:3] == 'add':
        if tmp[3] == '2':chord.append(2)
        elif tmp[3] == '4':chord.append(5)
        elif tmp[3] == '6':chord.append(9)
        elif tmp[3] == '8':chord.append(12) #?
        elif tmp[3] == '9':chord.append(14)
        elif tmp[3:5] == '11':chord.append(17)
        elif tmp[3:5] == '13':chord.append(21)
    if tmp == 'sus': tmp = 'sus4'
    if tmp[0:3] == 'sus':
        if tmp[3] == '2': chord[1] = 2
        elif tmp[3] == '4': chord[1] = 5
    if tmp[0:1] == '/':
        new_start,tmp = get_start(tmp[1:]) 

    for i in chord:
        if i == 0 and new_start != start: #处理根音变化
            setColor(ui,new_start)
            continue
        if i != -1 : setColor(ui,start+i)  

if __name__ == '__main__':
    app = QApplication(sys.argv)
    black = QPixmap(':/Prefix1/black.png')
    white = QPixmap(':/Prefix1/white.png')
    trans = QPixmap(':/Prefix1/transparent.png')
    MainWindow = QMainWindow()
    ui = Qchord.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.pushButton.clicked.connect(partial(showchord, ui))
    sys.exit(app.exec_())
