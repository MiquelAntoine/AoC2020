file = open(r"C:\Users\Antoine\Desktop\AoC\AoC2020\data\day07.txt", mode="r")

data = file.read()
list_rules = data.split(".\n")

def process_rule(dict_content, dict_containers, rule):
    split_ = rule.split(" contain ")
    container = split_[0]
    container_word = container.split(" ")
    container_type = container_word[0] + " " + container_word[1]

    if not container_type in dict_containers.keys():
        dict_containers[container_type] = []
    all_contents = split_[1]
    split_contents = all_contents.split(",")

    for content in split_contents:

        content_words = content.split(" ")

        if content_words[0] == "":
            content_words = content_words[1:]
        content_nb = content_words[0]
        content_type = content_words[1] + " " + content_words[2]

        if content_type in dict_content.keys():
            dict_content[content_type].append(container_type)
        else:
            dict_content[content_type] = [container_type]

        # We should not need a if not in otherwise it would be infinite
        dict_containers[container_type].append((content_nb, content_type))


dict_contents = {}
dict_containers = {}
for rule in list_rules:
    process_rule(dict_contents, dict_containers, rule)

# Question 1
# Now we have to search back all the containers possible
start_set = set()
new_color = dict_contents["shiny gold"].copy()
while new_color != []:
    test_color = new_color.pop()
    start_set.add(test_color)
    if test_color in dict_contents.keys():
        containers_of_test_color = dict_contents[test_color]
        for containers in containers_of_test_color:
            if not containers in start_set:
                new_color.append(containers)


print(len(start_set))


# Question2
def compute_nb_bags(tuple):
    global dict_containers
    name = tuple[1]
    children = dict_containers[name]

    sum_ = 0
    for child in children:
        if child[0] != "no":
            sum_ += int(child[0]) * compute_nb_bags(child) + int(child[0])

    return sum_


print(compute_nb_bags((1, "shiny gold")))
