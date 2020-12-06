file = open(r"C:\Users\Antoine\Desktop\AoC\AoC2020\data\day06.txt", mode="r")

data = file.read()
list_groups = data.split("\n\n")


def process_group_method1(raw_group):
    persons_answer = raw_group.split("\n")
    group_answers = set()
    for person_answer in persons_answer:
        for answer in person_answer:
            group_answers.add(answer)

    return group_answers


def process_group_method2(raw_group):
    persons_answer = raw_group.split("\n")
    group_answers = set()
    # We need to inialize the group_answers with the first person answers
    first_person_answer = persons_answer[0]
    for answer in first_person_answer:
        group_answers.add(answer)

    for person_answer in persons_answer:
        set_answer = set()
        for answer in person_answer:
            set_answer.add(answer)

        group_answers = group_answers.intersection(set_answer)

    return group_answers


def count_total_answer(list_groups):
    count = 0
    for group in list_groups:
        count += len(process_group_method2(group))

    return count


print(count_total_answer(list_groups))
