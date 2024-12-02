#print("200 is a great number") #string
#print(3.5)  #float
#print(3)    #integer


#creating variables

#calc_to_seconds = cts
#calc_to_units = cTU
#cts = 24 * 60 * 60

calcToSecs = 24 * 60 * 60
calcToMins = 24 * 60
calcToHours = 24


#userInputUnit = input("Please specify unit to convert to ('hours' , 'minutes' , 'seconds') :\n")

while True:
    try:

        userInputUnit = input("Please specify unit to convert to ('hours' , 'minutes' , 'seconds') :\n")

        if userInputUnit == "hours":
            cTU = calcToHours
            break
        elif userInputUnit == "minutes":
            cTU = calcToMins
            break
        elif userInputUnit == "seconds":
            cTU = calcToSecs
            break
        else:
            print("try again by typing 'hours', 'minutes', or 'seconds' ")
    except ValueError:
            print("error, try again.")




def daysToUnits(numDays):
    return(f"{numDays} days are {numDays * cTU} {userInputUnit}")


userInput = input(f"Enter number of days to convert to {userInputUnit}:\n")
userInputNum = int(userInput)

calcVal = daysToUnits(userInputNum)
print(calcVal)


#def scopeCheck(numDays):
   #  myVar = "Variable inside function"
    # print(unitName)
    # print(numDays)
    # print(myVar)


#common way below
#print("20 days are " + str(50) + " minutes")
#print(20 * 24 * 60)
#more elegant way
#f stands for format
#print(f"20 days are {20 * 24 * 60} minutes")
#print(f"35 days are {35 * 24 * 60} minutes")
#print(f"50 days are {50 * 24 * 60} minutes")
#print(f"110 days are {110 * 24 * 60} minutes")
#for seconds
#print(f"20 days are {20 * ctu} {unitName}")

#functions
#daysToUnits(20, "Awesome!")
#daysToUnits(35, "Looks Great!")

#scopeCheck(20)








