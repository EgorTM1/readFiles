dictOfRecipes = {}

def ReadFile(file):
    with open (file, 'r', encoding='utf-8') as file_recipes:

        for i in file_recipes:
            dish = file_recipes.readline().strip()

            count_ingredients = int(file_recipes.readline().strip())
            for j in range(int(count_ingredients)):
                ingredient = file_recipes.readline().strip().split(' | ')
            
                if dish in dictOfRecipes:
                    dictOfRecipes[dish].append({'ingredient_name': ingredient[0], 'quantity': ingredient[1], 'measure': ingredient[2]})
                else:
                    dictOfRecipes[dish] = [{'ingredient_name': ingredient[0], 'quantity': ingredient[1], 'measure': ingredient[2]}]
                    
def get_shop_list_by_dishes(dishes, person_count):
    for dish in dishes:
        if dish in dictOfRecipes:
            for i in dictOfRecipes[dish]:
                print(f'{i["ingredient_name"]} - {int(i["quantity"])*person_count} {i["measure"]}')


ReadFile('Recipes.txt')

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)