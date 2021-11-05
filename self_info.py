
def GetName():
    nameFunc = input("What is your name:")
    return nameFunc

def GetAge():
    ageFunc = input("How old are you:")
    return ageFunc

def GetAddress():
    addressFunc = input("Where do you live:")
    return addressFunc

def DisplayOutput(nameFunc, ageFunc, addressFunc):
    print(f"Hi, my name is {nameFunc}. I am {ageFunc} years old and I live in {addressFunc}.")


# Create a program that will ask for name, age and address. 
# Display those details in the following format.
# Hi, my name is _____. I am ____ years old and I live in _____ .

# Steps
# ask for the name and save as variable
Name = GetName()
# ask for the age and save as variable
Age = GetAge()
# ask for the address and save as variable
Address = GetAddress()
# display the name, age and variable
Output = DisplayOutput(Name, Age, Address)