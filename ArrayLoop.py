import random

##generating an empty list
myList = []

##appending elements in the list using random method
for i in range(0, 20):
    myList.append(random.randint(10,1000))

##finding mean value from the list
sum = 0
for i in range(0, len(myList)):
    sum += myList[i]
mean = sum/len(myList)


##finding smallest number
minNum = myList[0]
for i in range(0, len(myList)):
    if minNum > myList[i]:
        minNum = myList[i]


##finding largest number
maxNum = myList[0]
for i in range(0, len(myList)):
    if maxNum < myList[i]:
        maxNum = myList[i]


##printing results
print("\n\tLIST ELEMENTS")
print("The values in the list are :", myList)
print("\n\tMEAN VALUE")
print("The mean value of the list is : ", int(mean))
print("\n\tMINIMUM VALUE")
print("The minimum value of the list is :", minNum, " &  its index is :", myList.index(minNum))
print("\n\tMAXIMUM VALUE")
print("The maximum value of the list is :", maxNum, " &  its index is :", myList.index(maxNum), "\n")
