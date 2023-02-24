
#############################################################################################################################
#   filename:pyPotter.py                                                       
#   created: 2023-02-24                                                              
#   import your librarys below                                                    
#############################################################################################################################


import requests
import random
import warnings
from requests.packages.urllib3.exceptions import InsecureRequestWarning

warnings.filterwarnings("ignore", category=InsecureRequestWarning)
urlcharacter = "https://hp-api.onrender.com/api/characters"
urlspeel = "https://hp-api.onrender.com/api/spells"
#characters
url = requests.get(urlcharacter).json()

class Pypotter:
    def __init__(self):
        self.characters = requests.get(urlcharacter).json()

    def get_all_wizard(self):
        student_wizards = []
        for c in range(len(url)):
            if url[c]['wizard'] == True and url[c]['hogwartsStudent'] == True:
                student_wizard = {
                "name": url[c]['name'] if url[c]['name'] else "No information",
                "specie": url[c]['species'].capitalize() if url[c]['species'] else "No information",
                "gender": url[c]['gender'].capitalize() if url[c]['gender'] else "No information",
                "house": url[c]['house'].capitalize() if url[c]['house'] else "No information",
                "wand_wood": url[c]['wand']['wood'].capitalize() if url[c]['wand']['wood'] else "No information",
                "wand_core": url[c]['wand']['core'].capitalize() if url[c]['wand']['core'] else "No information",
                "patronus": url[c]['patronus'].capitalize() if url[c]['patronus'] else "No information",
                "yearOfBirth": url[c]['yearOfBirth'] if url[c]['yearOfBirth'] else "No information",
                'ancestry':  url[c]['ancestry'].capitalize() if url[c]['ancestry'] else "No information",
                'image': url[c]['image'] if url[c]['image'] else "No information"
            }
                student_wizards.append(student_wizard) 
            
        return student_wizards

    def get_all_wizard_only_names(self):
        student_wizards_names = []
        for c in range(len(url)):
            if url[c]['wizard'] == True and url[c]['hogwartsStudent'] == True:
                student_wizards_names.append(url[c]['name']) 
                
        return student_wizards_names

    def get_student_wizard_one_random_names(self):
        student_wizards_one = []
        for c in range(len(url)):
            if url[c]['wizard'] == True and url[c]['hogwartsStudent'] == True:
                student_wizards_one.append(url[c]['name']) 
                
        return student_wizards_one[random.randint(0, len(student_wizards_one)-1)]

    def get_student_wizard_random_information(self):
        student_wizards_information = []
        for c in range(len(url)):
            if url[c]['wizard'] == True and url[c]['hogwartsStudent'] == True:
                student_wizard = {
                "name": url[c]['name'] if url[c]['name'] else "No information",
                "specie": url[c]['species'].capitalize() if url[c]['species'] else "No information",
                "gender": url[c]['gender'].capitalize() if url[c]['gender'] else "No information",
                "house": url[c]['house'].capitalize() if url[c]['house'] else "No information",
                "wand_wood": url[c]['wand']['wood'].capitalize() if url[c]['wand']['wood'] else "No information",
                "wand_core": url[c]['wand']['core'].capitalize() if url[c]['wand']['core'] else "No information",
                "patronus": url[c]['patronus'].capitalize() if url[c]['patronus'] else "No information",
                "yearOfBirth": url[c]['yearOfBirth'] if url[c]['yearOfBirth'] else "No information",
                'ancestry':  url[c]['ancestry'].capitalize() if url[c]['ancestry'] else "No information",
                'image': url[c]['image'] if url[c]['image'] else "No information"
            }
                student_wizards_information.append(student_wizard) 
        return student_wizards_information[random.randint(0, len(student_wizards_information)-1)]

    def get_all_wizard_hogwartsStudent(self):
        student_wizards_horgawrts = []
        for c in range(len(url)):
            wizards = {
                "name": url[c]['name'] if url[c]['name'] else "No information",
                "specie": url[c]['species'].capitalize() if url[c]['species'] else "No information",
                "gender": url[c]['gender'].capitalize() if url[c]['gender'] else "No information",
                "house": url[c]['house'].capitalize() if url[c]['house'] else "No information",
                "wand_wood": url[c]['wand']['wood'].capitalize() if url[c]['wand']['wood'] else "No information",
                "wand_core": url[c]['wand']['core'].capitalize() if url[c]['wand']['core'] else "No information",
                "patronus": url[c]['patronus'].capitalize() if url[c]['patronus'] else "No information",
                "yearOfBirth": url[c]['yearOfBirth'] if url[c]['yearOfBirth'] else "No information",
                'ancestry':  url[c]['ancestry'].capitalize() if url[c]['ancestry'] else "No information",
                'image': url[c]['image'] if url[c]['image'] else "No information"
            }
            student_wizards_horgawrts.append(wizards)
        return student_wizards_horgawrts

    def get_all_names_wizard_hogwartsStudents(self):
        student_all_names_wizards_horgawrts = []
        for c in range(len(url)):
            student_all_names_wizards_horgawrts.append(url[c]['name'])
        return student_all_names_wizards_horgawrts

    def get_one_name_wizard_hogwartsStudents(self):
        student_all_names_wizards_horgawrts = []
        for c in range(len(url)):
            student_all_names_wizards_horgawrts.append(url[c]['name'])
        return student_all_names_wizards_horgawrts[random.randint(0,len(student_all_names_wizards_horgawrts)-1)]

    def get_oneRandom_wizard_hogwartsStudent(self):
        student_wizards_horgawrts = []
        for c in range(len(url)):
            wizards = {
                "name": url[c]['name'] if url[c]['name'] else "No information",
                "specie": url[c]['species'].capitalize() if url[c]['species'] else "No information",
                "gender": url[c]['gender'].capitalize() if url[c]['gender'] else "No information",
                "house": url[c]['house'].capitalize() if url[c]['house'] else "No information",
                "wand_wood": url[c]['wand']['wood'].capitalize() if url[c]['wand']['wood'] else "No information",
                "wand_core": url[c]['wand']['core'].capitalize() if url[c]['wand']['core'] else "No information",
                "patronus": url[c]['patronus'].capitalize() if url[c]['patronus'] else "No information",
                "yearOfBirth": url[c]['yearOfBirth'] if url[c]['yearOfBirth'] else "No information",
                'ancestry':  url[c]['ancestry'].capitalize() if url[c]['ancestry'] else "No information",
                'image': url[c]['image'] if url[c]['image'] else "No information"
            }
            student_wizards_horgawrts.append(wizards)
        return student_wizards_horgawrts[random.randint(0,len(student_wizards_horgawrts)-1)]


    def get_all_wizard_not_hogwartsStudents(self):
        all_wizard_not_hogwartsStudents = []
        for c in range(len(url)):
            if url[c]['wizard'] == True and url[c]['hogwartsStudent'] == False:
                wizards = {
                "name": url[c]['name'] if url[c]['name'] else "No information",
                "specie": url[c]['species'].capitalize() if url[c]['species'] else "No information",
                "gender": url[c]['gender'].capitalize() if url[c]['gender'] else "No information",
                "house": url[c]['house'].capitalize() if url[c]['house'] else "No information",
                "wand_wood": url[c]['wand']['wood'].capitalize() if url[c]['wand']['wood'] else "No information",
                "wand_core": url[c]['wand']['core'].capitalize() if url[c]['wand']['core'] else "No information",
                "patronus": url[c]['patronus'].capitalize() if url[c]['patronus'] else "No information",
                "yearOfBirth": url[c]['yearOfBirth'] if url[c]['yearOfBirth'] else "No information",
                'ancestry':  url[c]['ancestry'].capitalize() if url[c]['ancestry'] else "No information",
                'image': url[c]['image'] if url[c]['image'] else "No information"
            }
                all_wizard_not_hogwartsStudents.append(wizards)
        return all_wizard_not_hogwartsStudents

    def get_one_wizard_not_hogwartsStudents(self):
        one_wizard_not_hogwartsStudents = []
        for c in range(len(url)):
            if url[c]['wizard'] == True and url[c]['hogwartsStudent'] == False:
                wizards = {
                "name": url[c]['name'] if url[c]['name'] else "No information",
                "specie": url[c]['species'].capitalize() if url[c]['species'] else "No information",
                "gender": url[c]['gender'].capitalize() if url[c]['gender'] else "No information",
                "house": url[c]['house'].capitalize() if url[c]['house'] else "No information",
                "wand_wood": url[c]['wand']['wood'].capitalize() if url[c]['wand']['wood'] else "No information",
                "wand_core": url[c]['wand']['core'].capitalize() if url[c]['wand']['core'] else "No information",
                "patronus": url[c]['patronus'].capitalize() if url[c]['patronus'] else "No information",
                "yearOfBirth": url[c]['yearOfBirth'] if url[c]['yearOfBirth'] else "No information",
                'ancestry':  url[c]['ancestry'].capitalize() if url[c]['ancestry'] else "No information",
                'image': url[c]['image'] if url[c]['image'] else "No information"
            }
                one_wizard_not_hogwartsStudents.append(wizards)
        return one_wizard_not_hogwartsStudents[random.randint(0,len(one_wizard_not_hogwartsStudents)-1)]


    def get_onlyNames_wizard_not_hogwartsStudents(self):
        names_wizard_not_hogwartsStudents = []
        for c in range(len(url)):
            if url[c]['wizard'] == True and url[c]['hogwartsStudent'] == False:
                names_wizard_not_hogwartsStudents.append(url[c]['name'])
        return names_wizard_not_hogwartsStudents

    def get_oneName_wizard_not_hogwartsStudents(self):
        oneName_wizard_not_hogwartsStudents = []
        for c in range(len(url)):
            if url[c]['wizard'] == True and url[c]['hogwartsStudent'] == False:
                oneName_wizard_not_hogwartsStudents.append(url[c]['name'])
        return oneName_wizard_not_hogwartsStudents[random.randint(0,len(one_wizard_not_hogwartsStudents)-1)]

    def get_allMuggles(self):
        allMuggles = []
        for c in range(len(url)):
            if url[c]['species'] == 'human' and url[c]['wizard'] == False:
                ordinary_people = {
                    "name": url[c]['name'],
                    "specie": url[c]['species'].capitalize(),
                    "gender": url[c]['gender'].capitalize()            
                }
                allMuggles.append(ordinary_people)
        return allMuggles

    def get_allNamesMuggles(self):
        allMuggles = []
        for c in range(len(url)):
            if url[c]['species'] == 'human' and url[c]['wizard'] == False:
                allMuggles.append(url[c]['name'])
        return allMuggles

    def get_RandomNameMuggles(self):
        allMuggles = []
        for c in range(len(url)):
            if url[c]['species'] == 'human' and url[c]['wizard'] == False:
                ordinary_people = {
                    "name": url[c]['name'],
                    "specie": url[c]['species'].capitalize(),
                    "gender": url[c]['gender'].capitalize()            
                }
                allMuggles.append(ordinary_people)
        return allMuggles[random.randint(0,len(allMuggles)-1)]

    def get_OnlyRandomNameMuggles(self):
        allMuggles = []
        for c in range(len(url)):
            if url[c]['species'] == 'human' and url[c]['wizard'] == False:
                allMuggles.append(url[c]['name'])
        return allMuggles[random.randint(0,len(allMuggles)-1)]




    def getAllGryffindor(self):
        names = []
        for c in range(len(url)):
            if url[c]['house'] == 'Gryffindor':
                names.append(url[c]['name'])
        return names

    def getOneNameGryffindor(self):
        names = []
        for c in range(len(url)):
            if url[c]['house'] == 'Gryffindor':
                names.append(url[c]['name'])
        return names[random.randint(0,len(names)-1)]

    def getAllHufflepuff(self):
        names = []
        for c in range(len(url)):
            if url[c]['house'] == 'Hufflepuff':
                names.append(url[c]['name'])
        return names

    def getOneNameHufflepuff(self):
        names = []
        for c in range(len(url)):
            if url[c]['house'] == 'Hufflepuff':
                names.append(url[c]['name'])
        return names[random.randint(0,len(names)-1)]

    def getAllRavenclaw(self):
        names = []
        for c in range(len(url)):
            if url[c]['house'] == 'Ravenclaw':
                names.append(url[c]['name'])
        return names

    def getOneNameRavenclaw(self):
        names = []
        for c in range(len(url)):
            if url[c]['house'] == 'Ravenclaw':
                names.append(url[c]['name'])
        return names[random.randint(0,len(names)-1)]

    def getAllSlytherin(self):
        names = []
        for c in range(len(url)):
            if url[c]['house'] == 'Slytherin':
                names.append(url[c]['name'])
        return names

    def getOneNameSlytherin(self):
        names = []
        for c in range(len(url)):
            if url[c]['house'] == 'Slytherin':
                names.append(url[c]['name'])
        return names[random.randint(0,len(names)-1)]
    


