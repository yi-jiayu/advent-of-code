length_of_string_literals = 0
length_of_string_values = 0
length_of_reencoded_strings = 0

with open('../input/day8') as f:
    for line in f:
        line = line.replace('\n', '')
        print(line)
        print(len(line))
        print(bytes(line, "utf-8").decode("unicode_escape"))
        print(len(bytes(line, "utf-8").decode("unicode_escape")))
        print(repr(line))
        print(len(repr(line)))
        length_of_string_literals += len(line)
        length_of_string_values += len(bytes(line, "utf-8").decode("unicode_escape")) - 2
        length_of_reencoded_strings += len(line) + 2
        length_of_reencoded_strings += line.count('"')
        length_of_reencoded_strings += line.count('\\')


print(length_of_string_literals - length_of_string_values)
print(length_of_reencoded_strings - length_of_string_literals)
