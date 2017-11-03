list1=[1,2,3]

print("max(list1): ",max(list1))

def GetMax(listA):
    big=0
    for element in listA:
        if element>big:
            big=element
    return big

print("max(list1): ",GetMax(list1))
