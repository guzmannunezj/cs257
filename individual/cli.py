'''
    cli.py
    Jacky Gu zman
    18 April 2025

    NAME: cli.py - command-line interface exercise
    SYNOPSIS: python3 cli.py animaldiet
    DESCRIPTION: Shows a list of all the animals that have a specific
    diet.

'''

import argparse
import csv

def get_parsed_arguments():
    parser = argparse.ArgumentParser(description='Give the names of all the animals that have a certain diet.')
    parser.add_argument('diet', help='One or more animal diets you want to use to filter animals out with. For example, if you want to find out all the animals that are carnivores, type Carnivore.')
    parsed_arguments = parser.parse_args()
    return parsed_arguments

def main():
    arguments = get_parsed_arguments()
    with open('/mnt/c/Users/jacqu/sdlabs/cs257/data/animals_info.csv') as f:
        reader = list(csv.reader(f, delimiter=',')) 
        animal_list = []
        for d in arguments.diet: 
            for animal_row in reader:
                if d in animal_row:
                    animal_name = animal_row[0]
                    animal_list.append(animal_name)
    if len(animal_list) == 0:
        print(f'Could not find any animal with that diet. Sorry. It could be that the diet is either super rare or there is a typo. Please check that you spelled the diet correctly.')
    else: 
        for i in range(len(animal_list)):
            print(animal_list[i])

if __name__ == '__main__':
    main()


