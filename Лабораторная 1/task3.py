list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
number_of_players = len(list_players)
number_of_players_in_team = number_of_players // 2
the_first_team = list_players[:number_of_players_in_team]
the_second_team = list_players[number_of_players_in_team:]

print(the_first_team)
print(the_second_team)