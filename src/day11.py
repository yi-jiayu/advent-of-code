def increment_password(pw: str):
    ordinals = [ord(c) for c in pw]

    while True:
        for pos in reversed(range(len(ordinals))):
            if ordinals[pos] < 122:
                ordinals[pos] += 1
                break
            else:
                ordinals[pos] = 97
                if ordinals[0] > 122:
                    raise StopIteration()
        yield ''.join(chr(o) for o in ordinals)


def check_password(pw: str) -> bool:
    # cannot contain i, o, l
    for illegal_char in ('i', 'o', 'l'):
        if illegal_char in pw:
            return False

    # include one increasing straight
    for pos in range(len(pw) - 1):
        if pos == len(pw) - 2:
            return False
        if ord(pw[pos + 1]) == (ord(pw[pos]) + 1) and ord(pw[pos + 2]) == (ord(pw[pos]) + 2):
            break

    # contain two different, non-overlapping pairs of letters
    first_pair = None
    for pos in range(len(pw) - 1):
        if pw[pos] == pw[pos + 1]:
            if first_pair is None:
                first_pair = pw[pos]
            elif pw[pos] != first_pair:
                return True

    return False


def generate_next_valid_password(old_pw: str) -> str:
    counter = 0
    for pw in increment_password(old_pw):
        counter += 1
        # if not counter % (2 << 15):
        #     print('Attempt {}: Trying \'{}\''.format(counter, pw))
        if check_password(pw):
            return pw


if __name__ == '__main__':
    with open('../input/day11.txt') as f:
        inp = f.read().strip()

    print("Input: " + inp)
    print("Calculating...")

    part_one_ans = generate_next_valid_password(inp)
    part_two_ans = generate_next_valid_password(part_one_ans)
    print('Part one answer: {}'.format(part_one_ans))
    print('Part two answer: {}'.format(part_two_ans))

