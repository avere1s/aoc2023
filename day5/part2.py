import sys


def translate_with_rules(values, rules):
    res = []

    for a_value in values:
        rule_found = False
        for a_rule in rules:
            if a_value >= a_rule[1] and a_value <= a_rule[1] + a_rule[2]:
                print(f"{a_value} is between {a_rule[1]} and {a_rule[1]+a_rule[2]}")
                rule_found = True
                res.append(a_rule[0] + (a_value - a_rule[1]))
                break
        if not rule_found:
            print(f"{a_value} is not between any rules")
            res.append(a_value)
    return res


def translate_ranges_with_rules(input_ranges, rules):
    res = []

    remaining_ranges = input_ranges

    for a_rule in rules:
        istart = a_rule[1]
        ostart = a_rule[0]
        step = a_rule[2]
        istart_end = istart + step

        print(f"    Rule range: ({istart}, {istart_end}) -> ({ostart}, {ostart+step})")

        updated_remaining_ranges = []

        for a_range in remaining_ranges:
            print(f"        Remaining range: {a_range}")
            before_overlap = (a_range[0], min(a_range[1], istart))
            overlap = (max(a_range[0], istart), min(istart_end, a_range[1]))
            after_overlap = (max(istart_end, a_range[0]), a_range[1])

            if before_overlap[1] > before_overlap[0]:
                print(f"            Before overlap: {before_overlap}")
                updated_remaining_ranges.append(before_overlap)
            if overlap[1] > overlap[0]:
                print(
                    f"            Overlap: {overlap} -> {[overlap[0] - istart + ostart, overlap[1] - istart + ostart]}"
                )
                res.append([overlap[0] - istart + ostart, overlap[1] - istart + ostart])
            if after_overlap[1] > after_overlap[0]:
                print(f"            After overlap: {after_overlap}")
                updated_remaining_ranges.append(after_overlap)

        remaining_ranges = updated_remaining_ranges

    res = res + remaining_ranges

    return res


# read seeds
seeds = []

translations = {
    "seeds": [],
    "soils": [],
    "fertilizers": [],
    "waters": [],
    "lights": [],
    "temperatures": [],
    "humidities": [],
    "locations": [],
}

line = sys.stdin.readline()
print(line.rstrip())

for a_seed in line.rstrip().split(" ")[1:]:
    seeds.append(int(a_seed))

for i in range(0, len(seeds), 2):
    translations["seeds"].append([seeds[i], seeds[i] + seeds[i + 1]])


print(f"{seeds=}")
print(f"{translations['seeds']=}")

line = sys.stdin.readline()

# read seed-to-soil map:
seed_soil_rules = []
for line in sys.stdin:
    print(line.rstrip())
    if line.rstrip() == "":
        break
    if line.rstrip() == "seed-to-soil map:":
        continue
    seed_soil_rules.append([])
    seed_soil_rules[-1] = list(map(int, line.rstrip().split(" ")))

print(f"{seed_soil_rules=}")

translations["soils"] = translate_ranges_with_rules(
    translations["seeds"], seed_soil_rules
)

print(f"{translations=}")

# read soil-to-fertilizer map:
soil_fertilizer_rules = []
for line in sys.stdin:
    print(line.rstrip())
    if line.rstrip() == "":
        break
    if line.rstrip() == "soil-to-fertilizer map:":
        continue
    soil_fertilizer_rules.append([])
    soil_fertilizer_rules[-1] = list(map(int, line.rstrip().split(" ")))

print(f"{soil_fertilizer_rules=}")

translations["fertilizers"] = translate_ranges_with_rules(
    translations["soils"], soil_fertilizer_rules
)

print(f"{translations=}")

# read fertilizer-to-water map:

fertilizer_water_rules = []
for line in sys.stdin:
    print(line.rstrip())
    if line.rstrip() == "":
        break
    if line.rstrip() == "fertilizer-to-water map:":
        continue
    fertilizer_water_rules.append([])
    fertilizer_water_rules[-1] = list(map(int, line.rstrip().split(" ")))

print(f"{fertilizer_water_rules=}")

translations["waters"] = translate_ranges_with_rules(
    translations["fertilizers"], fertilizer_water_rules
)

print(f"{translations=}")

# read water-to-light map:

water_light_rules = []
for line in sys.stdin:
    print(line.rstrip())
    if line.rstrip() == "":
        break
    if line.rstrip() == "water-to-light map:":
        continue
    water_light_rules.append([])
    water_light_rules[-1] = list(map(int, line.rstrip().split(" ")))

print(f"{water_light_rules=}")

translations["lights"] = translate_ranges_with_rules(
    translations["waters"], water_light_rules
)

print(f"{translations=}")

# read light-to-temperature map:

light_temperature_rules = []
for line in sys.stdin:
    print(line.rstrip())
    if line.rstrip() == "":
        break
    if line.rstrip() == "light-to-temperature map:":
        continue
    light_temperature_rules.append([])
    light_temperature_rules[-1] = list(map(int, line.rstrip().split(" ")))

print(f"{light_temperature_rules=}")

translations["temperatures"] = translate_ranges_with_rules(
    translations["lights"], light_temperature_rules
)

print(f"{translations=}")

# read temperature-to-humidity map:

temperature_humidity_rules = []
for line in sys.stdin:
    print(line.rstrip())
    if line.rstrip() == "":
        break
    if line.rstrip() == "temperature-to-humidity map:":
        continue
    temperature_humidity_rules.append([])
    temperature_humidity_rules[-1] = list(map(int, line.rstrip().split(" ")))

print(f"{temperature_humidity_rules=}")

translations["humidities"] = translate_ranges_with_rules(
    translations["temperatures"], temperature_humidity_rules
)

print(f"{translations=}")

# read humidity-to-location map:

humidity_location_rules = []

for line in sys.stdin:
    print(line.rstrip())
    if line.rstrip() == "":
        break
    if line.rstrip() == "humidity-to-location map:":
        continue
    humidity_location_rules.append([])
    humidity_location_rules[-1] = list(map(int, line.rstrip().split(" ")))

print(f"{humidity_location_rules=}")

translations["locations"] = translate_ranges_with_rules(
    translations["humidities"], humidity_location_rules
)

print(f"{translations=}")

min = translations["locations"][0][0]
for a_location in translations["locations"]:
    if a_location[0] < min:
        min = a_location[0]

print(f"{min=}")

# print(f"{min(translations['locations'])=}")
