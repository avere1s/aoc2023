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

translations["seeds"] = seeds

print(f"{seeds=}")

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

translations["soils"] = translate_with_rules(seeds, seed_soil_rules)

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

translations["fertilizers"] = translate_with_rules(
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

translations["waters"] = translate_with_rules(
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

translations["lights"] = translate_with_rules(translations["waters"], water_light_rules)

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

translations["temperatures"] = translate_with_rules(
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

translations["humidities"] = translate_with_rules(
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

translations["locations"] = translate_with_rules(
    translations["humidities"], humidity_location_rules
)

print(f"{translations=}")

print(f"{min(translations['locations'])=}")
