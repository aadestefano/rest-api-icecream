
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

#delete function for removing flavor from list
def delFlavor(flavorName):
    for flavor in iceCreamFlavors:
        if flavor['name'] == flavorName:
            iceCreamFlavors.remove(flavor)
            return True
    return False


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


def inputUpdateFlavor():
    oldFlavorName = input("Enter flavor you wish to update: ")
    newFlavorName = input("Enter new flavor name: ")
    newDesc = input("Enter new flavor description: ")

    if updateFlavor(oldFlavorName, newFlavorName, newDesc):
        print(f"Flavor: {oldFlavorName} , updated successfully.")
    else:
        print("Flavor not updated successfully.")


def inputDelFlavor():
    flavorName = input("Enter the flavor you wish to delete: ")
    if delFlavor(flavorName):
        print(f"Flavor: {flavorName} successfully deleted.")
    else:
        print(f"Flavor: {flavorName} not found.")



while True:
    userChoice = input("Do you wish to add, update, or delete a flavor? (add/update/delete/quit)\n")
    if userChoice == 'add':
        inputAddFlavor()
        addedFlavor = input("Would you like to continue? (y/n): ")
        if addedFlavor == 'y':
            continue #starts loop from the top
    elif userChoice == 'update':
        print(f"Flavors: {displayFlavors()}")
        inputUpdateFlavor()
    elif userChoice == 'delete':
        displayFlavors()
        inputDelFlavor()
    elif userChoice == 'quit':
        break
    else:
        print("Invalid choice.")


displayFlavors()


