file = open(r"C:\Users\Antoine\Desktop\AoC\AoC2020\data\day03.txt", mode="r")

data = file.read()
list_lines = data.split("\n")

y_lentgth = len(list_lines)
x_lentgth = len(list_lines[0])
x_index = 0
y_index = 0

print(int(list_lines[0][1] == "#"))
print(int(list_lines[0][0] == "#"))

method1_trees = 0
# Method 1
# while y_index < y_lentgth - 1:

#     x_index = (x_index + 3) % (x_lentgth)
#     y_index += 1
#     method1_trees += int(list_lines[y_index][x_index] == "#")


# print("Method 1", method1_trees)


def try_slop(x_step, y_step):
    x_index = 0
    y_index = 0

    score = 0
    while y_index < y_lentgth - 1:
        x_index = (x_index + x_step) % (x_lentgth)
        y_index += y_step
        score += int(list_lines[y_index][x_index] == "#")

    return score


print(
    try_slop(1, 1) * try_slop(3, 1) * try_slop(5, 1) * try_slop(7, 1) * try_slop(1, 2)
)
