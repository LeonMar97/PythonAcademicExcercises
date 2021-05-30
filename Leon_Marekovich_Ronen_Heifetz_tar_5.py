import re
csvFileName ="us_postal_codes.csv"
citiesFileName="2019_largest_cities.txt"
cityFile=open(citiesFileName)
csvFile=open(csvFileName)
csvList=csvFile.read().split('\n')

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#splits by postal city and state
def splitPostal(csvFile):
    citiesPostal = []
    for i in csvFile:
        temp = i.split(',')
        if len(temp) > 3:
            citiesPostal.append((temp[0], temp[1] + ' ' + temp[2]))
    return citiesPostal
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#creating requested city list
def bigCity():
    biggestCities = []
    citiesList=cityFile.read().split('\n')[1:]
    for line in citiesList:
        biggestCities.append(line.split('\t')[1])
    return biggestCities

#decompose a string into "<city name> <state name> using REGEX
def decompose(s):
    temp = re.search(r'[a-z][A-Z]', s)
    return s[0:temp.span()[0]+1] + ' ' + s[temp.span()[0]+1:]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
cities = bigCity()
biggestCities = [decompose(x) for x in cities]
allCities = splitPostal(csvList)
PostalBigCities = [x[0] + ' ' + x[1] for x in allCities if x[1] in biggestCities]
print(PostalBigCities)