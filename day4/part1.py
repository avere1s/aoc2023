import re
import sys

line_number = 0
sum = 0

for line in sys.stdin:
    line_number += 1
    print(f"{line_number}: {line.rstrip()}")

    card_match = re.search(
        r"Card\s+(?P<card_number>\d+): (?P<numbers>.+)", line.rstrip()
    )

    if card_match:
        print(f"Card number: {card_match.group('card_number')}")
        print(f"Numbers: {card_match.group('numbers')}")

        numbers = card_match.group("numbers").split("|")

        winning_numbers = []

        for a_number in re.findall(r"\d+", numbers[0]):
            winning_numbers.append(int(a_number))

        print(f"{winning_numbers=}")

        numbers_we_have = []

        for a_number in re.findall(r"\d+", numbers[1]):
            numbers_we_have.append(int(a_number))

        print(f"{numbers_we_have=}")

        for a_number in numbers_we_have:
            if numbers_we_have.count(a_number) > 1:
                print(f"    Number {a_number} appears more than once")
                exit(1)

        card_value = 0

        numbers_won = []

        for a_number in numbers_we_have:
            if a_number in winning_numbers:
                numbers_won.append(a_number)
                if card_value == 0:
                    card_value = 1
                else:
                    card_value *= 2

        print(f"Card value: {card_value}. Numbers won: {numbers_won}")

        sum += card_value
        print(f"Sum: {sum}. Added {card_value}")
