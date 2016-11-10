import csv
from PokemonClass import *
import sys

#Gustav Kjellberg och Isak Hassbring 2016-01-09

def start():
	searchedPokemon = str(input("Ange vilken Pokemon du söker efter: "))
	return searchedPokemon

def menue():

	bigPokeList = createList()
	searchedPokemon = start()
	choice = getPokemon(searchedPokemon, bigPokeList)

	while True:

		print("Klicka på det du vill göra" + "\n" + "1. Se om Pokemon är bra/dålig" + "\n" + "2. Se om Pokemon är rare" + "\n" + "3. Se vad Pokemon passar som" + "\n" + "4. Sök efter en pokemons samtliga stats " + "\n" "5. Avsluta")

		i = input(("Val: "))

		if i == "1":
			if choice.good(choice.Atk, choice.Def):
				print("Good")
			else:
				print("Bad")
		elif i == "2":
			if choice.ifRare(choice.Name):
				print("This Pokemon is rare!!!")
			else:
				print("This Pokemon is not rare...")
		elif i == "3":
			if choice.ifAttacker(choice.Atk, choice.Def):
				print("This Pokemon is ideal for attacking")
			else:
				print("This Pokemon is ideal for Defending")
		elif i == "4":
			print(choice)
		elif i == "5":
			sys.exit(0) 




def createList():
	with open('pokedex-lab-1.csv', encoding = "latin1") as pokeList:
		reader = csv.DictReader(pokeList)
		bigPokeList = []

		for everyObject in reader:

			objectTest = (Pokemon(everyObject['Pokemon'], int(everyObject['HP']), int(everyObject['Atk']), int(everyObject['Def']), everyObject['Mass']))
			bigPokeList.append(objectTest)

	return bigPokeList


def getPokemon(searchedPokemon, bigPokeList):

	for objekt in bigPokeList:

		if objekt.Name == searchedPokemon:
			return objekt

	return None






menue()

