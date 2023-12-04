import re
import sys

schematic = []
sum = 0

for line in sys.stdin:
    schematic.append(line.rstrip())

print(f"{schematic=}")

for line_idx, a_line in enumerate(schematic):
    print(f"{line_idx=}")

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
            sum += int(a_number.group())
            print(f"        Sum: {sum}. Added {a_number.group()}")
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
            sum += int(a_number.group())
            print(f"        Sum: {sum}. Added {a_number.group()}")
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
            sum += int(a_number.group())
            print(f"        Sum: {sum}. Added {a_number.group()}")
            continue
