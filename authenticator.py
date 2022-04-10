from typing import Optional
from datetime import datetime
from exceptions import AuthorizationError
from exceptions import RegistartionError
import os
class Authenticator():
    def __init__(self, login: Optional[str] = None, password: Optional[int] = None,
                 last_success_login_at: Optional[datetime] = None, errors_count: int = 0):
        self.login = login
        self.password = password
        self.last_success_login_at = last_success_login_at
        self.errors_count = errors_count
        self._is_auth_file_exist()

    def _is_auth_file_exist(self) -> bool:
        """Метод проверки наличия файла Auth.txt
        """
        if os.path.exists("D:\PYTHON\Authorization\Auth.txt"):
            return True
        else:
            return False

    def _read_auth_file(self):
        """Метод чтения данных из файла Auth.txt
        """
        with open("Auth.txt", "r") as f:
            self.login = f.readline()
            self.password = f.readline()
            # self.last_success_login_at = f.readline()
            # self.errors_count = f.readline()

    def _update_auth_file(self):
        """Метод перезаписи файла Auth.txt
        """
        with open("Auth.txt", "w") as f:
            f.write(self.errors_count.__str__())

    def authorize(self, new_login, new_password):
        """Метод проверки логина и пароля. Принимает аргументы строки логина и пароля.
        Сравнивает логин и пароль из аргументов с логином и паролем из файла.
        """
        self.new_login = new_login
        self.new_password = new_password
        self.errors_count = 0
        self._read_auth_file()
        if self.login.strip() == new_login and self.password.strip() == new_password:
            print("You authorized")
            return
        elif self.login.strip() is None:
            raise AuthorizationError

        self.errors_count += 1
        raise AuthorizationError

    def registrate(self, registrate_login: str, registrate_password: str):
        """Регистрация пользователя. Принимает аргументы строки логина и пароля. Делает проверку, что файла рядом auth.txt нет.
        Если он есть, вызывает исключение RegistrationError
        """
        self.registrate_login = registrate_login
        self.registrate_password = registrate_password
        if os.path.exists("D:\PYTHON\Authorization\Auth.txt"):
            raise RegistartionError
        with open("Auth.txt", "w") as f:
            f.write(self.registrate_login)
            f.write(self.registrate_password)
            f.write(self._update_auth_file())
            if self.registrate_login is None:
                raise RegistartionError
















