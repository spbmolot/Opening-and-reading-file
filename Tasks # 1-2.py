from pprint import pprint


def get_list_cook_book():
    with open('recipes.txt', 'rt', encoding='utf-8') as file:
        cook_book = {}
        for line in file:
            dish_name = line.strip()
            cont_ing = int(file.readline())
            ingredients = []
            for _ in range(cont_ing):
                ingredient_name, quantity, measure = file.readline().strip().split(' | ')
                ingredients.append({
                    'ingredient_name': ingredient_name,
                    'quantity': quantity,
                    'measure': measure
                })
            file.readline()
            cook_book[dish_name] = ingredients
    # pprint(cook_book, sort_dicts=False)
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    ingredients = {}
    q = 0
    for key, value in get_list_cook_book().items():
        if key in dishes:
            for ing in value:
                if ing["ingredient_name"] not in ingredients:
                    ingredients[ing["ingredient_name"]] = {"measure": ing["measure"], "quantity": int(ing["quantity"]) * person_count}
                else:
                    for key_, value_ in ingredients.items():
                        if key_ == ing["ingredient_name"]:
                            q = value_["quantity"]
                    ingredients[ing["ingredient_name"]] = {"measure": ing["measure"], "quantity": int(ing["quantity"]) * person_count + q}
    pprint(ingredients)


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)