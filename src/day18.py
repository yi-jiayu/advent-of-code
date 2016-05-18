from copy import deepcopy
import pprint

NUM_STEPS = 100


class LightGrid:
    def __init__(self, rows: list):
        self.rows = rows

    def step(self):
        next_step = deepcopy(self.rows)

        for i in range(len(self.rows)):
            for j in range(len(self.rows[i])):
                lit_neighbours = self.lit_neighbours(i, j)
                # on
                if self.rows[i][j] == '#':
                    if lit_neighbours not in (2, 3):
                        next_step[i][j] = '.'
                # off
                elif self.rows[i][j] == '.':
                    if lit_neighbours == 3:
                        next_step[i][j] = '#'
        self.rows = next_step

    def lit_neighbours(self, i, j):
        lit_neighbours = 0
        for x, y in LightGrid.neighbours(i, j):
            try:
                if x < 0 or y < 0:
                    continue
                if self.rows[x][y] == '#':
                    lit_neighbours += 1
            except IndexError:
                pass
        return lit_neighbours

    @staticmethod
    def neighbours(x, y):
        for adjacent in ((x - 1, y - 1),
                         (x - 1, y),
                         (x - 1, y + 1),
                         (x, y - 1),
                         (x, y + 1),
                         (x + 1, y - 1),
                         (x + 1, y),
                         (x + 1, y + 1)):
            yield adjacent


rows = []

with open('../input/day18.txt') as f:
    for line in f:
        rows.append([char for char in line])

# test_grid = """.#.#.#
# ...##.
# #....#
# ..#...
# #.#..#
# ####.."""
#
# test_rows = []
#
# for line in test_grid.split('\n'):
#     test_rows.append([char for char in line if char in ('#', '.')])
#
# light_grid = LightGrid(test_rows)
# pprint.pprint(light_grid.rows)

light_grid = LightGrid(rows)

for i in range(NUM_STEPS):
    print('Simulating step {}'.format(i + 1))
    light_grid.step()

lights_on = 0

for i in range(len(light_grid.rows)):
    for j in range(len(light_grid.rows[i])):
        if light_grid.rows[i][j] == '#':
            lights_on += 1

print('Part 1 answer: {}'.format(lights_on))
