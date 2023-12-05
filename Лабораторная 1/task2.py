# TODO Найдите количество книг, которое можно разместить на дискете

information_volume_of_disk_Mb = 1.44
number_of_pages = 100
number_of_lines = 50
number_of_characters = 25
volume_one_characters_b = 4

information_volume_of_disk_b = information_volume_of_disk_Mb * 1024 * 1024
number_of_characters_in_book = number_of_pages * number_of_lines * number_of_characters
book_size_b = number_of_characters_in_book * volume_one_characters_b

print("Количество книг, помещающихся на дискету:", int(information_volume_of_disk_b / book_size_b))
