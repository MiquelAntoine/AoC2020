file = open(r"C:\Users\Antoine\Desktop\AoC\AoC2020\data\day08.txt", mode="r")

data = file.read()
list_instructions = data.split("\n")


# # Partie 1
# set_index = set()
# index_ = 0
# acc = 0

# while not index_ in set_index:
#     print(index_)
#     set_index.add(index_)
#     split = list_instructions[index_].split(" ")
#     key_word = split[0]
#     if key_word == "acc":
#         sign = split[1][0]
#         value = int(split[1][1:])
#         if sign == "+":
#             acc += value
#         else:
#             acc -= value

#         index_ += 1

#     elif key_word == "jmp":
#         sign = split[1][0]
#         value = int(split[1][1:])
#         if sign == "+":
#             index_ += value
#         else:
#             index_ -= value

#     elif key_word == "nop":
#         index_ += 1


def read_programme(list_instructions):
    set_index = set()
    index_ = 0
    acc = 0
    nb_intstruction = len(list_instructions)
    while not index_ in set_index and index_ < nb_intstruction:
        set_index.add(index_)
        split = list_instructions[index_].split(" ")
        key_word = split[0]
        if key_word == "acc":
            sign = split[1][0]
            value = int(split[1][1:])
            if sign == "+":
                acc += value
            else:
                acc -= value

            index_ += 1

        elif key_word == "jmp":
            sign = split[1][0]
            value = int(split[1][1:])
            if sign == "+":
                index_ += value
            else:
                index_ -= value

        elif key_word == "nop":
            index_ += 1

    if index_ < len(list_instructions):
        return -0.1

    else:
        return acc


# Partie 2

for i in range(len(list_instructions)):
    instruction = list_instructions[i]
    keyword = instruction.split(" ")[0]
    if keyword == "jmp":
        new_instruction = "nop " + instruction.split(" ")[1]
        list_instructions[i] = new_instruction
        value = read_programme(list_instructions)
        if value != -0.1:
            print(value)
        list_instructions[i] = instruction

    elif keyword == "nop":
        new_instruction = "jmp " + instruction.split(" ")[1]
        list_instructions[i] = new_instruction
        value = read_programme(list_instructions)
        if value != -0.1:
            print(value)
        list_instructions[i] = instruction

    else:
        pass
