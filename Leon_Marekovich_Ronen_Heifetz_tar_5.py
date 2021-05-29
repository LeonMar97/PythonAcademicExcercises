import re
csvFileName ="us_postal_codes.csv"
citiesFileName="2019_largest_cities.txt"
cityFile=open(citiesFileName)
csvFile=open(csvFileName)
csvList=csvFile.read().split('\n')

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#splits by postal city and state
def splitPostal():
    citiesPostal = []
    for i in csvFile:
        temp = i.split(',')
        if len(temp) > 3:
            citiesPostal.append((temp[0], temp[1], temp[2]))
    return citiesPostal
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#creating requested city list
def bigCity():
    citiesList=cityFile.read().split('\n')[1:]
    for line in citiesList:
        print(line.split('\t')[1])
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(splitPostal())
#bigCity()