import re
import sys

line_number = 0
sum = 0

card_count = [0]

for line in sys.stdin:
    line_number += 1
    print(f"{line_number}: {line.rstrip()}")

    card_match = re.search(
        r"Card\s+(?P<card_number>\d+): (?P<numbers>.+)", line.rstrip()
    )

    if card_match:
        print(f"Card number: {card_match.group('card_number')}")
        print(f"Numbers: {card_match.group('numbers')}")

        card_number = int(card_match.group("card_number"))

        if len(card_count) <= card_number:
            card_count.append(1)
        else:
            card_count[card_number] += 1

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

        for number_idx, a_number in enumerate(numbers_won):
            print(f"    {number_idx=} {a_number=}")
            if len(card_count) <= card_number + number_idx + 1:
                print(
                    f"    Next card has not been initialized. Appending to {card_count[card_number]} card_count"
                )
                card_count.append(card_count[card_number])
                print(f"    New value: {card_count[card_number + number_idx + 1]}")
            else:
                print(
                    f"    Next card already has a value {card_count[card_number + number_idx + 1]}. Adding {card_count[card_number]} card_count"
                )
                card_count[card_number + number_idx + 1] += card_count[card_number]
                print(f"    New value: {card_count[card_number + number_idx + 1]}")

        print(f"{card_count=}")

print(f"{card_count=}")

for a_count in card_count:
    sum += a_count

print(f"Sum: {sum}")
