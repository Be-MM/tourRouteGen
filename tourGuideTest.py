tourRoutes = {}

while True:
    inputGuides = input("Enter the name of each tour guide and press enter. Type 'Done' when you have entered all names: \n").title()
    if inputGuides == "Done":
        break

    tourRoutes.update(inputGuides)
    print(tourRoutes)


