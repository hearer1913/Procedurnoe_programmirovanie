
def find_common_participants(first_group, second_group, razdelitel=','):
     first_group = set(first_group.split(razdelitel))
     second_group = set(second_group.split(razdelitel))
     common = list(first_group.intersection(second_group))
     common.sort()
     return common

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"


result = find_common_participants(participants_first_group,participants_second_group)
print(result)

