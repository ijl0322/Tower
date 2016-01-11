def printTower():
    while True:
        tower_height = int(raw_input("Enter a number between 1 to 24:"))
        if tower_height > 0 and tower_height <= 24:
            break
        else:
            print "invalid input, please try again"
    for i in range(tower_height):
        print (tower_height - i -1)*" " + "#"*(i+1)*2  

printTower()