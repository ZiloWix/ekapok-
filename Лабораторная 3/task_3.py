def count_letters(text):

    split_text = text.split()
    string_text = ''.join(split_text)
    dict_letters = {}
    for item in string_text:
        if item.isalpha():
            if dict_letters.get(item) == None:
                dict_letters[item] = 1
            else:
                dict_letters[item] += 1

    return dict_letters


def calculate_frequency(dict_letters):
    total_count_letters = sum(dict_letters.values())
    for key in dict_letters:
        dict_letters[key] = round(dict_letters.get(key) / total_count_letters, 2)
    return dict_letters


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""
main_str = main_str.lower()
dict_letters = count_letters(main_str)
dict_letters = calculate_frequency(dict_letters)
for key in dict_letters:
    print(f"{key}: {dict_letters.get(key):.2f}")
