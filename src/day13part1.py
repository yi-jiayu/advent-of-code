import re
from itertools import permutations

regex = re.compile(r'(\w+) would (lose|gain) (\d+) happiness units by sitting next to (\w+)')

happiness_changes = {}

with open('../input/day13.txt') as f:
    for line in f:
        subject, direction, change, other = regex.match(line).groups()
        if subject not in happiness_changes.keys():
            happiness_changes[subject] = {}
        happiness_changes[subject][other] = int(change) if direction == 'gain' else -1 * int(change)

invitees = list(happiness_changes.keys())
anchor = invitees.pop()

arrangements = permutations(invitees)
net_happinesses = []

for arrangement in arrangements:
    net_happiness = 0
    prev_person = anchor
    for person in arrangement:
        net_happiness += happiness_changes[prev_person][person] + happiness_changes[person][prev_person]
        prev_person = person
    net_happiness += happiness_changes[prev_person][anchor] + happiness_changes[anchor][prev_person]
    net_happinesses.append(net_happiness)

print('Part 1 ans: {}'.format(max(net_happinesses)))
