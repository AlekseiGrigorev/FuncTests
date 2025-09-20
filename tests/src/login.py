from typing import cast
import requests
from bs4 import BeautifulSoup, element

class Login:
# login using the login form

    def __init__(self, login_url: str, username: str, password: str):
        self.login_url = login_url
        self.username = username
        self.password = password    

    def login(self) -> requests.Session:
        session = requests.Session()

        # Get the form with the token
        response = session.get(self.login_url)
        
        # Find the token in <input> with name csrf_token (example)
        soup = BeautifulSoup(response.text, 'html.parser')
        token_element = soup.find('input', {'name': '_token'})
        if token_element is not None:
            token_tag = cast(element.Tag, token_element)  # Cast to Tag for better typing
            val = token_tag.get('value', '')  # val can be str, _AttributeValue, or None
            csrf_token: str = str(val) if val is not None else ''
        else:
            csrf_token = ''
        
        # Login form data including the token
        payload: dict[str, str] = {
            'login': self.username,
            'password': self.password,
            '_token': csrf_token,
        }

        # Send POST request with form and token
        login_response = session.post(self.login_url, data=payload)

        # Check success
        print()
        print(f'Login status: {login_response.status_code}')

        assert login_response.status_code == 200        
        
        return session
    