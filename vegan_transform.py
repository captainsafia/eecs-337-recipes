vegan_substitutes = {
    'buttermilk',
    'cottage',
    'cream',
    'creamer',
    'creamy',
    'creme',
    'ghee',
    'half-and-half', 
    'milk',
    'yogurt'
}

def from_vegan(recipe):

def to_vegan(recipe):
    ingredients = recipe['ingredients']
    not_vegan = vegan_substitutes.keys()
    substitutes = vegan_substitutes.values()
    for ingredient in ingredients:
        if ingredient['name'] in not_vegan:
            ingredient['name'] = substitutes[ingredient['name']]
    recipe['ingredients'] = ingredients
