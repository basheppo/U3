import csv
listOfCountries = ["Brazil","Germany","India","Russia","Us"]
def readData (listOfCountries) : 
    confirmed = 0
    recovered=0
    deaths=0
    for country in listOfCountries:
        print("_________________"+country+"_________________")
        with open (country+".csv","r") as file:
            reader = csv.DictReader(file)
            for line in reader :
                print(line)
                confirmed += int(line["confirmed"])
                recovered += int(line["recovered"])
                deaths += int(line["deaths"])

        return confirmed,recovered,deaths


numOfConfirmed, numOfRecovered, numOfDeaths = readData(listOfCountries)
print("Total Confirmed:", numOfConfirmed)
print("Total Recovered:", numOfRecovered)
print("Total Deaths:", numOfDeaths)




