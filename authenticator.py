from typing import Optional
from datetime import datetime
from exceptions import AuthorizationError
from exceptions import RegistartionError
import json
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
        if os.path.exists("Auth.txt"):
            return True
        else:
            return False

    def _read_auth_file(self):
        """Метод чтения данных из файла Auth.txt
        """
        with open("Auth.txt", "r") as f:
            self.parsed_data = json.loads(self.data)
            self.parsed_data['last_success_login_at'] = datetime.fromisoformat(self.parsed_data['last_success_login_at'])
            f.readline(self.parsed_data)
            # self.login = f.readline().strip()
            # self.password = f.readline().strip()
            # self.last_success_login_at = datetime.fromisoformat(f.readline().strip())
            # self.errors_count = (f.readline().strip())

    def _update_auth_file(self):
        """Метод перезаписи файла Auth.txt
        """
        with open("Auth.txt", "w") as f:
            self.data_dict = {"login": 'danil',
            "password": 'danil12',
            'last_success_login_at': datetime.utcnow().isoformat()}
            self.data = json.dumps(self.data_dict)
            f.write(self.data)




    def authorize(self, login, password):
        """Метод проверки логина и пароля. Принимает аргументы строки логина и пароля.
        Сравнивает логин и пароль из аргументов с логином и паролем из файла.
        """
        if not self.login:
            self.errors_count += 1
            raise AuthorizationError("Not registrated")
        if not login:
            self.errors_count += 1
            raise AuthorizationError("Логин не может быть пустым")
        if login == self.login and password == self.password:
            self._update_auth_file()
        else:
            self.errors_count += 1
            raise AuthorizationError("Пароль или логин некорректны")

    def registrate(self, login, password):
        """Регистрация пользователя. Принимает аргументы строки логина и пароля. Делает проверку, что файла рядом auth.txt нет.
        Если он есть, вызывает исключение RegistrationError
        """
        if self.login:
            self.errors_count += 1
            raise RegistartionError("Вы уже зарегистрированы")
        if not login:
            self.errors_count += 1
            raise RegistartionError("Логин не должен быть пустым")

        self.login = login
        self.password = password
        self._update_auth_file()
















