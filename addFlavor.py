
#creating a list to store the ice cream flavors in

iceCreamFlavors = []

def addFlavor(flavorName,flavorDesc):
    flavor = {
        'name': flavorName,
        'description': flavorDesc
    }
    #adding a flavor to the list
    iceCreamFlavors.append(flavor)

def displayFlavors():
    #display the flavors in the list
    for flavor in iceCreamFlavors:
        print(f"Flavor: {flavor['name']} , Description: {flavor['description']}")

#flavors added below
addFlavor('Chocolate Fudge', 'Sweet cocoa with fudge')
addFlavor('Strawberry Banana', 'Sweet & fruity')
addFlavor('Cookies & Cream', 'Vanilla & chocolate with chocolate cookie chunks')

displayFlavors()


