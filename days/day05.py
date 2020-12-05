file = open(r"C:\Users\Antoine\Desktop\AoC\AoC2020\data\day05.txt", mode="r")

data = file.read()
list_raw_ids = data.split("\n")


def get_seat_coordinates(code):
    row_code = code[:7]
    low_index = 0
    up_index = 127
    for letter in row_code:
        middle_ = int((up_index + low_index) / 2)
        if letter == "F":
            up_index = middle_
        else:
            low_index = middle_

    row_indice = up_index

    column_code = code[7:]
    low_index = 0
    up_index = 7
    for letter in column_code:
        middle_ = int((up_index + low_index) / 2)
        if letter == "R":
            low_index = middle_
        else:
            up_index = middle_

    column_indice = up_index
    return row_indice, column_indice


def get_seat_id(code):
    row_indice, column_indice = get_seat_coordinates(code)
    return row_indice * 8 + column_indice

# Part One
max_ = 0
for raw_id in list_raw_ids:
    seat_id = get_seat_id(raw_id)
    if max_ < seat_id:
        max_ = seat_id

print(max_)

# Part two
list_ids = []
for raw_id in list_raw_ids:
    list_ids.append(get_seat_id(raw_id))

possible_seats = []
for i in range(max_):
    if not(i in list_ids) and (i-1 in list_ids) and (i+1 in list_ids):
        possible_seats.append(i)

print(possible_seats)

