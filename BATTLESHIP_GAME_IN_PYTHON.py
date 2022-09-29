from random import randint # this will help to import random places of the ships
grid_size = 9 # grid size 
Hidden_Pattern=[[' ']*grid_size for x in range(grid_size)] # here we give the grid the parameters we need it to be, this being the hidden grid which will have the ships 
Guess_Pattern=[[' ']*grid_size for x in range(grid_size)] # here we give the grid the parameters we need it to be, this being the guess grid which will have the ones we guess 

num={'0':0,'1':1, '2':2,'3':3,'4':4,'5':5,'6':6,'7':7, '8':8} #here we are defining each number to assign to each guess

def drawBoard(myBoard):
    print("+---+---+---+---+---+---+---+---+---+---+---+\n") # this will create how the grid looks and forms
    print('|   | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |')
    row_num=1
    for row in myBoard:
        print("+---+---+---+---+---+---+---+---+---+---+---+\n") # here we used %d and %s to have it as place holders for when we insert a x or y on the grid, and then we also do .joinrow to make the grid come together
        print("| %d | %s |   |"%(row_num," | ".join(row)))
        row_num +=1


def main():
    #Enter the row number between 1 to 9
    row=input('Enter a row(Y): ') # here we prompt user to enter row 
    while row not in '123456789': # set a boolean to make sure user enters correct numbers 
        print("Invalid row. ")
        row=input('Enter a row(Y): ')
    column=input('Enter a colum(X): ')
    while column not in '012345678':
        print("Invalid row. ")
        column=input('Enter a colum(X): ')
    return int(row)-1,num[column] #here we are return the int row and column to be able to keep returning until the correct numbers are entered 


#Function that creates the ships
def setupBoard(myBoard):
    for ship in range(5): # number of random places ships 
        ship_r, ship_cl=randint(0,8), randint(0,8) # parameters for where the ships will be placed 
        while myBoard[ship_r][ship_cl] =='X': # this will indicate a ship hit 
            ship_r, ship_cl = randint(0, 8), randint(0, 8)
        myBoard[ship_r][ship_cl] = 'S' 


def hitOrMiss(myBoard): # here we are defining a hit or miss of the ships 
    count=0
    for row in myBoard:
        for column in row:
            if column=='X':
                count+=1
    return count

setupBoard(Hidden_Pattern),drawBoard(Hidden_Pattern) #### had a little problem putting the grid together like one on top of another like the example
# here we are printing out the actual board with the ships placed in them 
 
while True: # here we are creating the parameters with a while true statement
    print('BATTLESHIP')
    drawBoard(Guess_Pattern)
    row,column =main()
    
    if Hidden_Pattern[row][column] =='S': # when we hit on S it will print HIT
        print('HIT ')
        Guess_Pattern[row][column] = 'X' # this means it will be a X if we hit and subsitiute the S from the hidden board 
    elif Guess_Pattern[row][column] == 'S': ### here  i waas trying to make it come together where i did not need to grids but could not make the S turn into a X once it was hit hence the two grids up top 
        print('HIT')
        Hidden_Pattern[row][column] = 'X'
    else:
        print('MISS') # it will print other wise miss 
        Guess_Pattern[row][column] = '.'# this will be in the grid (.) instead of a X when you miss as we 

    if  hitOrMiss(Guess_Pattern)|hitOrMiss(Hidden_Pattern) == 5: # once 5 X's are reached the game will print game over 
        print("GAME OVER!! ")
        break
