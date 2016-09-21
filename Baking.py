# 1L = 4.2 cups
def convert(L):
    cups = round((float(L)* 4.2), 2)
    return cups


print("This program will convert Liters to cups")
liters = raw_input("How many Liters?")
cups = convert(liters)
print(liters + " Liters is equal to " + str(cups) + " cups")
