from transforms import *


args = sys.argv[1:]

if len(args == 2):

    if args[0] == "-healthy":
        print(healthy_transform.healthy_trans(args[1]))
        exit()
    elif args[0] == "-vegan":
        exit()
    elif args[0] == "-thai":
    	print(thai_transform.run(args[1]))
        exit()

else:
    print("usage: python healthy_transform.py <recipe_path>")
    exit()
