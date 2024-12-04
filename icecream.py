from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

#main input categories

class IceCream(BaseModel):
    flavorName: str
    description: str
    price: float
    count: int
    id: int

flavors = {
    0: IceCream(flavorName="Lemon Sherbet", description="tangy, sweet, lemon flavor", price=1.50, count=25, id=0),
    1: IceCream(flavorName="Chocolate", description="cocoa, rich, sweet flavor", price=2.50, count=100, id=1),
    2: IceCream(flavorName="Vanilla", description="vanilla bean flavor", price=1.25, count=150, id=2),
}

@app.get("/")
def index() -> dict[str, dict[int, IceCream]]:
    return {"flavors": {k: v.dict() for k, v in flavors.items()}}

@app.get("/flavors/{flavorID}")
def queryFlavorByID(flavorID: int) -> IceCream:
    if flavorID not in flavors:
        raise HTTPException(
            status_code=404, detail="flavor not found"
        )
    return flavors[flavorID]

Selection = dict[
    str, str | int | float | None
]

@app.get("/flavors")
def queryFlavorsByParam(
        flavorName: str | None = None,
        description: str | None = None,
        price: float | None = None,
        count: int | None = None,
        id: int | None = None,
) -> dict[str, Selection]:
    def checkFlavor(flavors: IceCream) -> bool:
        return all(
            (
                flavorName is None or flavors.flavorName == flavorName,
                description is None or flavors.description == description,
                price is None or flavors.price == price,
                count is None or flavors.count == count,
                id is None or flavors.id == id,
            )

        )

    selection = [flavor.dict() for flavor in flavors.values() if checkFlavor(flavor)]
    return{
        "query": {"Flavor Name": flavorName, "Description": description, "Price": price, "Count": count, "Id": id},
        "selection": selection,

    }

@app.post("/flavors")
def createFlavor(flavor: IceCream) -> dict[str, IceCream]:

    if flavor.id in flavors:
        raise HTTPException(status_code=400, detail=f"flavor with id #{flavor.id} already exists.")
    flavors[flavor.id] = flavor
    return {"added": flavor}






#creating a list to store the ice cream flavors in
#iceCreamFlavors = []
'''
def addFlavor(flavorName, flavorDesc, flavorPrice, flavorCount, flavorID):
    flavor = IceCream(
        flavor=flavorName,
        description=flavorDesc,
        price=flavorPrice,
        count=flavorCount,
        id=flavorID
    )
    # appending flavors
    iceCreamFlavors.append(flavor.model_dump())
'''

'''
 def addFlavor(flavorName,flavorDesc):
    flavor = {
        'name': flavorName,
        'description': flavorDesc
    }
    #adding a flavor to the list
    iceCreamFlavors.append(flavor) 
'''
#adding an update function
'''
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
        elif addedFlavor == 'n':
            break
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

@app.get("/")
async def root():
    return {displayFlavors()}
'''