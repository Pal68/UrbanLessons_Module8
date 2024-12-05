def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for i in range(0, len(numbers)):
        try:
            result = result + numbers[i]
        except TypeError as exc:
            print(f"Некорректый тип данных для подсчёта суммы - {numbers[i]}")
            incorrect_data = incorrect_data + 1
    return(result, incorrect_data)

def calculate_average(numbers):
    result_mean = 0
    try:
        sum_numbers, incorrect_data = personal_sum(numbers)
        result_mean = sum_numbers/(len(numbers) -incorrect_data)
    except ZeroDivisionError:
        result_mean = 0
    except TypeError:
        result_mean = None
        print('В numbers записан некорректный тип данных')
    return result_mean

# тесты
print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать