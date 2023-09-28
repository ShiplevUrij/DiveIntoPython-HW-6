# Создайте функцию генератор чисел Фибоначчи (см. Википедию).

# Простая функция
def number_fibonacci():
    count_number_fibanache = int(input("Введите количечтво чисел фибаначе: ")) - 2
    count = 0
    list_fibanache = [0, 1]

    while count < count_number_fibanache:
        next_number = (list_fibanache[len(list_fibanache)-1]) + (list_fibanache[len(list_fibanache) - 2])
        list_fibanache.append(next_number)
        count += 1
    return list_fibanache

print(number_fibonacci())

# Функция генератор
def generator_number_fibonacci(count_number_fibanache):
    if count_number_fibanache <= 2:
        print("Аргумент должен быть больше двух!")
        return
    count = 2
    list_fibanache = []
    if len(list_fibanache) == 0:
        list_fibanache.append(0)
        yield list_fibanache[0]
    if len(list_fibanache) == 1:
        list_fibanache.append(1)
        yield list_fibanache[1]
    while count < count_number_fibanache:
        next_number = (list_fibanache[len(list_fibanache)-1]) + (list_fibanache[len(list_fibanache) - 2])
        yield next_number
        list_fibanache.append(next_number)
        count += 1

for i in generator_number_fibonacci(10):
    print(i)

# Пример с интернета, увидел что много напихал лишних действий

def num_fib(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

for i in num_fib(10):
    print(i)