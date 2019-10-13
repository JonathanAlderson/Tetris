# This version has some bug fixes about gaps

import tkinter , random , time, sys , operator
from tkinter import *
playerScore = 0
main_window = tkinter.Tk()
main_window.title("Tetris")
textFile = open("hiScore.txt","r")
hiScore = textFile.read()
leftPane = Frame(main_window,width=750,height=550,bg="grey")
instructions = Label(leftPane,text=("                     Tetris                     \n\n  A ~ Move Left\nD ~ Move Right\nW~Rotate\nS ~ Soft Drop\nShift ~ Hard Drop\n # ~ Restart Game\nP ~ Pause Game\nO ~ Unpause\n\n"),font=("Agency FB Bold",30),bg="grey")
showInstructions = False
goodGraphics = False
forget = False
def startGame():
    global showInstructions , forget
    showInstructions = False
    forget = True
def startGame2():
    global showInstructions , goodGraphics , forget
    showInstructions = False
    goodGraphics = True
    forget = True
button = Button(leftPane, text="Old Grapics", command=startGame)
button2 = Button(leftPane, text="New Graphics", command=startGame2)
while showInstructions == True:
    leftPane.pack()
    instructions.pack()
    button.pack(side=RIGHT)
    button2.pack(side=LEFT)
    main_window.update()
if forget == True:
    button.pack_forget()
    button2.pack_forget()
    leftPane.pack_forget()
c = tkinter.Canvas(main_window, width=350, height=550, bg="white") 
c.pack(side=LEFT)
instructions.pack_forget()
scoreChangeList = [[400,25],[800,20],[1200,15],[1600,12],[2000,10],[3000,9],[4000,8],[5000,7],[6000,6],[7000,5],[10000,3]]
leftPane = Frame(main_window,width=400,height=550,bg="grey")
leftPane.pack(side=RIGHT)
title = Label(leftPane,text=("\nTetris\n"),font=("Agency FB Bold",52),bg="grey")
title.pack(side=TOP)
speedLabel = Label(leftPane,text="Speed: " + str(12 - (len(scoreChangeList))),font=("Agency FB Bold",20),bg="Grey")
shapeIcons = ["####\n","###\n    #","    ###\n#","##\n##","   ##\n## ","###\n # ","##\n    ## "] 
shapesList = [  [[[3,1],[4,1],[5,1],[6,1]],[1]]  ,[[[5,2],[3,1],[4,1],[5,1]],[2]],[[[3,2],[3,1],[4,1],[5,1]],[3]]  ,  [[[4,2],[3,2],[3,1],[4,1],],[4]] , [[[5,2],[4,2],[5,1],[6,1]],[5]] , [[[4,2],[3,1],[4,1],[5,1]],[6]] ,  [[[5,2],[6,2],[4,1],[5,1]],[7]]]
nextShapeToSpawn = random.choice(shapesList)
score = Label(leftPane,text="Score: " + str(playerScore) + ("\n\nNext Shape\n\n") + (shapeIcons[(nextShapeToSpawn[1][0])-1]),font=("Agency FB Bold",20),bg="Grey")
score2 = Label(leftPane,text="Hi-Score: " + str(hiScore) + ("\n"),font=("Agency FB Bold",20),bg="Grey")
score2.pack(side=TOP)
speedLabel.pack(side=TOP)
score.pack(side=TOP)  
frame = 0
grid = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[1,0,1,1,1,1,1,1,1,1]]# creates a 10*20 2D array
shapes = []    
refreshTime = 30
hardDrop = False       
spawnNewItem = True
pause = False
coloursList = [[0,"black"],[1,"cyan"],[2,"blue"],[3,"orange"],[4,"yellow"],[5,"pink"],[6,"purple"],[6,"red"]]
def checkLine(grid,shapes,playerScore,refreshTime):
            myGrid = grid
            for i in range(len(myGrid)):
                        lineFull = True
                        for space in range(len(myGrid[i])):
                            if myGrid[i][space] == 0: 
                                lineFull = False
                        if lineFull == True:
                            playerScore += 200
                            myGrid[i] = [0,0,0,0,0,0,0,0,0,0]
                            currentLine = i
                            extraMoveList = []
                            for shape in range(len(shapes)):
                                accumulator = 0
                                currentShape = shapes[shape][0]
                                try:
                                    x,y = currentShape[0][0],currentShape[0][1]
                                except:
                                    x,y = -100,-100
                                for square in range(len(shapes[shape][0])):
                                    if shapes[shape][0][square-accumulator][1] == currentLine:
                                        if len(currentShape) == 4:
                                            if currentShape[1]  == [x,y-1] and currentShape[2] == [x+1,y-1] and currentShape[3] == [x+1,y-2]:
                                                extraMoveList.append(shape)
                                            if currentShape[1]  == [x-1,y-1] and currentShape[2] == [x,y-1] and currentShape[3] == [x-1,y-2]:
                                                extraMoveList.append(shape)                          
                                        shapes[shape][0].remove(shapes[shape][0][square-accumulator])
                                        accumulator += 1
                            for shape in range(len(shapes)):
                                for i in range(len(shapes[shape][0])):
                                    if (int(shapes[shape][0][i][1])) <= (int(currentLine)):
                                        grid[shapes[shape][0][i][1]][shapes[shape][0][i][0]] = 0
                                        if shape in extraMoveList :
                                            shapes[shape][0][i][1] += 1
                                        shapes[shape][0][i][1] += 1                                       
                                        grid[shapes[shape][0][i][1]][shapes[shape][0][i][0]] = shapes[shape][1][0]                             
            return grid,shapes,playerScore,refreshTime

def rotateShape():
    global grid,shapes
    pressRotate = False
    canRotate = True
    currentShape = shapes[len(shapes)-1][0]
    x,y = currentShape[0][0],currentShape[0][1]
    currentLowest = 20
    currentHighest = 0
    farLeft = False
    farRight = False
    for i in range(len(currentShape)):
        if (int(currentShape[i][0])) < currentLowest:
            currentLowest = int(currentShape[i][0])
        if (int(currentShape[i][0])) > currentHighest:
            currentHighest = int(currentShape[i][0])
    if currentLowest == 0:
        farLeft = True
    if currentHighest == 9:
        farRight = True
    if currentShape[1] == [x+1,y] and currentShape[2] == [x+2,y] and currentShape[3] == [x+3,y]:   
        if grid[y+1][x+1] == 0 and grid[y+2][x+1] == 0 and grid[y+3][x+1] == 0:
            grid[y][x],grid[y][x+1],grid[y][x+2],grid[y][x+3] = 0,0,0,0
            grid[y][x+1],grid[y+1][x+1],grid[y+2][x+1],grid[y+3][x+1] = 1,1,1,1
            shapes[len(shapes)-1] = [[[x+1,y+3],[x+1,y+2],[x+1,y+1],[x+1,y]],[1]]
    if farRight == False and currentHighest != 8:
        if currentShape[1] == [x,y-1] and currentShape[2] == [x,y-2] and currentShape[3] == [x,y-3] and farLeft == False:                
            if  grid[y-2][x-1] == 0 and grid[y-2][x+1] == 0 and grid[y-2][x+2] == 0:                   
                grid[y][x],grid[y-1][x],grid[y-2][x],grid[y-3][x] = 0,0,0,0                            
                grid[y-2][x-1],grid[y-2][x],grid[y-2][x+1],grid[y-2][x+2] = 1,1,1,1                    
                shapes[len(shapes)-1] = [[[x-1,y-2],[x,y-2],[x+1,y-2],[x+2,y-2]],[1]]
    if currentShape[1] == [x-2,y-1] and currentShape[2] == [x-1,y-1] and currentShape[3] == [x,y-1]:
        if grid[y][x-2] == 0 and grid[y][x-1] == 0 and grid[y-2][x-1] == 0:
            grid[y][x],grid[y-1][x-2],grid[y-1][x-1],grid[y-1][x] = 0,0,0,0
            grid[y][x-2],grid[y][x-1],grid[y-1][x-1],grid[y-2][x-1] = 2,2,2,2
            shapes[len(shapes)-1] = [[[x-2,y],[x-1,y],[x-1,y-1],[x-1,y-2]],[2]]
    if farRight == False:      
        if currentShape[1] == [x+1,y] and currentShape[2] == [x+1,y-1] and currentShape[3] == [x+1,y-2]:
            if grid[y-1][x] == 0 and grid[y-1][x+2] == 0 and grid[y-2][x] == 0:
                grid[y][x],grid[y][x+1],grid[y-1][x+1],grid[y-2][x+1] = 0,0,0,0
                grid[y-1][x],grid[y-1][x+1],grid[y-1][x+2],grid[y-2][x] = 2,2,2,2
                shapes[len(shapes)-1] = [[[x,y-1],[x+1,y-1],[x+2,y-1],[x,y-2]],[2]]              
    if currentShape[0] == [x,y] and currentShape[1] == [x+1,y] and currentShape[2] == [x+2,y] and currentShape[3] == [x,y-1]:
        if grid[y+1][x+1] == 0 and grid[y-1][x+1] == 0 and grid[y-1][x+2] == 0:
            grid[y][x],grid[y][x+1],grid[y][x+2],grid[y-1][x] = 0,0,0,0
            grid[y+1][x+1],grid[y][x+1],grid[y-1][x+1],grid[y-1][x+2] = 2,2,2,2
            shapes[len(shapes)-1] =  [[[x+1,y+1],[x+1,y],[x+1,y-1],[x+2,y-1]],[2]]
    if farRight == False:
        if currentShape[1] == [x,y-1] and currentShape[2] == [x,y-2] and currentShape[3] == [x+1,y-2]:
            if grid[y][x+2] == 0 and grid[y+1][x+1] == 0 and grid[y+1][x+2] == 0:
                grid[y][x],grid[y-1][x],grid[y-2][x],grid[y-2][x+1] = 0,0,0,0
                grid[y][x+2],grid[y-1][x],grid[y-1][x+1],grid[y-1][x+2] = 2,2,2,2
                shapes[len(shapes)-1] =  [[[x+2,y],[x,y-1],[x+1,y-1],[x+2,y-1]],[2]]
    if currentShape[1] == [x,y-1] and currentShape[2] == [x+1,y-1] and currentShape[3] == [x+2,y-1]:
        if grid[y+1][x+2] == 0 and grid[y][x+2] == 0:
            grid[y][x],grid[y-1][x],grid[y-1][x+1],grid[y-1][x+2] = 0,0,0,0
            grid[y+1][x+2],grid[y][x+2],grid[y-1][x+2],grid[y-1][x+1] = 3,3,3,3
            shapes[len(shapes)-1] = [[[x+2,y+1],[x+2,y],[x+2,y-1],[x+1,y-1]],[3]]
    if currentShape[1] == [x,y-1] and currentShape[2] == [x,y-2] and currentShape[3] == [x-1,y-2] and farLeft == False:
        if grid[y-1][x-3] == 0 and grid[y-1][x-2] == 0 and grid[y-1][x-1] == 0:
            grid[y][x],grid[y][x-1],grid[y][x-2],grid[y-1][x-2],grid[y-1][x],grid[y-2][x],grid[y-2][x-1] = 0,0,0,0,0,0,0
            grid[y-1][x-2],grid[y-1][x-1],grid[y-1][x],grid[y-2][x] = 3,3,3,3
            shapes[len(shapes)-1] = [[[x-2,y-1],[x-1,y-1],[x,y-1],[x,y-2]],[3]]
    if currentShape[1]  == [x+1,y] and currentShape[2] == [x+2,y] and currentShape[3] == [x+2,y-1]:
        if grid[y+1][x] == 0 and grid[y+1][x+1] == 0 and grid[y-1][x] == 0:
            grid[y][x],grid[y][x+1],grid[y][x+2],grid[y-1][x+2] = 0,0,0,0
            grid[y+1][x],grid[y+1][x+1],grid[y][x],grid[y-1][x]= 3,3,3,3
            shapes[len(shapes)-1] = [[[x+1,y+1],[x,y+1],[x,y],[x,y-1]],[3]]
    if currentShape[1] == [x-1,y] and currentShape[2] == [x-1,y-1] and currentShape[3] == [x-1,y-2]:
        if grid[y-1][x] == 0 and grid[y-2][x+1] == 0 and grid[y][x+1] == 0:
            grid[y][x],grid[y][x-1],grid[y-1][x-1],grid[y-2][x-1] = 0,0,0,0             
            grid[y][x-1],grid[y-1][x-1],grid[y-1][x],grid[y-1][x+1] = 3,3,3,3
            shapes[len(shapes)-1] = [[[x-1,y],[x-1,y-1],[x,y-1],[x+1,y-1]],[3]]
    if currentShape[1]  == [x-1,y] and currentShape[2] == [x,y-1] and currentShape[3] == [x+1,y-1]:
        if grid[y][x+1] == 0 and grid[y-2][x] == 0:
            grid[y][x],grid[y][x-1],grid[y-1][x],grid[y-1][x+1] = 0,0,0,0
            grid[y][x+1],grid[y-1][x],grid[y-1][x+1],grid[y-2][x] = 5,5,5,5
            shapes[len(shapes)-1] = [[[x+1,y],[x,y-1],[x+1,y-1],[x,y-2]],[5]]
    if currentShape[1]  == [x-1,y-1] and currentShape[2] == [x,y-1] and currentShape[3] == [x-1,y-2] and farLeft == False:
        if grid[y][x-1] == 0 and grid[y][x-2] == 0:
            grid[y][x],grid[y-1][x-1],grid[y-1][x],grid[y-2][x-1] = 0,0,0,0
            grid[y][x-1],grid[y][x-2],grid[y-1][x-1],grid[y-1][x] = 5,5,5,5
            shapes[len(shapes)-1] = [[[x-1,y],[x-2,y],[x-1,y-1],[x,y-1]],[5]]
    if currentShape[1]  == [x-2,y] and currentShape[2] == [x-1,y] and currentShape[3] == [x-1,y-1]:
        if grid[y+1][x-1] == 0:
            toSwap = currentShape[0]
            currentShape[0] = [x-1,y+1]
            currentShape[1] = toSwap
            grid[y][x-2] = 0
            grid[y+1][x-1] = 6
    if farRight == False:
        if currentShape[1]  == [x-1,y-1] and currentShape[2] == [x,y-1] and currentShape[3] == [x,y-2]:
            if grid[y-1][x+1] == 0:
                currentShape[0] = [x+1,y-1]
                grid[y][x] = 0
                grid[y-1][x+1] = 6
    if currentShape[1]  == [x-1,y-1] and currentShape[2] == [x,y-1] and currentShape[3] == [x+1,y-1]:
        if grid[y][x-1] == 0 and grid[y][x-2] == 0:
            currentShape[3] = [x,y-2]
            grid[y-1][x+1] = 0
            grid[y-2][x] = 6
    if currentShape[1]  == [x+1,y-1] and currentShape[2] == [x,y-1] and currentShape[3] == [x,y-2] and farLeft == False:
        if grid[y-1][x-1] == 0:
            currentShape[3] = [x-1,y-1]
            grid[y-2][x] = 0
            grid[y-1][x-1] = 6
            toSwap = currentShape[1]
            currentShape[1] = currentShape[3]
            currentShape[3] = toSwap 
    if currentShape[1]  == [x+1,y] and currentShape[2] == [x-1,y-1] and currentShape[3] == [x,y-1]:
        if grid[y][x-1] == 0 and grid[y-2][x] == 0:
            grid[y][x],grid[y][x+1],grid[y-1][x-1],grid[y-1][x] = 0,0,0,0
            grid[y][x-1],grid[y-1][x-1],grid[y-1][x],grid[y-2][x] = 7,7,7,7
            shapes[len(shapes)-1] = [[[x-1,y],[x-1,y-1],[x,y-1],[x,y-2]],[7]]
    if currentShape[1]  == [x,y-1] and currentShape[2] == [x+1,y-1] and currentShape[3] == [x+1,y-2]:
        if grid[y][x+1] == 0 and grid[y][x+2] == 0:
            grid[y][x],grid[y-1][x],grid[y-1][x+1],grid[y-2][x+1] = 0,0,0,0
            grid[y][x+1],grid[y][x+2],grid[y-1][x],grid[y-1][x+1] = 7,7,7,7
            shapes[len(shapes)-1] = [[[x+1,y],[x+2,y],[x,y-1],[x+1,y-1]],[7]]
def moveRight():
    global pressRight,canMove,shapes,grid
    pressRight = False
    canMove = True 
    for i in range(len(shapes[len(shapes)-1][0])):
        if ((shapes[len(shapes)-1][0][i][0])+1) >= 10 or ((shapes[len(shapes)-1][0][i][1])+1) >= 20:
            canMove = False
        else: 
            if grid[(shapes[len(shapes)-1][0][i][1])][((shapes[len(shapes)-1][0][i][0])+1)] != 0:
                if [((shapes[len(shapes)-1][0][i][0])+1),(shapes[len(shapes)-1][0][i][1])] not in shapes[len(shapes)-1][0]:
                    canMove = False
    if canMove == True:
        for i in range(len(shapes[len(shapes)-1][0])): 
            (shapes[len(shapes)-1][0][i][0]) += 1
            grid[(shapes[len(shapes)-1][0][i][1])][(shapes[len(shapes)-1][0][i][0])-1] = 0
        for i in range(len(shapes[len(shapes)-1][0])):    
            grid[(shapes[len(shapes)-1][0][i][1])][((shapes[len(shapes)-1][0][i][0])-1)+1] = shapes[len(shapes)-1][1][0]
def moveLeft():
    global pressLeft,canMove,grid,shapes
    pressLeft = False
    canMove = True
    for i in range(len(shapes[len(shapes)-1][0])):
        if ((shapes[len(shapes)-1][0][i][0])-1) <= -1 or ((shapes[len(shapes)-1][0][i][1])+1) >= 20:
            canMove = False
        else: 
            if grid[(shapes[len(shapes)-1][0][i][1])][((shapes[len(shapes)-1][0][i][0])-1)] != 0: 
                if [((shapes[len(shapes)-1][0][i][0])-1),(shapes[len(shapes)-1][0][i][1])] not in shapes[len(shapes)-1][0]:
                    canMove = False                        
    if canMove == True:
        for i in range(len(shapes[len(shapes)-1][0])):
            (shapes[len(shapes)-1][0][i][0]) -= 1
            grid[(shapes[len(shapes)-1][0][i][1])][(shapes[len(shapes)-1][0][i][0])+1] = 0
        for i in range(len(shapes[len(shapes)-1][0])):    
            grid[(shapes[len(shapes)-1][0][i][1])][((shapes[len(shapes)-1][0][i][0])+1)-1] = shapes[len(shapes)-1][1][0]
def resetGame():
    global grid,shapes,canMove,spawnNewItem,playerScore,refreshTime,hiScore,score2,scoreChangeList
    grid = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[1,0,1,1,1,1,1,1,1,1]]# creates a 10*20 2D array
    shapes = []  
    canMove = False
    spawnNewItem = True
    scoreChangeList = [[400,25],[800,20],[1200,15],[1600,10],[1000,6],[3000,4],[4000,2],[5000,1]]
    if playerScore > int(hiScore):
        hiScore = playerScore
        textFile = open("hiScore.txt","w")  
        textFile.write(str(hiScore))
    refreshTime = 50
    score2.pack_forget()
    score2 = Label(leftPane,text="Hi-Score: " + str(hiScore) + ("\n"),font=("Agency FB Bold",20),bg="Grey")
    score2.pack()
    playerScore = 0
def render(c,myList,myGrid,shapeList):
    global spawnNewItem , shapes , grid , hardDrop , playerScore , nextShapeToSpawn , frame , leftPane , score , title , hiScore , score2 , shapeIcons , refreshTime , scoreChangeList , speedLabel , placingItem,numberOfPieces# I don't know how to not use globals
    render = True
    if hardDrop == False:
        time.sleep(0.02)
    frame += 1
    if len(scoreChangeList) > 0:
        if playerScore > scoreChangeList[0][0]:
            refreshTime = scoreChangeList[0][1]
            scoreChangeList.remove(scoreChangeList[0])
    shapesList = [  [[[3,1],[4,1],[5,1],[6,1]],[1]]  ,[[[5,2],[3,1],[4,1],[5,1]],[2]],[[[3,2],[3,1],[4,1],[5,1]],[3]]  ,  [[[4,2],[3,2],[3,1],[4,1],],[4]] , [[[5,2],[4,2],[5,1],[6,1]],[5]] , [[[4,2],[3,1],[4,1],[5,1]],[6]] ,  [[[5,2],[6,2],[4,1],[5,1]],[7]]] # The initial grid positions of the items
    if spawnNewItem == True:
        placingItem = False
        playerScore += 10
        shapeToSpawn = nextShapeToSpawn
        nextShapeToSpawn = random.choice(shapesList) 
        myList.append(shapeToSpawn)
        numberOfPieces += 1
        for i in range(len(shapeToSpawn[0])):
            if myGrid[shapeToSpawn[0][i][1]][shapeToSpawn[0][i][0]] == 0:
                myGrid[shapeToSpawn[0][i][1]][shapeToSpawn[0][i][0]] = shapeToSpawn[1][0]
            else:
                if playerScore > 0:
                    textFile = open("AI Score List 9.txt","a")
                    textFile.write(str(playerScore) + ("\n"))
                    textFile.close()
                    print("Score: " + str(playerScore))
                    #print("Pieces Placed: " + str(numberOfPieces))
                    resetGame()               
        spawnNewItem = False

    canMove = False
    if frame % 10 == 0:
        if render == True:
            speedLabel.pack_forget() 
            score.pack_forget()
            speedLabel = Label(leftPane,text="Speed: " + str(12 - (len(scoreChangeList))),font=("Agency FB Bold",20),bg="Grey")    
            score = Label(leftPane,text="Score: " + str(playerScore) + ("\n\nNext Shape\n\n") + (shapeIcons[(nextShapeToSpawn[1][0])-1]),font=("Agency FB Bold",20),bg="Grey")
            speedLabel.pack_forget()
            speedLabel.pack(side=TOP)
            score.pack(side=TOP)
        timesToCycle = 1
        if hardDrop == True:
            timesToCycle = 20
            playerScore += 20 - shapes[len(shapes)-1][0][0][1]
            hardDrop = False
        for i  in range(timesToCycle):
            for shape in range (len(myList)):
                canMove = True
                for square in range(len(myList[shape][0])):
                    if ((myList[shape][0][square][1])+1) >= 20:
                        canMove = False
                    else:
                        if myGrid[(myList[shape][0][square][1])+1][myList[shape][0][square][0]] != 0:
                            if [(myList[shape][0][square][0]),(myList[shape][0][square][1])+1] not in myList[shape][0]:
                                canMove = False
                if canMove == True:
                    for square in range(len(myList[shape][0])):
                        myList[shape][0][square][1] += 1
                        myGrid[(myList[shape][0][square][1])-1][myList[shape][0][square][0]] = 0  
                        myGrid[(myList[shape][0][square][1])][myList[shape][0][square][0]] = myList[shape][1][0]
            
            if canMove == False:
                    spawnNewItem = True
                    grid,shapes,playerScore,refreshTime = checkLine(grid,shapes,playerScore,refreshTime)
        hardDrop = False
        
    coloursList = [[0,"black"],[1,"cyan"],[2,"blue"],[3,"orange"],[4,"yellow"],[5,"lawn green"],[6,"purple"],[7,"red"],[8,"grey"]]
    if render == True:
        c.create_rectangle(10, 10, 350, 640, fill="black")
        c.create_rectangle(60, 60, 290, 500, fill="white")
        for row in range(10):
            for column in range(20):
                if goodGraphics == True:
                    c.create_rectangle(70+(row*21),70+(column*21),90+(row*21),90+(column*21),fill=coloursList[grid[column][row]][1])
                    if (coloursList[grid[column][row]][1]) != "black":
                        c.create_rectangle(72+(row*21),72+(column*21),88+(row*21),88+(column*21),fill="white")
                        c.create_rectangle(72+(row*21),72+(column*21),88+(row*21),88+(column*21),fill=coloursList[grid[column][row]][1])
                        c.create_rectangle(70+(row*21),70+(column*21),73+(row*21),73+(column*21),fill="white")
                else:
                   c.create_rectangle(70+(row*21),70+(column*21),90+(row*21),90+(column*21),fill=coloursList[grid[column][row]][1])   
def cycle():
        c.delete(tkinter.ALL)
        render(c,shapes,grid,shapesList)
        main_window.update()
        #time.sleep(0.01)

def key(event):
    global hardDrop
    if event.char == (""):
        hardDrop = True
    """
        global shapes , grid , hardDrop , spawnNewItem ,playerScore , myGrid , refreshTime , pause , pressLeft, pressRight, pressRotate
        if event.char == ("o"):
            endGame()
        if len(shapes) > 0:
            if event.char == ("d") or event.char == ("D"):
                moveRight()        
            if event.char == ("a") or event.char == ("A"):
                moveLeft()
            if event.char == ("s") or event.char == ("S"):
                    for shape in range (len(shapes)):
                            canMove = True
                            for square in range(len(shapes[shape][0])):
                                if ((shapes[shape][0][square][1])+1) >= 20:
                                    canMove = False
                                else:
                                    if grid[(shapes[shape][0][square][1])+1][shapes[shape][0][square][0]] != 0: 
                                        if [(shapes[shape][0][square][0]),(shapes[shape][0][square][1])+1] not in shapes[shape][0]:
                                            canMove = False
                            if canMove == True:
                                for square in range(len(shapes[shape][0])):
                                    shapes[shape][0][square][1] += 1
                                    grid[(shapes[shape][0][square][1])-1][shapes[shape][0][square][0]] = 0
                                    grid[(shapes[shape][0][square][1])][shapes[shape][0][square][0]] = shapes[shape][1][0]
                    try:
                        if canMove == False:
                            spawnNewItem = True
                            grid,shapes,playerScore,refreshTime = checkLine(grid,shapes,playerScore,refreshTime)
                    except:
                        canMove = False
            if event.char == ("w") or event.char == ("W"):
                rotateShape()
            if event.char == ("#"):
                resetGame()
            if event.char == (""):
                hardDrop = True
            if event.char == ("p"):
                pause = True
            if event.char == ("o"):
                pause = False
                
    """

    


def checkGridClear(shapeList,yHeight):
        for cube in shapeList:
            if grid[cube[1]+yHeight][cube[0]] != 0:
                if [cube[0],cube[1]+yHeight] not in shapeList:
                    return False
        return True    
def nextSpace(line):
    rotationsList = [[2,1],[4,"Left"],[4,1],[1,0],[2,0],[4,0],[2,0]]
    global rotations , grid , shapes , mywindow , leftMostBlock, rightMostBlock , cItem , lowestBlock  , cLowest , leftMoves , possibleAreasToPlace , numberOfBubbles , checkNextForBubbles , backUpPosition

    cItem = shapes[len(shapes)-1]
    if len(cItem[0]) == 4:           
        leftMostBlock = 999
        rightMostBlock = -999
        for i in range (len(cItem[0])):
            if cItem[0][i][0] < leftMostBlock:
                leftMostBlock = cItem[0][i][0]
            if cItem[0][i][0] > rightMostBlock:
                rightMostBlock = cItem[0][i][0]
    #if cItem[1][0] == 4:
        #print("L = " + str(leftMostBlock))
    cLowest = 0
    for i in range(len(cItem[0])):
        if (int(cItem[0][i][1])) > cLowest:
            cLowest = int(cItem[0][i][1])
    numberOfBlocksBottomLayer = 0
    for i in range (len(cItem[0])):
        if cItem[0][i][1] == cLowest:
            numberOfBlocksBottomLayer += 1
    canPlace = True
    for y in range(0,line-cLowest+1):     
        if checkGridClear(cItem[0],y) == False:
            canPlace = False
    if canPlace == True:
        for cube in cItem[0]:
            if cube[1]+line-cLowest+1 < 20:
                if grid[cube[1]+line-cLowest+1][cube[0]] == 0:
                    if [cube[1]+line-cLowest+1,cube[0]] not in [ [cItem[0][0][1]+line-cLowest,cItem[0][0][0]],[cItem[0][1][1]+line-cLowest,cItem[0][1][0]],[cItem[0][2][1]+line-cLowest,cItem[0][2][0]],[cItem[0][3][1]+line-cLowest,cItem[0][3][0]]]:
                        numberOfBubbles += 1

        possibleAreasToPlace.append([leftMostBlock,numberOfBlocksBottomLayer,rotations,leftMoves,numberOfBubbles])
        
        #if cItem[1][0]  ==  4:
        #    print(possibleAreasToPlace[len(possibleAreasToPlace)-1])
        numberOfBubbles = 0
    if leftMoves < 10:
        moveRight()
        leftMoves += 1
        return(nextSpace(line))
    if rotations < [2,4,4,1,2,4,2][cItem[1][0]-1]:
        rotations += 1
        if rotations == rotationsList[shapes[len(shapes)-1][1][0]-1][0]:
            if rotationsList[shapes[len(shapes)-1][1][0]-1][1] == 1:
                for square in (shapes[len(shapes)-1][0]):
                    grid[square[1]][square[0]] = 0
                for counter in range (len(shapes[len(shapes)-1][0])):
                    shapes[len(shapes)-1][0][counter][1] -= 1
                    grid[shapes[len(shapes)-1][0][counter][1]][shapes[len(shapes)-1][0][counter][0]] = shapes[len(shapes)-1][1][0]
            if rotationsList[shapes[len(shapes)-1][1][0]-1][1] == "Left":
                for square in (shapes[len(shapes)-1][0]):
                    grid[square[1]][square[0]] = 0
                for counter in range (len(shapes[len(shapes)-1][0])):
                    shapes[len(shapes)-1][0][counter][0] -= 1
                    grid[shapes[len(shapes)-1][0][counter][1]][shapes[len(shapes)-1][0][counter][0]] = shapes[len(shapes)-1][1][0]
        [moveLeft() for i in range(3)]
        
        try:
            rotateShape()
        except:
            pass
        [moveLeft() for i in range(7)]
        leftMoves = 0
        return(nextSpace(line))

    if leftMoves == 10:
        if len(possibleAreasToPlace) > 0:
            possibleAreasToPlace = sorted(sorted(possibleAreasToPlace, key = lambda x : x[4]), key = lambda x : x[1], reverse = True)
            leftMostBlock = possibleAreasToPlace[0][0]
            if checkNextForBubbles == True:
                checkNextForBubbles = False
                if possibleAreasToPlace[0][4] == 0:
                    # this means it finds a better place on the above line
                    for i in range(3):
                        moveLeft()
                    for i in  range(possibleAreasToPlace[0][2]):
                        rotateShape()
                    for i in range(6):
                        moveLeft()
                    for i in range(possibleAreasToPlace[0][0]):
                        moveRight()
                    retVal = possibleAreasToPlace
                    possibleAreasToPlace = []
                    return(retVal)
                else:
                    for i in range(3):
                        moveLeft()
                    for i in  range(backUpPosition[0][2]):
                        rotateShape()
                    for i in range(6):
                        moveLeft()
                    for i in range(backUpPosition[0][0]):
                        moveRight()
                possibleAreasToPlace = []
                
                return(backUpPosition[0])
            

            if possibleAreasToPlace[0][4] > 0:
                checkNextForBubbles = True
                backUpPosition = []
                backUpPosition.append(possibleAreasToPlace[0])
                return(nextSpace(line-1))
            else:
                for i in range(3):
                    moveLeft()
                for i in  range(possibleAreasToPlace[0][2]):
                    rotateShape()
                for i in range(6):
                    moveLeft()
                for i in range(possibleAreasToPlace[0][0]):
                    moveRight()
                retVal = possibleAreasToPlace[0]
                possibleAreasToPlace = []
                return(retVal)
    leftMoves = 0
    rotations = 0
    return(nextSpace(line-1))        
numberOfBubbles = 0
possibleAreasToPlace = []
numberOfPieces = 0
leftMoves = 0
rotations = 0
# if number of bubbles isn't 0. Checks the above lines.  Sees if it can find a place that creates 0 bubbles.
#If possibleAreasToPlace[0][0] has 1 bubble or more. Change a boolean
# Which recursively checks the next line. if the line above also has 1 bubble, go back to the first alternative...
backUpPosition = 0 
checkNextForBubbles = False
main_window.bind_all("<Key>",key)
END = False
priorSpaceChosen = 0
placingItem = False
def endGame():
    global END
    END = True
while True:
        if pause == True:
            speedLabel.pack_forget() 
            speedLabel = Label(leftPane,text="Paused",font=("Agency FB Bold",50),bg="Red")
            speedLabel.pack() 
            main_window.update()
        if END == True:
            print("Exit")
            sys.exit()
        cycle()
        if len(shapes) > 0:
                cItem = shapes[len(shapes)-1]             
                rotations = 0
                if placingItem == False:
                    moveLeft()
                    moveLeft()
                    moveLeft()
                    moveLeft()
                    moveLeft()
                    nextSpaceChosen = nextSpace(19)
                    #print(nextSpaceChosen[4])
                    placingItem = True
                    hardDrop = True
                    render(c,shapes,grid,shapesList)


# Hi - Score 12,095         
