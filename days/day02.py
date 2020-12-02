file = open(r"C:\Users\Antoine\Desktop\AoC\AoC2020\data\day02.txt", mode="r")

data = file.read()
list_lines = data.split("\n")

score1 = 0
for line in list_lines:
    mdp = line.split(": ")[1]
    lower_bound = int(line.split(": ")[0].split(" ")[0].split("-")[0])
    upper_bound = int(line.split(": ")[0].split(" ")[0].split("-")[1])
    letter = line.split(": ")[0].split(" ")[1]

    nb_occurence = mdp.count(letter)
    if nb_occurence >= lower_bound and nb_occurence <= upper_bound:
        score1 += 1

print("score1",score1)

score2 = 0
for line in list_lines:
    mdp = line.split(": ")[1]
    index1 = int(line.split(": ")[0].split(" ")[0].split("-")[0])
    index2 = int(line.split(": ")[0].split(" ")[0].split("-")[1])
    letter = line.split(": ")[0].split(" ")[1]

    index1_is_ok = mdp[index1-1] == letter
    index2_is_ok = mdp[index2-1] == letter
    if (index1_is_ok and not index2_is_ok) or (index2_is_ok and not index1_is_ok):
        score2 += 1
        

print("score2",score2)