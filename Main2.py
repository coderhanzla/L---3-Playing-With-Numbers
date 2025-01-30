LargeNum = int(input("Enter the largest number: "))
SmalNum = int(input("Enter the Smallest number: "))

while SmalNum:
    temp = SmalNum
    SmalNum = LargeNum % SmalNum
    LargeNum = temp

print("HCF is: ", LargeNum)