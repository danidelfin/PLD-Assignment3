
def NumberApple():
    numberAppleFunc = int(input("How many apples do you want to buy?:"))
    return numberAppleFunc

def NumberOrange():
    numberOrangeFunc = int(input("How many oranges do you want to buy?:"))
    return numberOrangeFunc

def AmountApple():
    amountAppleFunc = int(input("How much does one apple costs?:"))
    return amountAppleFunc

def AmountOrange():
    amountOrangeFunc = int(input("How much does one orange costs?:"))
    return amountOrangeFunc

def PayApple(numberAppleFunc, amountAppleFunc):
    payAppleFunc = int(numberAppleFunc*amountAppleFunc)
    return payAppleFunc

def PayOrange(numberOrangeFunc, amountOrangeFunc):
    payOrangeFunc = int(numberOrangeFunc*amountOrangeFunc)
    return payOrangeFunc

def FullAmount(payAppleFunc, payOrangeFunc):
    fullAmountFunc = int(payAppleFunc+payOrangeFunc)
    return fullAmountFunc

def DisplayTotal(fullAmountFunc):
    print(f"The total amount is {fullAmountFunc}.")

# Create a program that will ask how many apples and oranges you want to buy.
# Display the total amount you need to pay if apple price is 20 pesos and orange is 25.
# Display the output in the following format.
# The total amount is ______.

# Steps
# 1. ask how many apples to buy and save to variable
Apple = int(NumberApple())
# 2. ask how many oranges to buy and save to variable
Orange = int(NumberOrange())
# 3. ask the price of the apple and save to variable
PriceA = int(AmountApple())
# 4. ask the price of the oranges and save to variable
PriceO = int(AmountOrange())
# 5. compute the number of apples to buy and the price of the apple by multiplying it
TotalA = int(PayApple(Apple, PriceA))
# 6. compute the number of oranges to buy and the price of the orange by multiplying it
TotalO = int(PayOrange(Orange, PriceO))
# 7. add the product of number of apple and price of apple to the product of the number of orange and price of orange
Sum = int(FullAmount(TotalA, TotalO))
# 8. display the toal amount of the apples and oranges
Output = DisplayTotal(Sum)