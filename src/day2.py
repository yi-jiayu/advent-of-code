wrapping_paper_needed = 0
ribbon_needed = 0

with open('../input/day2') as f:
    for line in f:
        l, w, h = [int(x) for x in line.split('x')]
        wrapping_paper_needed += 2 * (l*w + l*h + w*h)
        wrapping_paper_needed += (l * w * h) / (max(l, w, h))

        ribbon_needed += 2 * (l + w + h) - 2 * max(l, w, h)
        ribbon_needed += l * w * h

print('Square feet of wrapping paper needed: ' + str(int(wrapping_paper_needed)))
print('Feet of ribbon needed: ' + str(ribbon_needed))
