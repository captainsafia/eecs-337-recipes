import json
import os
from pprint import pprint

#Used to check whether recipe is already thai or not
thai_essentials = [
    'curry',
    'coconut milk',
    'fish sauce',
    'chili pepper'
]

#Used to check whether to add fish sauce and coconut milk or not to recipe
pasta = [
    'pasta',
    'capellini',
    'spaghetti',
    'ziti',
    'fettuccine',
    'lasagne',
    'linguine',
    'cavatappi',
    'ditalini',
    'macaroni',
    'penne',
    'rigatoni',
    'bowtie',
    'rotini',
    'rice',
    'stock',   
]

#Used to determine where to add in the step to add thai ingredients
cooking = [
    'stir',
    'mix',
    'blend'
]

def print_recipe(recipe):
    print(recipe['name'])
    print('Ingredients')
    for ingredient in recipe['ingredients']:
        print('- ', ingredient.get('quantity', ''), ' ',
                ingredient.get('unit', ''), ' ',
                ingredient.get('name', ''), ' ',
                ingredient.get('preparation', ''),
                sep='')
    print('Recipe')
    for index, step in enumerate(recipe['steps']):
        print(index + 1, '. ', step.get('raw', ''), sep='')
    print('\n\n')


def is_thai(recipe):
    thai = False
    for ingredient in recipe['ingredients']:
        if contains_substring(ingredient['name'], thai_essentials):
            return True
    return thai

#If element of elements is in value
def contains_substring(value, elements):
    for element in elements:
        if element in value:
            return True
    return False


def thaify(recipe):
    ingredients = recipe['ingredients']
    isentree = False
    #If the recipe is an entree (pasta, rice, soup, the likes), then add coconut milk and fish sauce
    for ingredient in ingredients:
        if contains_substring(ingredient['name'], pasta):
            isentree = True
    if 'soup' in recipe['name']:
        isentree = True

    if isentree == True:
        ingredients.append({"quantity":"2", "unit":"tablespoon", "preparation":"", "name":"fish sauce"})
        ingredients.append({"quantity":"5", "unit":"tablespoon", "preparation":"", "name":"coconut milk"}) 

    #Makeing it hot (for all recipes)
    ingredients.append({"quantity":"1/4", "unit":"cups", "preparation":"diced", "name":"thai pepper"})
   
    lemongrass = False
    basil = False

    #Thai garnishes
    #If ingredient is already in the recipe, then don't add
    for ingredient in ingredients:
        if 'lemongrass' in ingredient['name']:
            lemongrass = True
        elif 'basil' in ingredient['name']:
            basil = True

    if lemongrass == False:
        ingredients.append({"quantity":"", "unit":"", "preparation":"chopped", "name":"lemongrass"})
    if basil == False:
        ingredients.append({"quantity":"", "unit":"", "preparation":"chopped", "name":"basil"})   

    steps = recipe['steps']
    done = False
    for step in steps:
        #If step involves stirring, blending, or mixing, then add in thai ingredients
        if contains_substring(step['raw'], cooking) and done == False:
            if isentree == True:
                step['ingredients'].append({"quantity":"2", "unit":"tablespoon", "preparation":"", "name":"fish sauce"})
                step['ingredients'].append({"quantity":"5", "unit":"tablespoon", "preparation":"", "name":"coconut milk"})
                step['raw'] += ' Mix in fish sauce, coconut milk, and thai peppers.'
                done = True
            else:
                step['raw'] += ' Mix in thai peppers.'
                done = True
            step['ingredients'].append({"quantity":"1/4", "unit":"cups", "preparation":"diced", "name":"thai pepper"})

    if lemongrass == False and basil == False:
        steps.append({"method":["garnish"],"tools":[],"ingredients":[{"quantity":"", "unit":"", "preparation":"chopped", "name":"lemongrass"}, 
            {"quantity":"", "unit":"", "preparation":"chopped", "name":"basil"}],"raw":"Garnish with lemongrass and basil."})
    elif lemongrass == False and basil == True:
        steps.append({"method":["garnish"],"tools":[],"ingredients":[{"quantity":"", "unit":"", "preparation":"chopped", "name":"lemongrass"}],
            "raw":"Garnish with lemongrass."})
    elif lemongrass == Truee and basil == False:
        steps.append({"method":["garnish"],"tools":[],"ingredients":[{"quantity":"", "unit":"", "preparation":"chopped", "name":"basil"}],
            "raw":"Garnish with basil."})

    recipe['ingredients'] = ingredients
    recipe['steps'] = steps
    return recipe

def run(path):
    with open(path) as recipe:
        curr = json.load(recipe)
    if not is_thai(curr):
        print_recipe(thaify(curr))
    else:
        print('Recipe is already Thai!')     

if __name__ == '__main__':
    recipes = [
        './recipes/mac-cheese-casserole.json',
        './recipes/mac-cheese.json',
        './recipes/sugar-cookies.json'
    ]
    directory = os.path.dirname(os.path.realpath('__file__'))
    for recipe in recipes:
        filename = os.path.join(directory, recipe)
        with open(filename) as recipe_file:
            curr = json.load(recipe_file)
            if not is_thai(curr):
                transformed = thaify(curr)
                print_recipe(transformed)
            else:
                print('Recipe is already Thai!')