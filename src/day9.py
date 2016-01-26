import re


def trace_route(current_location: str, distance_travelled: int, to_visit: set, visited: list):
    global distances, best_distance, best_route

    print(to_visit, visited)

    if distance_travelled > best_distance:
        print('Abort!')
        return

    if len(to_visit) == 0:
        if distance_travelled < best_distance:
            best_distance = distance_travelled
            best_route = visited
            print('d!')
        return

    for location in to_visit:
        new_distance_travelled = distance_travelled + distances[frozenset([current_location, location])]
        trace_route(location, new_distance_travelled, to_visit - {location}, visited + [location])



distances = {}
destinations = set()

regex = re.compile('(.+) to (.+) = (\d+)')

distances_upper_limit = 0

with open('../input/day9') as f:
    for line in f:
        match = regex.match(line)
        start, end, distance = match.groups()
        destinations.update([start, end])
        distances[frozenset([start, end])] = int(distance)
        distances_upper_limit += int(distance)

print('All destinations:')
print(destinations)

best_distance = distances_upper_limit
best_route = []

for location in destinations:
    trace_route(location, 0, destinations - {location}, [location])

print(best_distance, best_route)
