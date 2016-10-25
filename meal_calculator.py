import sys 

mealCost = float(input())
tipPercent = int(input())
taxPercent = int(input())

tip = mealCost * tipPercent / 100
tax = mealCost * taxPercent / 100
totalCost = mealCost + tip + tax 
totalCost = round(totalCost)

# same output - 4 version print style
print("%s %s %s" % ('The total meal cost is', totalCost, 'dollars.'))
print("{} {} {}" .format ('The total meal cost is', totalCost, 'dollars.'))
print("{} {:d} {}" .format ('The total meal cost is', totalCost, 'dollars.'))
print("The total meal cost is " + str(totalCost) + " dollars.")