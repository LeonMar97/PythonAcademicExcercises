import re
#Ronen Heifetz  :316481423
#Leon Markovich :318375060
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def findPostalCodes():
    csvFileName ="us_postal_codes.csv"
    citiesFileName="2019_largest_cities.txt"
    cityFile=open(citiesFileName)
    csvFile=open(csvFileName)
    csvList=csvFile.read()
    biggestCities = cityFile.read()
    matchBiggestCities = re.findall(r"([A-Z].*[a-z])([A-Z].*?)\t", biggestCities)
    matchCsv = re.findall(r"(.*?),(.*?),(.*?),", csvList)

    for tupCities in matchBiggestCities:
        for tupCsv in matchCsv:
            if tupCsv[1] + tupCsv[2] == tupCities[0] + tupCities[1]:
                print(tupCsv[0] + ' ' + tupCsv[1] + ' ' + tupCsv[2])
                break
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def atomlogs():
    file=open("atoms2.log")
    listOfLogs=file.read()
    a= re.findall(r"([0-9]+).*?([a-z][a-z\.]+) [0-9\.]+ CPU SECONDS.\n",listOfLogs)
    for i in a:
        print(i[0]+' '+i[1])

#to run the function uncomment
#findPostalCodes()
#atomlogs()