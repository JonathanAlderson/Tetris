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
    global spawnNewItem , shapes , grid , hardDrop , playerScore , nextShapeToSpawn , frame , leftPane , score , title , hiScore , score2 , shapeIcons , refreshTime , scoreChangeList , speedLabel , placingItem# I don't know how to not use globals 
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
        #nextShapeToSpawn = [[[3,1],[4,1],[4,2],[4,3]],[3]]
        nextShapeToSpawn = random.choice(shapesList) #random.choice(shapesList)
        myList.append(shapeToSpawn)
        
        for i in range(len(shapeToSpawn[0])):
            if myGrid[shapeToSpawn[0][i][1]][shapeToSpawn[0][i][0]] == 0:
                myGrid[shapeToSpawn[0][i][1]][shapeToSpawn[0][i][0]] = shapeToSpawn[1][0]
            else:
                if playerScore > 0:
                    textFile = open("AI Score List 2.txt","a")
                    textFile.write(str(playerScore) + ("\n"))
                    textFile.close()
                    if playerScore > 3000:
                        print("Your score was pretty sick, it was " + str(playerScore))
                    else:
                        print("Your score was not very good, it was " + str(playerScore))
                    resetGame()               
        spawnNewItem = False
        
    canMove = False
    if frame % 10 == 0:
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
def key(event):   
        global shapes , grid , hardDrop , spawnNewItem ,playerScore , myGrid , refreshTime , pause , pressLeft, pressRight, pressRotate
        if event.char == ("o"):
            endGame()
        if len(shapes) > 0:
            if event.char == ("d") or event.char == ("D"):
                #print("Press Right")
                moveRight()        
            if event.char == ("a") or event.char == ("A"):
                #print("Press Left")
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


def checkGridClear(shapeList,yHeight):
        for cube in shapeList:
            if grid[cube[1]+yHeight][cube[0]] != 0:
                #print("Grid obj isn't 0")
                if [cube[0],cube[1]+yHeight] not in shapeList:
                    #print("False " + str(cube[1]+yHeight))
                    return False
        return True

#              "","Line","B L","L","Cube","Z","T","S"
        
def nextSpace(line):
    rotationsList = [[2,1],[4,"Left"],[4,1],[0,0],[2,0],[4,0],[2,0]]
    global rotations , grid , shapes , mywindow , leftMostBlock, rightMostBlock , cItem , lowestBlock  , cLowest , leftMoves , possibleAreasToPlace

    cItem = shapes[len(shapes)-1]
    if len(cItem[0]) == 4:           
        leftMostBlock = 999
        rightMostBlock = -999
        for i in range (len(cItem[0])):
            if cItem[0][i][0] < leftMostBlock:
                leftMostBlock = cItem[0][i][0]
            if cItem[0][i][0] > rightMostBlock:
                rightMostBlock = cItem[0][i][0]
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
        #print("Can Place on line " + str(line))
        possibleAreasToPlace.append([leftMostBlock,numberOfBlocksBottomLayer,rotations,leftMoves])
        #return(leftMostBlock)
    if leftMoves < 10:
        moveRight()
        leftMoves += 1
        return(nextSpace(line))
        
    if rotations < 4:
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
            #print("Rotate Shape")
        except:
            #print("Error")
            pass
        [moveLeft() for i in range(7)]
        leftMoves = 0
        return(nextSpace(line))

    if leftMoves == 10:
        #print("Left Moves == 10")
        #time.sleep(0.5)
        #print("Length is")
        #print(len(possibleAreasToPlace))
        #time.sleep(0.5)
        if len(possibleAreasToPlace) > 0:
            possibleAreasToPlace = sorted(possibleAreasToPlace,key=operator.itemgetter(1),reverse=True)
            #print("Sorted list = ")
            #print(possibleAreasToPlace)
            leftMostBlock = possibleAreasToPlace[0][0]
            #print("Placing in " + str(leftMostBlock))
            #time.sleep(1)
            for i in range(3):
                moveLeft()
            for i in  range(possibleAreasToPlace[0][2]):
                rotateShape()
            for i in range(6):
                moveLeft()
            for i in range(possibleAreasToPlace[0][0]):
                #print("Moving Right")
                moveRight()
            possibleAreasToPlace = []
            return(leftMostBlock)
    leftMoves = 0
    rotations = 0
    #print("Check Above Line")
    return(nextSpace(line-1))
        
        
    
possibleAreasToPlace = []
leftMoves = 0
rotations = 0
main_window.bind_all("<Key>",key)
END = False
priorSpaceChosen = 0
placingItem = False
def endGame():
    global END
    END = True
    

while True:
    #try:
    
        if pause == True:
            speedLabel.pack_forget() 
            speedLabel = Label(leftPane,text="Paused",font=("Agency FB Bold",50),bg="Red")
            speedLabel.pack() 
            main_window.update()
        if END == True:
            print("Exit")
            sys.exit()
        #else:
        #   timeToSleep = int(refreshTime) / 1000 
        #   time.sleep(timeToSleep)
        cycle()
            

        ### AI ###
        if len(shapes) > 0:
                cItem = shapes[len(shapes)-1]
#####################################################################             
                rotations = 0
                if placingItem == False:
                    #print(["","Line","B L","L","Cube","Z","T","S"][cItem[1][0]])
                    moveLeft()
                    moveLeft()
                    moveLeft()
                    moveLeft()
                    moveLeft()
                    nextSpaceChosen = nextSpace(19)
                    #print(nextSpaceChosen)
                    placingItem = True
                    hardDrop = True
                    #frame = 10
                    render(c,shapes,grid,shapesList)
                    #time.sleep(1)



                
                


# 1 = Line
# 2 = Backwards L
# 3 = L
# 4 = Square
# 5 = Z
# 6 = T
# 7 = S


# Hi - Score 12,095         
