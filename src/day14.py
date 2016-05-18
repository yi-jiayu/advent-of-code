import re


class Reindeer:
    def __init__(self, name: str, top_speed: int, flight_time: int, rest_time: int):
        self.name = name
        self.top_speed = top_speed
        self.flight_time = flight_time
        self.rest_time = rest_time

        self.cycle_time = flight_time + rest_time
        self.cycle_distance = top_speed * flight_time

    def distance_travelled(self, seconds: int) -> int:
        cycles = seconds // self.cycle_time
        current_cycle_time = seconds % self.cycle_time
        current_cycle_distance = self.top_speed * min(self.flight_time, current_cycle_time)

        return cycles * self.cycle_distance + current_cycle_distance


regex = re.compile(r'(\w+) can fly (\d+) km\/s for (\d+) seconds, but then must rest for (\d+) seconds.')

reindeers = []

with open('../input/day14.txt') as f:
    for line in f:
        name, top_speed, flight_time, rest_time = regex.match(line).groups()
        reindeers.append(Reindeer(name, int(top_speed), int(flight_time), int(rest_time)))

print('Part 1 ans: {}'.format(max([reindeer.distance_travelled(2503) for reindeer in reindeers])))

scores = {}
for reindeer in reindeers:
    scores[reindeer.name] = 0

for seconds in range(1, 2504):
    distances = [(reindeer.name, reindeer.distance_travelled(seconds)) for reindeer in reindeers]
    max_distance = max([distance[1] for distance in distances])
    for reindeer, distance_travelled in distances:
        if distance_travelled == max_distance:
            scores[reindeer] += 1

print('Part 2 ans: {}'.format(max(scores.values())))
