
#create a list of the tour route. 'Machine Shop', 'Injection Mold', 'Mechanism Department', 'Laser', 'Tile', 'Paint Bay', 'Assembly', 'Rubber', 'Photo Op', 'Outside', 'Screen', 'Engineering', 'Office', 'Conference Room'
tourPath = []
#create a dictionary of dictionaries where the keys are the names of the tour guides and the values are an empty list.
tourRoutes = {}

#iterate through the list,

#create function that takes two arguments: the path of the tour (empty list), individual routes (empty dictionary)
#function should prompt for user input to define the tour path first (done)
#I also want to prompt for tour guide names. I imagine those will be stored as keys. The tour path will be rotated and assigned as a value to each of the keys
#After the key:value pairs are assigned to one another, they need to be printed and displayed



def tourRouteGenerator(tourPath, tourRoutes):
    print("""
          Hello! Welcome to the tour route generator. Follow the instructions below to generate a route for each tour guide.

          1. Enter each stop along your decided path. Make sure to press the enter/return key after each stop so we can add it to the path.
          2. After you are finished entering each stop, type "Done" and press the enter/return key to complete the tour path.
          3. Enter the name of each tour guide. This is so we can assign each person their own speacial route. 
          4. After you are finished entering each name, type "ALL DONE" and press the enter/return key to let us know your finished.

          After each stop and name is entered, we will generate a route for each tour guide and assign it to them.

          """)
    
    #the following code takes user input and adds that input to a list that will be printed at the end. This will be the tour path. 

    
    tourPath = []

    while True:
    
        inputStops = input("Enter stop and press enter: \n").title()
        if inputStops == "Done":
            break
    
        tourPath.append(inputStops)
        print(tourPath)

    print("Here is your tour path: ", tourPath)

    #maybe add in a verification step to allow for any corrections to the path

    #the following code takes tour guide names from user input and stores those names as keys inside a dictionary
    tourRoutes = {}

    while True:
        inputGuides = input("Enter the name of each tour guide and press enter. Type 'Done' when you have entered all names: \n").title()
        if inputGuides == "Done":
            break

        tourRoutes.update(inputGuides)
        print(tourRoutes)


 