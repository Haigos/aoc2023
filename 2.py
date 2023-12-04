bag = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""

bagAsArray = bag.split("\n")
maxRedCubes = 12
maxgreenCubes = 13
maxBlueCubes = 14
idSum = 0
powerSum = 0
for i in range(0, len(bagAsArray) -1 ):
    validBag = True
    minRedCubesRequired = None
    minGreenCubesRequired = None
    minBlueCubesRequired = None
    currentBagArray = bagAsArray[i].split(":")[1].split(";")
    for j in range(0, len(currentBagArray) ):
        cubeArray = currentBagArray[j].split(",")
        red = 0
        green = 0
        blue = 0
        for k in cubeArray:
            strippedArray = k.strip()
            if "red" in strippedArray:
                red = int(strippedArray.split(" ")[0])
                if minRedCubesRequired == None:
                    minRedCubesRequired = red
                elif minRedCubesRequired < red:
                    minRedCubesRequired = red

            if "green" in strippedArray:
                green = int(strippedArray.split(" ")[0])
                if minGreenCubesRequired == None:
                    minGreenCubesRequired = green
                elif minGreenCubesRequired < green:
                    minGreenCubesRequired = green

            if "blue" in strippedArray:
                blue = int(strippedArray.split(" ")[0])
                if minBlueCubesRequired == None:
                    minBlueCubesRequired = blue
                elif minBlueCubesRequired < blue:
                    minBlueCubesRequired = blue

        if red > maxRedCubes or green > maxgreenCubes or blue > maxBlueCubes:
            validBag = False
           
    if minRedCubesRequired != None and minGreenCubesRequired != None and minBlueCubesRequired != None:
        power = minRedCubesRequired * minGreenCubesRequired * minBlueCubesRequired
    elif minRedCubesRequired != None and minGreenCubesRequired != None:
        power = minRedCubesRequired * minGreenCubesRequired
    elif minRedCubesRequired != None and minBlueCubesRequired != None:
        power = minRedCubesRequired * minBlueCubesRequired
    elif minGreenCubesRequired != None and minBlueCubesRequired != None:
        power = minGreenCubesRequired * minBlueCubesRequired
    elif minRedCubesRequired != None:
        power = minRedCubesRequired
    elif minGreenCubesRequired != None:
        power = minGreenCubesRequired
    elif minBlueCubesRequired != None:
        power = minBlueCubesRequired
        
    if validBag:
        idSum += i + 1
  
    powerSum += power

print("The sum of the valid bags is", idSum)  
print("The sum of the power is", powerSum)
            
    

