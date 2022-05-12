from typing import Optional
from random import randint


def validate_name(name: str) -> None:
    """ Ф-ция, проверяющая кооректность введенного имени

    Проверяет имя на пустоту, минимальное кол-во символов, а также кол-во пробелов (не больше одного)
    """
    if not name:
        raise Exception("Ошибка: пустое имя")
    elif len(name) < 3:
        raise Exception("Ошибка: имя должно включать минимум 3 символа")
    elif name.count(" ") > 1:
        raise Exception("Ошибка: имя может содержать лишь один пробел")

    return


def validate_age(age: int) -> None:
    """Ф-ция, проверяющая корректность введенного возраста

    Проверяет возраст на ноль и отрицвательное число, а также минимальный возраст (<14)
    """
    if age <= 0:
        raise Exception("Ошибка: возраст не может быть равен нулю или отрицательному числу")
    elif age < 14:
        raise Exception("Ошибка: минимальный возраст - 14 лет")

    return


def get_passport_advice(age: int) -> Optional[str]:
    """Ф-ция, дающая подсказку по замене или получению паспорта

    Проверяет возраст и согласно значению выдает подсказку (16-17 лет, 25-26 лет, 45-46 лет)
    """
    if 16 <= age <= 17:
        return "Привет, не забудь получить первый паспорт"
    elif 25 <= age <= 26:
        return "Привет, не забудь заменить первый паспорт"
    elif 45 <= age <= 46:
        return "Привет, не забудь во второй раз заменить паспорт"

    return


def clear_whitespaces(value: str) -> str:
    """Ф-ция, убирающая пробелы в начале и конце строки

    Принимает строку и с помощью метода strip() убирает пробелы в начале и конце строки
    """
    return value.strip(" ")


def guess_number_game():
    """Ф-ция, предлагающая сыграть в угадайку

    Вызывается в случае, если пользователь ввел корректные данные
    """
    random_number = randint(1, 5)
    attempt = 0
    while True:
        number = input("Введите ваше число:")
        try:
            number = int(number)
        except ValueError as e:
            print(f"Я словил ошибку: {e}")
        if random_number == number:
            print("Браво, ты угадал число")
            print(f"Ты использовал {attempt + 1} попытки")
            break
        else:
            print(f"Пока мимо, попробуй еще раз")
            attempt += 1


def main():
    second_attempt = 0
    while True:
        name = input("Введите ваше имя:")
        age = input("Введите ваш возраст:")
        print(f"Это твоя попытка под номером: {second_attempt + 1}")


        name = clear_whitespaces(name)
        age = clear_whitespaces(age)

        try:
            age = int(age)
        except ValueError as e:
            print(f"Я словил ошибку: {e}")
            second_attempt += 1
            continue

        try:
            validate_name(name)
            validate_age(age)
        except Exception as e:
            print(f"Я словил ошибку: {e}")
            second_attempt += 1
            continue

        break

    advice = get_passport_advice(age)

    if not advice:
        advice = ""

    text_welcome = f"Привет, {name.title()}, твой возраст {age}.{advice}"
    print(text_welcome)

    guess_number_game()


main()