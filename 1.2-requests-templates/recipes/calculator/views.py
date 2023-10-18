from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}
0
# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

def recipe(request, dish):
    recipe = DATA.get(dish)
    servings = int(request.GET.get('servings', default=1))

    recipe_mod = {}
    for ingredient, quantity in recipe.items():
        quantity_mod = servings * float(quantity)
        if quantity_mod == int(quantity_mod):
            quantity_mod = int(quantity_mod)
        else:
            quantity_mod = round(quantity_mod, 2)

        recipe_mod[ingredient] = quantity_mod

    context = {
        'recipe': recipe_mod
    }

    return render(request, 'calculator/index.html', context)