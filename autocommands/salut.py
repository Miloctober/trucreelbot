import csv
import random

inconnu = []
connu = []
places = []

def init():
    with open('./data/csv/inconnu.csv', mode ='r', encoding='utf-8')as file:
        file = csv.reader(file)
        for line in file:
            inconnu.append(line[0])
    with open('./data/csv/connu.csv', mode='r', encoding='utf-8') as file:
        file = csv.reader(file)
        for line in file:
            connu.append(line[0])
    with open('./data/csv/places.csv', mode='r', encoding='utf-8') as file:
        file = csv.reader(file)
        for line in file:
            places.append(line[0])

def sentence(slt):
    nb1 = random.randint(0, 2)
    nb3 = random.randint(0, len(places)-1)
    if nb1 == 0:
        nb2 = random.randint(0, len(connu)-1)
        return f"{slt}, c'est {connu[nb2]} {places[nb3]}!"
    else:
        nb2 = random.randint(0, len(inconnu)-1) 
        return f"{slt}, c'est {inconnu[nb2]} {places[nb3]}!"
