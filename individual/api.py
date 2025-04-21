#!/usr/bin/env python3
'''
    flask_sample.py
    Jacky Guzman, 21 April 2025 
    I have copied and modified Jeff Ondich's code from his file
    flask_sample.py on GitHub. (We received permission from him
    to do so for an assignment.)
'''
import sys
import argparse
import flask
import json
import csv

app = flask.Flask(__name__)

# Who needs a database when you can just hard-code some actors and movies?


@app.route('/')
def hello():
    return 'Hello! How are you? Ask and you shall receive...if you need help in knowing how to obtain information about animals, please go to the help page by going to the top of the browser and in the place where the http address of the website appears, simply add at the end "/help". Good luck!'

@app.route('/animals/<diet>')
def get_animals_with_diet(diet):
    '''Returns a list of all the animals that have that specific diet.'''
    with open('../data/animals_info.csv') as f:
        reader = list(csv.reader(f, delimiter=',')) 
        animal_list = []
        for animal_row in reader:
            if diet in animal_row[19]:
                animal_name = animal_row[0]
                animal_list.append(animal_name)
    return json.dumps(animal_list)

@app.route('/help')
def get_help():
    return 'Glad you asked for help! In order to find out what animals have certain diets, at the top of the page where the http link of the website appears, simply type "/animals/<diet>" where <diet> is the animal diet you are curious about. You should receive a page that is full of all the animals who have that specific diet.' 

if __name__ == '__main__':
    parser = argparse.ArgumentParser('A sample Flask application/API')
    parser.add_argument('host', help='the host on which this application is running')
    parser.add_argument('port', type=int, help='the port on which this application is listening')
    arguments = parser.parse_args()
    app.run(host=arguments.host, port=arguments.port, debug=True)
