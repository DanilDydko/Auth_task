from random import randint
from authenticator import Authenticator
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
    while True:
        authenticator = Authenticator()
        user_login = input("Enter your login:")
        user_password = int(input("Enter your password:"))
        if user_login == new_login and user_password == new_password:
            authenticator.authorize(user_login, user_password)
        else:
            authenticator.registrate()
        break


    guess_number_game()
