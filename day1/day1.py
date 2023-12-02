import sys


line_number = 0
sum = 0

for line in sys.stdin:
    line_number += 1
    print(f"{line_number}: {line.rstrip()}")

    print("")

    first_digit = -1
    first_digit_position = 0
    for a_digit in line.rstrip():
        first_digit_position += 1
        print(f"    {a_digit}: {ord(a_digit)}")

        if ord(a_digit) > 47 and ord(a_digit) < 58:
            print(f"Found digit: {a_digit}, position: {first_digit_position}")
            first_digit = int(a_digit)
            break

    if first_digit == -1:
        print("First digit not found")
        exit(1)

    if first_digit_position == len(line.rstrip()):
        print("First digit found at the last line digit")

        sum += first_digit * 10 + first_digit
        print(f"Sum: {sum}. Added {first_digit * 10 + first_digit}")
        continue

    second_digit = -1
    print("characters in reverse:")
    second_digit_position = len(line.rstrip())
    for index in range(len(line.rstrip()) - 1, first_digit_position - 1, -1):
        second_digit_position -= 1
        print(f"    {line[index]}: {ord(line[index])}")

        if ord(line[index]) > 47 and ord(line[index]) < 58:
            print(f"Found digit: {line[index]}, position: {second_digit_position}")
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
