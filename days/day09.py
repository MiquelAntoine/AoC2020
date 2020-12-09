file = open(r"C:\Users\Antoine\Desktop\AoC\AoC2020\data\day09.txt", mode="r")

data = file.read()
list_raw_numbers = data.split("\n")
list_numbers = [int(el) for el in list_raw_numbers]


def find_decomposeur(list_, number_):
    for i in range(len(list_)):
        for j in range(i + 1, len(list_)):
            if list_[i] + list_[j] == number_:
                return (i, j)

    return None


print(not None)
upper_index = 25
lower_index = 0
continue_ = True
while continue_:
    last_25_numbers = list_numbers[lower_index:upper_index]
    if not (find_decomposeur(last_25_numbers, list_numbers[upper_index])):
        continue_ = False
        print(list_numbers[upper_index])
        print("invalid number index", upper_index)
        invalid_number = list_numbers[upper_index]
    lower_index += 1
    upper_index += 1


lower_index = 0
upper_index = lower_index + 2
sum_ = sum(list_numbers[lower_index:upper_index])
while sum_ != invalid_number:
    if sum_ < invalid_number:
        # Then we can try to add another one
        upper_index += 1
        sum_ = sum(list_numbers[lower_index:upper_index])
    else:
        # We have to move from the next begining number
        # print(lower_index)
        lower_index += 1
        upper_index = lower_index + 2
        sum_ = sum(list_numbers[lower_index:upper_index])

print(
    min(
        list_numbers[lower_index:upper_index])
        + max(list_numbers[lower_index:upper_index])
    )
