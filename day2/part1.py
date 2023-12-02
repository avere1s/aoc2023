import re
import sys

# bag contains only 12 red cubes, 13 green cubes, and 14 blue cubes?
bag = {"red": 12, "green": 13, "blue": 14}

line_number = 0
sum = 0

for line in sys.stdin:
    line_number += 1
    print(f"{line_number}: {line.rstrip()}")

    # Game 1: 19 blue, 12 red; 19 blue, 2 green, 1 red; 13 red, 11 blue

    game_match = re.search(r"Game (?P<game_number>\d+): (?P<reveals>.+)", line.rstrip())

    if game_match:
        print(f"Game number: {game_match.group('game_number')}")
        print(f"Reveals: {game_match.group('reveals')}")

        reveals = game_match.group("reveals").split("; ")
        game_number = int(game_match.group("game_number"))

        possible_game = True
        for idx, reveal in enumerate(reveals):
            print(f"    Reveal: {idx+1} - {reveal}")
            for color in reveal.split(", "):
                print(f"    {color}")

                color_match = re.search(r"(?P<quantity>\d+) (?P<color>\w+)", color)

                if color_match:
                    print(f"    Quantity: {color_match.group('quantity')}")
                    print(f"    Color: {color_match.group('color')}")

                    if (
                        int(color_match.group("quantity"))
                        > bag[color_match.group("color")]
                    ):
                        print(
                            f'    Not enough {color_match.group("color")} cubes: {color_match.group("quantity")} > {bag[color_match.group("color")]}. Game is impossible'
                        )
                        possible_game = False
                        break
                else:
                    print("    No match")
                    exit(1)

            if not possible_game:
                break

        if possible_game:
            print("    Game is possible")
            sum += game_number
            print(f"    Sum: {sum}. Added {game_number}")

    print("")

    print(f"Sum: {sum}")
