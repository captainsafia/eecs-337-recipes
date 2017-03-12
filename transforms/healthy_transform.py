import sys
import json
from pprint import pprint


to_healthy_dict = {
                    "breadcrumbs":"ground flaxseeds",
                    "gluten-free flour":"wheat flour",
                    "quinoa":"couscous",
                    "zoodles":"pasta noodles",
                    "ground flaxseeds":"bread crumbs",
                    "spaghetti squash":"pasta",
                    "lettuce leaves":"tortilla wraps",
                    "corn tortilla":"flour tortilla",
                    "quinoa":"oatmeal",
                    "veggies":"pita",
                    "nuts":"croutons",
                    "unsweetened applesauce":"sugar",
                    "natural peanut butter":"peanut butter",
                    "seltzer water with citrus slice":"soda",
                    "Stevia":"sugar",
                    "cacao nibs":"chocolate chips",
                    "vanilla extract":"sugar",
                    "cinnamon":"cream and sugar",
                    "unsweetened iced tea":"juice",
                    "plain yogurt with fresh fruit":"flavored yogurt",
                    "fresh fruits":"canned fruit",
                    "red wine":"white wine",
                    "soda water":"juice",
                    "soda water":"tonic water",
                    "garlic powder":"salt",
                    "low-sodium soy sauce":"standard soy sauce",
                    "nut butter":"butter",
                    "whole grain pasta":"pasta",
                    "whole grain noodles":"noodles",
                    "whole grain bread":"bread"
                    }

from_healthy_dict = dict((v,k) for k,v in to_healthy_dict.items())


def replace_ingredient(old_ing, new_ing, old):

    start = old.find(old_ing)
    new = (old[:start] + new_ing + old[start + len(old_ing):])

    return new

def swap_string(ingredient, convert_dict):

    for key, val in convert_dict.items():
        if key in ingredient:
            ingredient = replace_ingredient(key, val, ingredient)

    return ingredient

def swap_ingredients(ingredients, convert_dict):

    for desc in ingredients:
        desc["name"] = swap_string(desc["name"], convert_dict)

def to_or_from_healthy(recipe, convert_dict):

    swap_ingredients(recipe["ingredients"], convert_dict)

    steps = recipe["steps"]
    for step in steps:
        swap_ingredients(step["ingredients"], convert_dict)

        # call different because of string
        step["raw"] = swap_string(step["raw"], convert_dict)

    return recipe


def healthy_trans(recipe_path, to=True):

    with open(recipe_path) as rf:
        recipe = json.load(rf)

    # pprint(recipe)

    transformed = None
    if not(to):
        transformed = to_or_from_healthy(recipe, to_healthy_dict)
    else:
        transformed = to_or_from_healthy(recipe, from_healthy_dict)

    return transformed


if __name__ == '__main__':

    args = sys.argv[1:]

    trans = None
    if len(args) == 1:
        trans = healthy_trans(args[0])
    elif len(args) == 2:
        if args[1] == "-from":
            print("not yet ;)")
    else:
        print("usage: python healthy_transform.py <recipe_path>")
        exit()
    pprint(trans)
