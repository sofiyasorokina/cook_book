cook_book = {}
file = open("recept.txt", "r")
for i in file:
    name = i.strip( )
    kollvo = file.readline().strip()
    cook_book[name] = []
    for j in range(int(kollvo)):
        ingredient = file.readline().strip().split(" | ")
        cook_book[name].append({"ingredient_name": ingredient[0], "quantity": ingredient[1], "measure": ingredient[2]})
    file.readline()
# print(cook_book, "\n")

def get_shop_list_by_dishes(dishes, person_count):
    ingredients = {}
    for i in dishes:
        for j in cook_book[i]:
            if j["ingredient_name"] in ingredients:
                ingredients [j["ingredient_name"]]["quantity"] += int(j["quantity"])*person_count
            else:
                ingredients [j["ingredient_name"]] = {"measure": j["measure"], "quantity": int(j["quantity"])*person_count}
    print(ingredients)
get_shop_list_by_dishes(["Омлет", "Утка по-пекински"], 2)
