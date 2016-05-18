DAY_10_INPUT = '1113222113'
NUM_ITERATIONS = 40


def tokenise_digits(number: str) -> list:
    current_char = number[0]
    current_char_count = 1
    tokenised_digits = []
    for i in range(1, len(number)):
        if number[i] != current_char:
            tokenised_digits.append((current_char_count, current_char))
            current_char = number[i]
            current_char_count = 1
        else:
            current_char_count += 1
        if i == len(number) - 1:
            tokenised_digits.append((current_char_count, current_char))
    return tokenised_digits


def look_and_say(tokenised_digits: list) -> str:
    output = ''
    for count, number in tokenised_digits:
        output += str(count) + number
    return output

result = DAY_10_INPUT

for i in range(NUM_ITERATIONS):
    result = look_and_say(tokenise_digits(result))

print('The length of the result is {}'.format(len(result)))
