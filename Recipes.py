# Recipes
# Author: Bao Pham
# Version 1.0
# Description:
# This program utilizes the python request library and json to interact with the Spoonacular
# API and give a list of viable recipes depending on what ingredients the user already has

import requests

# getMissingIngredients
#
# Takes in a string of ingredients the user already has and takes
# in an integer representing the number of recipes they want returned
#
# Prints to console a list of recipes including the missing ingredients and what aisle they can be found in
def getMissingIngredients(availableIngredients, amountRecipes):
    
    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/findByIngredients"

    # "number": number of recipes you want returned
    # "ranking": "Put (1) to maximize used ingredients. Put (2) to minimize missing ingredients"
    # "ignorePantry: boolean whether or not to ignore common pantry ingredients such as water, salt, and flour
    # "ingredient": string of ingredients the user already has separated by commas
    parameters = {"number": str(amountRecipes), "ranking": "1", "ignorePantry": "true", "ingredients": availableIngredients}

    headers = {
        'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
        'x-rapidapi-key': "ffd0e0f178msh121876bea14258ep136a54jsn9fc186fa91fc" # api key goes here
    }

    # API request call
    response = requests.request("GET", url, headers=headers, params=parameters)

    data = response.json()

    print # adding whitespace just to make result look cleaner
    print "{"

    for x in range(amountRecipes):
        print '        "' + data[x]["title"] + '":'
        print('                {')

        for item in data[x]['missedIngredients']:
            print '                        "' + (item['name']) + '": "' + (item['aisle']) + '"'
        print('                },')

    print "}"

def main():

    # I am using Python 2 but I think raw_input might not work if you are running Python 3
    ingredients = raw_input("Enter the ingredients you have (each separated by a space): ")
    amountRecipes = input("How many recipes do you want to see? ")
    while amountRecipes < 1:
        amountRecipes = input("Please enter 1 or higher: ")

    temp = ingredients.split() # separate the individual ingredients into a list

    # creating a string of ingredients separated by a comma
    ingredients = ""
    for item in temp:
        ingredients = ingredients + item
        ingredients = ingredients + ", "

    if len(ingredients) != 0:
        ingredients = ingredients[:-2] #remove the last space and comma

    getMissingIngredients(ingredients, amountRecipes)

if __name__== "__main__":
    main()