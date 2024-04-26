tourPath = []

while True:
    
    inputStops = input("Enter stop and press enter: \n").title()
    if inputStops == "Done":
        break
    
    tourPath.append(inputStops)
    print(tourPath)

print("Here is your tour path: ", tourPath)


