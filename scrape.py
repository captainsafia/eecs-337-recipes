import requests
from bs4 import BeautifulSoup
import sys

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def parse_ingredient(ingredient):

    text = ingredient.getText()

    ingredient_parts = []

    if ('(' in text) and (')' in text):
        temp_split = text.split('(')
        ingredient_parts.append(temp_split[0])
        temp_split = temp_split[1].split(')')
        ingredient_parts.append(temp_split[0])
        ingredient_parts = ingredient_parts + temp_split[1].split(' ')
    else:
        ingredient_parts = text.split(' ')



    categories = ["quantity", "measurement", "descriptor","food", "technique"]
    cleand_ingredients = {}
    for c in categories:
         cleand_ingredients[c] = []

    number_categories = min(len(ingredient_parts), len(categories))
    start = 0
    # if not(is_number(ingredient_parts[0])):
    #     start += 2
    for s in range(start, number_categories):
        cleand_ingredients[categories[s]] = ingredient_parts[s]

    return cleand_ingredients


if __name__ == "__main__":

    if len(sys.argv) != 1: print("usage: python scrape.py '<urlof.recipe>'")

    url = sys.argv[1]
    r = requests.get(url)

    soup = BeautifulSoup(r.text, "html.parser")
    ingredients = soup.findAll("span", {"class":"recipe-ingred_txt"})

    ingredients_json = {"ingredients":[]}
    for i in ingredients[:-3]:
        ingredients_json["ingredients"].append(parse_ingredient(i))

    print(ingredients_json)
