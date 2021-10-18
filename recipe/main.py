from recipe import Recipe


def create_recipe(name, chocolate=0, coffee=0, milk=0, sugar=0, price=0.0):
    recipe = Recipe(name)
    recipe.chocolate = chocolate
    recipe.coffee = coffee
    recipe.milk = milk
    recipe.sugar = sugar
    recipe.price = price
    print(recipe)
    return recipe


if __name__ == '__main__':
    recipe1 = create_recipe("Coffee with sugar", chocolate=4, sugar=2, milk=0, price=30.0)
    recipe2 = create_recipe("Latte", coffee=3, sugar=2, milk=1, price=40.0)
    recipe3 = create_recipe("Hot Chocolate", coffee=0, chocolate=3, sugar=2, milk=4, price=30.0)
