import re

class Ingredient:
    def __init__(self, name: str, capacity: int, durability: int, flavor: int, texture: int, calories: int):
        self.name = name
        self.capacity = capacity
        self.durability = durability
        self.flavor = flavor
        self.texture = texture
        self.calories = calories

    def __str__(self, *args, **kwargs):
        return '{}: capacity {}, durability {}, flavor {}, texture {}, calories {}'.format(self.name, self.capacity,
                                                                                           self.durability,
                                                                                           self.flavor, self.texture,
                                                                                           self.calories)


class Cookie:
    def __init__(self, capacity = 0, durability = 0, flavor = 0, texture = 0):
        self.capacity = capacity
        self.durability = durability
        self.flavor = flavor
        self.texture = texture

    def add_ingredient(self, ingredient: Ingredient, amount: int):
        self.capacity += ingredient.capacity * amount
        self.durability += ingredient.durability * amount
        self.flavor += ingredient.flavor * amount
        self.texture = ingredient.texture * amount

    def copy(self):
        return Cookie(self.capacity, self.durability, self.flavor, self.texture)

    @property
    def score(self):
        return self.capacity * self.durability * self.flavor * self.texture


def permute(remaining_space: int, remaining_ingredients: list, unfinished_cookie: Cookie, best_cookie: Cookie):
    if remaining_space <= 0 and len(remaining_ingredients) != 0:
        return
    if len(remaining_ingredients) == 0:
        if remaining_space > 0:
            return
        if unfinished_cookie.score > best_cookie.score:
            best_cookie = unfinished_cookie
            print(best_cookie.score)
        return
    for amount in range(remaining_space + 1):
        # copy stuff
        local_remaining_ingredients = remaining_ingredients.copy()
        local_unfinished_cookie = unfinished_cookie.copy()

        local_unfinished_cookie.add_ingredient(local_remaining_ingredients.pop(), amount)
        permute(remaining_space - amount, local_remaining_ingredients, local_unfinished_cookie, best_cookie)

ingredients = {}

regex = re.compile(r'(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)')

with open('../input/day15.txt') as f:
    for line in f:
        name, capacity, durability, flavor, texture, calories = regex.match(line).groups()
        ingredients[name] = Ingredient(name, int(capacity), int(durability), int(flavor), int(texture), int(calories))

for ingredient in ingredients.values():
    print(ingredient)

best_cookie = Cookie()

permute(100, list(ingredients.values()), Cookie(), best_cookie)

print(best_cookie.score)
