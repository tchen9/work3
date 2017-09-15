source = open('occupations.csv', 'r')
file = source.read()
print(file)
occupationsList = file.split('\r\n')
occupationsList.remove('')
occupationsList.remove('Job Class,Percentage')
print(occupationsList)
occupationsDict = {}
print(occupationsDict)
tempList = []
for x in occupationsList:
    if(x.find('''",''') != -1):
        tempList = x.split('''",''')
        tempList.insert(0, tempList.pop(0) + '''"''')
        print(tempList)
        occupationsDict[tempList[0]] = float(tempList[1])
    else:
        tempList = x.split(",")
        print(tempList)
        occupationsDict[tempList[0]] = float(tempList[1])

print(occupationsDict)

def pickOccupation():
    blah = 0





        




        
        
