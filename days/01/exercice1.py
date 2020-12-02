file = open(r"C:\Users\Antoine\Desktop\AoC\AoC2020\data\day01.txt", mode="r")

data = file.read()
list_str = data.split("\n")
list_numbers = []

for number_str in list_str:
    list_numbers.append(int(number_str))

# Part One
for i in range(len(list_numbers)):
    for j in range(i+1, len(list_numbers)):
        if list_numbers[i] + list_numbers[j] == 2020:
            print(list_numbers[i]*list_numbers[j])

# Part two 
for i in range(len(list_numbers)):
    for j in range(i+1, len(list_numbers)):
        for k in range(j+1, len(list_numbers)):
            if list_numbers[i] + list_numbers[j] + list_numbers[k] == 2020:
                print(list_numbers[i]*list_numbers[j]*list_numbers[k])