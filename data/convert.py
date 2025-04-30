'''Authors: Anthony , Jacky , Bwalya 
    Date: 2023-10-01'
    Description: l read your dataset's file and write one CSV file for each of the tables in your database design. 
    If you have designed a table named animals, for example, the corresponding CSV file should be named animals.csv,
    and should have the same columns as the table. '''


import csv
import sys

def main(input_filename):
    animals = [] # List to store animal data
    AnimalDict= {} # Dictionary to store unique animals (still testing something with table linking)
    PlacesDict={}
    CountriesDict={}
    populationTrendDict={}
    populationStatusDict={}

    LinkTable=[]

    with open(input_filename) as f:
        reader = csv.reader(f)
       # next(reader)  # Skip the header row
        for csv_row in reader:
            
            AnimalName = csv_row[0]  # Animal name
            Species = csv_row[1] 
            LifeSpan = csv_row[2] 
            continents = csv_row[3] #( could chnage later be a continent or country,  Note :17 in animal_info.csv)  
            countries=csv_row[4]
            PopulationTrend = csv_row[5]
            PopulationStatus = csv_row[6]


            name_key = f'{AnimalName}+{Species}+{LifeSpan}' 

           
            if name_key not in AnimalDict: 
                animal_id = len(animals) +1    
                AnimalDict[name_key] = animal_id

            animals.append((animal_id, AnimalName, Species, LifeSpan, continents,  countries, PopulationTrend, PopulationStatus)) # Append animal data to the list
            
            
            if continents not in PlacesDict: # Check if the continent is unique
                place_id = len(PlacesDict) + 1 # Unique ID for the continent
                PlacesDict[continents] = place_id # Add continent to the dictionary

            if countries not in CountriesDict:
                country_id = len(CountriesDict) + 1
                CountriesDict[countries] = country_id

            if PopulationTrend not in populationTrendDict:
                population_id = len(populationTrendDict) + 1
                populationTrendDict[PopulationTrend] = population_id

            if PopulationStatus not in populationStatusDict:
                population_id = len(populationStatusDict) + 1
                populationStatusDict[PopulationStatus] = population_id

            LinkTable.append((AnimalDict[name_key], PlacesDict[continents], CountriesDict[countries], populationTrendDict[PopulationTrend], populationStatusDict[PopulationStatus])) # Append the animal ID and place ID to the linking table

    

    with open('animals.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for animal in animals:
            writer.writerow([animal[0], animal[1], animal[2], animal[3]])  

    # Write continents/Place table
    with open('Continents.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for place, place_id in PlacesDict.items():
            writer.writerow([place_id, place])
            
    with open ('countries.csv', 'w') as f:
        writer = csv.writer(f)
        for country, country_id in CountriesDict.items():
            writer.writerow([country_id, country])
        
    with open ('populationtTrend.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for trend, trend_id in populationTrendDict.items():
            writer.writerow([trend_id, trend])

    with open ('populationStatus.csv', 'w') as f:
        writer = csv.writer(f)
        for status, status_id in populationStatusDict.items():
            writer.writerow([status_id, status])
            
    # with open ('continents_countries.csv', 'w') as f:
    #     writer = csv.writer(f)
    #     writer.writerow(['CountryID', 'Continents'])
    #     for link in LinkTable:
    #         writer.writerow([link[2], link[1]])
    
    with open('animals_continents.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for link in LinkTable:
            writer.writerow([link[0], link[1]])

    with open ('animals_countries.csv', 'w') as f: 
        writer = csv.writer(f)
        for link in LinkTable:
            writer.writerow([link[0], link[2]])       

    with open ('animals_concern.csv', 'w') as f:
        writer = csv.writer(f)
        for link in LinkTable:
            writer.writerow([link[0], link[3], link[4]]) 

if len(sys.argv) != 2:
    print(f'Usage: {sys.argv[0]} original_csv_file', file=sys.stderr)
    exit()

main(sys.argv[1])