def find_common_participants(string_1, string_2, symbol=','):
    set_1 = set(string_1.split(symbol))
    set_2 = set(string_2.split(symbol))
    res = set_1.intersection(set_2)
    res = list(res)
    res.sort()
    return res


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
symbol = '|'

print(find_common_participants(participants_first_group, participants_second_group, symbol))
