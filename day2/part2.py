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

        current_bag = {
            "red": 0,
            "blue": 0,
            "green": 0,
        }

        reveals = game_match.group("reveals").split("; ")
        game_number = int(game_match.group("game_number"))

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
                        > current_bag[color_match.group("color")]
                    ):
                        print(
                            f'    Not enough {color_match.group("color")} '
                            + f'cubes: {color_match.group("quantity")} > '
                            + f'{current_bag[color_match.group("color")]}. '
                            + f'Increasing bag to {color_match.group("quantity")}'
                        )
                        current_bag[color_match.group("color")] = int(
                            color_match.group("quantity")
                        )
                else:
                    print("    No match")
                    exit(1)

        if (
            current_bag["red"] == 0
            or current_bag["blue"] == 0
            or current_bag["green"] == 0
        ):
            print("    One color is missing: {current_bag}")
            exit(1)
        else:
            sum += current_bag["red"] * current_bag["blue"] * current_bag["green"]
            print(f"    {current_bag=}")
            print(
                f'    Sum: {sum}. Added {current_bag["red"]*current_bag["blue"]*current_bag["green"]}'
            )

    print("")

    print(f"Sum: {sum}")
