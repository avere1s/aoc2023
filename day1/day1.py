import sys


line_digit = 0
sum = 0

for line in sys.stdin:
    line_digit += 1
    print(f"{line_digit}: {line.rstrip()}")

    print("")

    first_digit = -1
    first_character_position = 0
    for a_character in line.rstrip():
        first_character_position += 1
        print(f"    {a_character}: {ord(a_character)}")

        if ord(a_character) > 47 and ord(a_character) < 58:
            print(f"Found digit: {a_character}, position: {first_character_position}")
            first_digit = int(a_character)
            break

    if first_digit == -1:
        print("First digit not found")
        exit(1)

    if first_character_position == len(line.rstrip()):
        print("First digit found at the last line character")

        sum += first_digit * 10 + first_digit
        print(f"Sum: {sum}. Added {first_digit * 10 + first_digit}")
        continue

    second_digit = -1
    print("Characters in reverse:")
    second_character_position = len(line.rstrip())
    for index in range(len(line.rstrip()) - 1, first_character_position - 1, -1):
        second_character_position -= 1
        print(f"    {line[index]}: {ord(line[index])}")

        if ord(line[index]) > 47 and ord(line[index]) < 58:
            print(f"Found digit: {line[index]}, position: {second_character_position}")
            second_digit = int(line[index])
            break

    if second_digit != -1:
        print(f"Found numbers: {first_digit} and {second_digit}")
        sum += first_digit * 10 + second_digit
        print(f"Sum: {sum}. Added {first_digit * 10 + second_digit}")
    else:
        print("Second digit not found")

        sum += first_digit * 10 + first_digit
        print(f"Sum: {sum}. Added {first_digit * 10 + first_digit}")
        continue
