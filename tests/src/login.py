import requests
from bs4 import BeautifulSoup

class Login:
# логин с использованием формы входа

    def __init__(self, login_url, username, password):
        self.login_url = login_url
        self.username = username
        self.password = password    

    def login(self) -> requests.Session:
        session = requests.Session()

        # Получаем форму с токеном
        response = session.get(self.login_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Ищем токен в <input> с именем csrf_token (пример)
        csrf_token = soup.find('input', {'name': '_token'})['value']

        # Данные формы для логина, включая токен
        payload = {
            'login': self.username,
            'password': self.password,
            '_token': csrf_token,
        }

        # Отправляем POST-запрос с формой и токеном
        login_response = session.post(self.login_url, data=payload)

        # Проверяем успешность
        print()
        print(f'Login status: {login_response.status_code}')

        assert login_response.status_code == 200        
        
        return session
    