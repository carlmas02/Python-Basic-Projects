#Conways game of life

import random,time,copy
WIDTH = 60
HEIGHT = 20

#list of list for cells:
nextCells = []

for x in range(WIDTH):
    column = []
    for y in range(HEIGHT):
        if random.randint(0,1) == 0:
            column.append('#') #living cell
        else :
            column.append(' ') #dead cell
    nextCells.append(column)

#Main program
while True:
    print("\n\n\n\n\n")
    currentCells = copy.deepcopy(nextCells)

    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='') # Print the # or space.
        print()

    for x in range(WIDTH):
        for y in range(HEIGHT):
            leftCoord = (x - 1)% WIDTH
            rightCoord = (x + 1)%WIDTH
            aboveCoord = (y - 1)%HEIGHT
            belowCoord = (y + 1)%HEIGHT

            # Count number of living neighbors:
            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbors += 1  # Top-left neighbor is alive.
            if currentCells[x][aboveCoord] == '#':
                numNeighbors += 1  # Top neighbor is alive.
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbors += 1  # Top-right neighbor is alive.
            if currentCells[leftCoord][y] == '#':
                numNeighbors += 1  # Left neighbor is alive.
            if currentCells[rightCoord][y] == '#':
                numNeighbors += 1  # Right neighbor is alive.
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbors += 1  # Bottom-left neighbor is alive.
            if currentCells[x][belowCoord] == '#':
                numNeighbors += 1  # Bottom neighbor is alive.
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbors += 1  # Bottom-right neighbor is alive.

            # Set cell based on Conway's Game of Life rules:
            if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
                nextCells[x][y] = '#'
            elif currentCells[x][y] == ' ' and numNeighbors == 3:
                nextCells[x][y] = '#'
            else:
                nextCells[x][y] = ' '
    time.sleep(0.5)  # Add a 1-second pause to reduce flickering.


