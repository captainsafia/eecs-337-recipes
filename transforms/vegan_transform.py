import json
import os
from pprint import pprint

vegan_substitutes = {
    'butter': 'applesauce',
    'beef': 'seitan',
    'steak': 'portabello mushrooms',
    'liver': 'tofu',
    'pork': 'tempeh',
    'ham': 'tempeh',
    'ribs': 'tempeh',
    'bacon': 'veggie bacon',
    'sausage': 'tofu',
    'veal': 'seitan',
    'lamb': 'seitan',
    'chicken': 'eggplant',
    'carp': 'mashed chickpeas',
    'catfish': 'mashed chickpeas',
    'salmon': 'mashed chickpeas',
    'tilapia': 'mashed chickpeas',
    'trout': 'mashed chickpeas',
    'crayfish': 'mashed chickpeas',
    'lobster': 'mashed chickpeas',
    'shrimp': 'mashed chickpeas', 
    'prawns': 'mashed chickpeas', 
    'oyster': 'mashed chickpeas', 
    'mussel': 'mashed chickpeas', 
    'snail': 'beansi',
    'turkey': 'eggplant',
    'sheep': 'tempeh',
    'quail': 'eggplant',
    'rabbit': 'beans',
    'pheasant': 'eggplant',
    'goose': 'eggplant',
    'egg': 'chia seed mixture',
    'milk': 'almond milk',
    'cheese': 'vegan cheese'
}

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

def contains_substring(value, elements):
    for element in elements:
        if element in value:
            return element
    return ''

def is_vegan(recipe):
    not_vegan = vegan_substitutes.keys()
    for ingredient in recipe['ingredients']:
        if contains_substring(ingredient['name'], not_vegan):
            return False
    return True

def from_vegan(recipe):
    pass

def to_vegan(recipe):
    ingredients = recipe['ingredients']
    not_vegan = vegan_substitutes.keys()
    for ingredient in ingredients:
        element = contains_substring(ingredient['name'], not_vegan)
        if element != '':
            ingredient['name'] = vegan_substitutes[element]

    steps = recipe['steps']
    for step in steps:
        for phrase in step['raw']:
            if phrase in not_vegan:
                step['raw'] = step['raw'].replace(phrase, vegan_substitutes[phrase])

    recipe['ingredients'] = ingredients
    recipe['steps'] = steps
    return recipe

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
            data = json.load(recipe_file)
            if not is_vegan(data):
                transformed = to_vegan(data)
            else:
                transformed = from_vegan(data)
            print_recipe(transformed)
