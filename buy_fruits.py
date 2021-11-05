def ShowScene():
    print("A family who lived in the City of Dasmariñas, Cavite, is a happy family that loves to do household chores together and that includes going to the market. One day, the daughter named, Dani, wants to buy apples she has seen in the market yesterday, but she does not know how many apples she can buy with the amount of money she saved. So she asked her mother about this matter and her mother said:")

def GetMoney():
    getMoneyFunc = int(input("Dear, how much money do you have?: "))
    return getMoneyFunc

def GetPrice():
    getPriceFunc = int(input("Do you know how much does one apple costs?: "))
    return getPriceFunc

def ShowScene2():
    print("So her mother calculated the amount of the money that Dani has to the price of the apple by dividing the two.")

def GetApples(getMoneyFunc, getPriceFunc):
    getAppleFunc = int(getMoneyFunc//getPriceFunc)
    return getAppleFunc

def ShowScene3():
    print("After dividing the money of Dani and the apple's price, mother got to know how many pieces of apples they can buy. Now, she wanted to know how much money will be left for her daughter, Dani, after buying. So, she multiply the pieces of apple and apple's price, then the product will be subtracted from the amount of money that Dani has.")

def GetChange(getMoneyFunc, getPriceFunc, getAppleFunc):
    getChangeFunc = int(getMoneyFunc-(getPriceFunc*getAppleFunc))
    return getChangeFunc

def ShowScene4():
    print("When mother already calculated all the variables given, she turned to Dani and said,")

def DisplayApples(getAppleFunc, getChangeFunc):
    print(f"You can buy {getAppleFunc} apples and your change is {getChangeFunc} pesos.")
# Create a program which you will enter the amount of money you have, it will also ask for the price of an apple.
# Display the maximum number of apples that you can buy and the remaining money that you will have.
# Display the output in the following format.
# You can buy ___ apples and your change is ___ pesos.

#Steps
# add scenraio
Set = ShowScene()
# 1. ask for the money on hand and save to variable
Money = int(GetMoney())
# 2. ask for the price of an apple and save to variable
Price = int(GetPrice())
# add 2nd scenario
Set2 = ShowScene2()
# 3. compute the amount of money and price of apple by dividing the two variables to get how many pieces of apple can buy
Apples = int(GetApples(Money, Price))
# add 3rd scenario
Set3 = ShowScene3()
# 4. compute the pieces and price of apple by multiplying it and subtract its product from the amount of money
Change = int(GetChange(Money, Price, Apples))
# add a scenario
Set4 = ShowScene4()
# 5. display the money, price, and pieces
Output = DisplayApples(Apples, Change)