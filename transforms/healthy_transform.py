import sys
import json
from pprint import pprint


to_healthy_dict = {"breadcrumbs":"ground flaxseeds"}

from_healthy_dict = dict((v,k) for k,v in to_healthy_dict.items())


def to_healthy(recipe):
    pass


def from_healthy(recipe):
    pass


def healthy_trans(recipe_path, to=True):


    with open(recipe_path) as rf:
        recipe = json.load(rf)

    # pprint(recipe)

    transformed = None
    if not(to):
        transformed = from_healthy(recipe)
    else:
        transformed = to_healthy(recipe)

    return transformed


if __name__ == '__main__':

    args = sys.argv[1:]


    if len(args) == 1:
        print(healthy_trans(args[0]))
        exit()

    if len(args) == 2:
        if args[1] == "-from":
            print("not yet ;)")
            exit()


    print("usage: python healthy_transform.py <recipe_path>")
