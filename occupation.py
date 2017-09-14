source = open('occupations.csv', 'r')
file = source.read()
print(file)
occupationsList = file.split('\r\n')
print(occupationsList)
occupationsDict = {}
print(occupationsDict)
