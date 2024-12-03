
#creating a list to store the ice cream flavors in

iceCreamFlavors = []

def addFlavor(flavorName,flavorDesc):
    flavor = {
        'name': flavorName,
        'description': flavorDesc
    }
    #adding a flavor to the list
    iceCreamFlavors.append(flavor)

#adding an update function

def updateFlavor(oldFlavor, newFlavor, newDesc):
    #locate flavor by old name
    for flavor in iceCreamFlavors:
        if flavor['name'] == oldFlavor:
            #updating the name
            flavor['name'] = newFlavor
            flavor['description'] = newDesc
            return True #checks if update went through
        return False #when flavor is not found

def displayFlavors():
    #display the flavors in the list
    for flavor in iceCreamFlavors:
        print(f"Flavor: {flavor['name']} , Description: {flavor['description']}")

#flavors added below
addFlavor('Chocolate Fudge', 'Sweet cocoa with fudge')
addFlavor('Strawberry Banana', 'Sweet & fruity')
addFlavor('Cookies & Cream', 'Vanilla & chocolate with chocolate cookie chunks')

def inputAddFlavor():
    flavorName = input("Enter flavor name: ")
    flavorDesc = input("Enter flavor description: ")
    addFlavor(flavorName, flavorDesc)
    print(f"Flavor: {flavorName} , added successfully.")

while True:
    inputAddFlavor()
    addedFlavor = input("Would you like to add another flavor? (y/n): ")
    if addedFlavor != 'y':
        break



#if updateFlavor('Chocolate Fudge', 'Mint Chocolate', 'Minty with chocolate chips'):
#    print("Flavor updated!")
#else:
#    print("Flavor not updated!")


displayFlavors()


