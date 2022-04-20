from random import randint
from authenticator import Authenticator
from exceptions import AuthorizationError, RegistartionError

def infinity(func):
    def wrap():
        while True:
            if func():
                break
    return wrap



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


authenticator = Authenticator()

@infinity
def main():
    if authenticator.login:
        print("Чтобы авторизоваться, введите ваш логин и пароль")
    else:
        print("Чтобы зарегистрироваться, введите ваш логин и пароль")

    username = input("Введите логин:")
    password = input("Введите пароль:")

    if authenticator.login:
        try:
            authenticator.authorize(username, password)
        except AuthorizationError as e:
            print(f"Error: {e}")
            return False
    else:
        try:
            authenticator.registrate(username, password)
        except RegistartionError as e:
            print(f"Error: {e}")
            return False

        print("Вы прошли регистрацию")
        return True

    success_login_time = authenticator.last_success_login_at.strftime('%d.%m.%Y %H:%M:%S')

    print(f"Привет, {authenticator.login}")
    print(f"Время последней попытки: {success_login_time}")
    print(f"Кол-во попыток: {authenticator.errors_count}")

    guess_number_game()
    return True

if __name__ == '__main__':
    main()


