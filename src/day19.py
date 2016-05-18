import re
from collections import deque


def permute_replacements(tokens, replacements):
    distinct_molecules = set()
    for i in range(len(tokens)):
        if tokens[i] in replacements.keys():
            for replacement in replacements[tokens[i]]:
                new_molecule = tokens[:]
                new_molecule[i] = replacement
                distinct_molecules.add(''.join(new_molecule))
    return distinct_molecules

replacements_regex = re.compile(r'(\w+) => (\w+)')
tokenize_regex = re.compile(r'([A-Ze][a-z]?)')

replacements = {}
medicine_molecule = ''
tokens = []

with open('../input/day19.txt') as f:
    for line in f:
        replacement = replacements_regex.match(line)
        if replacement is not None:
            before, after = replacement.groups()
            if before not in replacements.keys():
                replacements[before] = []
            replacements[before].append(after)
        else:
            tokens = tokenize_regex.findall(line)
            medicine_molecule = line

# print(tokens)
# print(replacements)

print(medicine_molecule)

distinct_molecules = permute_replacements(tokens, replacements)

print('Part 1 answer: {}'.format(len(distinct_molecules)))

this_layer = set('e')
num_replacements = 0

while medicine_molecule not in this_layer:
    next_layer = set()
    for item in this_layer:
        tokens = tokenize_regex.findall(item)
        for permutation in permute_replacements(tokens, replacements):
            next_layer.add(permutation)
    num_replacements += 1
    this_layer = next_layer
    print(num_replacements)
    print(len(this_layer))

print('Part 2 answer: {}'.format(num_replacements))


