# Напишите однострочный генератор словаря:
# * который принимает на вход три списка одинаковой длины:<br>
# (имена str, ставка int, премия str с указанием процентов вида «10.25%».)
# * В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# * Сумма рассчитывается как ставка умноженная на процент премии

names = ['Garry', 'Fiona', 'Bob']
bets = [31_000, 14_000, 56_000]
prizes = ['13%', '22.5%', '100%']

def dict_summ_prize_and_bet(list_name, list_bet, list_prize):
    dict_func = {}
    for name_key, bet, prize in zip(list_name, list_bet, list_prize):
        dict_func[name_key] = bet + ((bet / 100) * (float(prize.replace("%",""))))
    return dict_func
    print(dict_func)

print(dict_summ_prize_and_bet(names,bets,prizes))

dict_generator = {name_key: bet + ((bet / 100) * (float(prize.replace("%","")))) for name_key, bet, prize in zip(names, bets, prizes)}
for key, values in dict_generator.items():
    print(f"Имя сотрудника: {key} \t зарплата сотрудника с учётом премии: {values} ")