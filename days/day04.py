import re


test_pattern = re.compile("[a-f0-9]+")
print("should be false", test_pattern.fullmatch("zfejfe") != None)
print("should be true", test_pattern.fullmatch("12abc6"))

file = open(r"C:\Users\Antoine\Desktop\AoC\AoC2020\data\day04.txt", mode="r")

data = file.read()
list_lines = data.split("\n\n")


def process_line(lines):
    dict_result = {}
    lines_split = lines.split("\n")
    fields = []
    for line in lines_split:
        split_space = line.split(" ")
        for field in split_space:
            fields.append(field)

    for field in fields:
        split = field.split(":")
        field_name = split[0]
        field_value = split[1]
        dict_result[field_name] = field_value

    return dict_result


hexa_pattern = re.compile("[a-f0-9]+")
digit_pattern = re.compile("[0-9]+")


def field_is_valid(field, dict_):
    global hexa_pattern
    global digit_pattern

    if field in dict_.keys():
        if field == "byr":
            return int(dict_["byr"]) >= 1920 and int(dict_["byr"]) <= 2002

        if field == "iyr":
            return int(dict_["iyr"]) >= 2010 and int(dict_["iyr"]) <= 2020

        if field == "eyr":
            return int(dict_["eyr"]) >= 2020 and int(dict_["eyr"]) <= 2030

        if field == "hgt":
            unit = dict_["hgt"][-2:]
            if unit == "cm":
                return int(dict_["hgt"][:-2]) >= 150 and int(dict_["hgt"][:-2]) <= 193
            elif unit == "in":
                return int(dict_["hgt"][:-2]) >= 59 and int(dict_["hgt"][:-2]) <= 76
            else:
                return False

        if field == "hcl":
            if dict_["hcl"][0] == "#":
                hexa_code = dict_["hcl"][1:]
                if len(hexa_code) == 6:
                    return hexa_pattern.fullmatch(hexa_code) != None
                else:
                    return False

            else:
                return False

        if field == "ecl":
            return dict_["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

        if field == "pid":
            return (digit_pattern.fullmatch(dict_["pid"]) != None) and (
                len(dict_["pid"]) == 9
            )

    else:
        return False


def is_good_dict(dict_):
    test_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for field in test_fields:
        if not (field_is_valid(field, dict_)):
            return False

    return True


list_processed_dicts = [process_line(lines) for lines in list_lines]
filtered_dicts = [d_ for d_ in list_processed_dicts if is_good_dict(d_)]

print(len(list_processed_dicts), len(filtered_dicts))

# test_dict = {
#     "pid": "087499704",
#     "hgt": "74in",
#     "ecl": "grn",
#     "iyr": "2012",
#     "eyr": "2030",
#     "byr": "1980",
#     "hcl": "#623a2f",
# }


# print(is_good_dict(test_dict))