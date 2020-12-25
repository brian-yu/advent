from collections import defaultdict
import re

file = open('input.txt')
lines = [line.rstrip('\n') for line in file.readlines()]

def parse_ingredients_and_allergens(lines):
    result = []

    for line in lines:
        match = re.match(r'([a-z ]+) \(contains ([a-z]+(, [a-z]+)*)\)', line)
        if not match:
            raise Exception('invalid line')
        ingredients = match.group(1).split(" ")
        allergens = match.group(2).split(", ")
        result.append((ingredients, allergens))
    
    return result

def get_allergen_possibilities(ingredients_and_allergens):
    allergen_possibilities = {}

    for ingredients, allergens in ingredients_and_allergens:
        for allergen in allergens:
            if allergen not in allergen_possibilities:
                allergen_possibilities[allergen] = set(ingredients)
            else:
                allergen_possibilities[allergen] &= set(ingredients)
    
    return allergen_possibilities

ingredients_and_allergens = parse_ingredients_and_allergens(lines)
allergen_possibilities = get_allergen_possibilities(ingredients_and_allergens)

def count_inert_ingredients(allergen_possibilities, ingredients_and_allergens):
    allergen_ingredients = set()
    for ingredients in allergen_possibilities.values():
        allergen_ingredients |= ingredients

    count = 0
    for ingredients, _ in ingredients_and_allergens:
        for ingredient in ingredients:
            if ingredient not in allergen_ingredients:
                count += 1
    return count

print(count_inert_ingredients(allergen_possibilities, ingredients_and_allergens))

def prune_allergen_possibilities(allergen_possibilities):
    pruned = set()

    def helper():
        to_prune = []
        for allergen, possible_ingredients in allergen_possibilities.items():
            if len(possible_ingredients) == 1 and allergen not in pruned:
                to_prune.append((allergen, list(possible_ingredients)[0]))
                pruned.add(allergen)

        for allergen_to_prune, ingredient in to_prune:
            for allergen in allergen_possibilities:
                if allergen != allergen_to_prune:
                    allergen_possibilities[allergen] -= {ingredient}
        
        return len(to_prune) > 0

    while helper():
        pass
    
    return {allergen: list(ingredients)[0] for allergen, ingredients in allergen_possibilities.items()}

allergen_ingredients = prune_allergen_possibilities(allergen_possibilities)

print(",".join(ingredient for _, ingredient in sorted(allergen_ingredients.items())))