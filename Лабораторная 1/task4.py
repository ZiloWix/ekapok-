users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

site_visitors = {
    "Общее количество": 0,
    "Уникальные посещения": 0
}

site_visitors["Общее количество"] = len(users)

unique_visitors = set(users)
site_visitors["Уникальные посещения"] = len(unique_visitors)

print(site_visitors)

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
