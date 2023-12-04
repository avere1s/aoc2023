import re
import sys

schematic = []
part_numbers = []
sum = 0

for line in sys.stdin:
    schematic.append(line.rstrip())

print(f"{schematic=}")

for line_idx, a_line in enumerate(schematic):
    print(f"{line_idx=}")
    part_numbers.append([])

    for a_number in re.finditer(r"\d+", a_line):
        print(f"    {a_number=}")

        left_bound = 0
        right_bound = len(a_line) - 1

        found_a_symbol = False

        if a_number.start() > 0:
            left_bound = a_number.start() - 1

        print(f"        Looking left: {left_bound=}: {a_line[left_bound]}")
        if a_line[left_bound] != "." and a_line[left_bound] not in [
            "0",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
        ]:
            print(f"        Found a symbol {a_line[left_bound]} to the left")
            found_a_symbol = True

        if a_number.end() < len(a_line) - 1:
            right_bound = a_number.end()

        print(f"        Looking right: {right_bound=}: {a_line[right_bound]}")
        if a_line[right_bound] != "." and a_line[right_bound] not in [
            "0",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
        ]:
            print(f"        Found a symbol {a_line[right_bound]} to the right")
            found_a_symbol = True

        if found_a_symbol:
            part_numbers[line_idx].append(a_number)
            continue

        if line_idx > 0:
            for bound_idx in range(left_bound, right_bound + 1):
                print(f"        {bound_idx=}")

                if schematic[line_idx - 1][bound_idx] != "." and schematic[
                    line_idx - 1
                ][bound_idx] not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    print(
                        f"        Found a symbol {schematic[line_idx - 1][bound_idx]} above at {bound_idx}"
                    )
                    found_a_symbol = True
                    break

        if found_a_symbol:
            part_numbers[line_idx].append(a_number)
            continue

        if line_idx < len(schematic) - 1:
            for bound_idx in range(left_bound, right_bound + 1):
                print(f"        {bound_idx=}")

                if schematic[line_idx + 1][bound_idx] != "." and schematic[
                    line_idx + 1
                ][bound_idx] not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    print(
                        f"        Found a symbol {schematic[line_idx + 1][bound_idx]} below at {bound_idx}"
                    )
                    found_a_symbol = True
                    break

        if found_a_symbol:
            part_numbers[line_idx].append(a_number)
            continue

print("===================================")
print("Found the following part numbers:")

for line_idx, a_line in enumerate(part_numbers):
    print(f"{line_idx}: {a_line}")

print("===================================")

for line_idx, a_line in enumerate(schematic):
    print(f"{line_idx=}")

    for char_idx, a_char in enumerate(a_line):
        if a_char == "*":
            print(f"    Found a potential gear at {char_idx}")

            number_of_matching_parts = 0
            matching_part_list = []

            # Check the same line
            for number_idx, a_number in enumerate(part_numbers[line_idx]):
                print(f"        Checking: {a_number=} vs {char_idx=}")
                if a_number.end() == char_idx or a_number.start() == char_idx + 1:
                    print(
                        f"        Found a matching part number - {line_idx}:{number_idx}={a_number.group()}"
                    )
                    number_of_matching_parts += 1
                    matching_part_list.append(int(a_number.group()))

            # Check the line above
            if line_idx > 0:
                for number_idx, a_number in enumerate(part_numbers[line_idx - 1]):
                    print(f"        Checking: {a_number=} vs {char_idx=}")
                    if a_number.end() >= char_idx and a_number.start() <= char_idx + 1:
                        print(
                            f"        Found a matching part number - {line_idx-1}:{number_idx}={a_number.group()}"
                        )
                        number_of_matching_parts += 1
                        matching_part_list.append(int(a_number.group()))

            # Check the line below
            if line_idx < len(schematic) - 1:
                for number_idx, a_number in enumerate(part_numbers[line_idx + 1]):
                    print(f"        Checking: {a_number=} vs {char_idx=}")
                    if a_number.end() >= char_idx and a_number.start() <= char_idx + 1:
                        print(
                            f"        Found a matching part number - {line_idx+1}:{number_idx}={a_number.group()}"
                        )
                        number_of_matching_parts += 1
                        matching_part_list.append(int(a_number.group()))

            if number_of_matching_parts == 2:
                print(
                    f"    Found a gear at {line_idx}:{char_idx} - {matching_part_list=}"
                )
                gear_ratio = 1
                for a_number in matching_part_list:
                    gear_ratio *= a_number
                sum += gear_ratio
                print(f"    Sum: {sum}. Added {gear_ratio}")
