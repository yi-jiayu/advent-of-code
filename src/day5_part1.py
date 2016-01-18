def vowel_check(name):
    vowel_count = 0
    for vowel in ('a', 'e', 'i', 'o', 'u'):
        vowel_count += name.count(vowel)
        if vowel_count > 2:
            return True
    return False


def double_letter_check(name):
    previous_char = '\0'
    for char in name:
        if char == previous_char:
            return True
        previous_char = char
    return False


def naughty_substring_check(name):
    for substring in ('ab', 'cd', 'pq', 'xy'):
        if substring in name:
            return False
    return True

nice_string_count = 0

with open('../input/day5') as f:
    for line in f:
        if vowel_check(line):
            if double_letter_check(line):
                if naughty_substring_check(line):
                    nice_string_count += 1

print('{} strings are nice!'.format(nice_string_count))
