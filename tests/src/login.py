import time
from typing import cast
import requests
from bs4 import BeautifulSoup, element

class Login:
    """A class to handle website login operations.

    This class provides methods to log in to a website using a login form,
    handling CSRF tokens and maintaining session state.

    Attributes:
        login_url (str): The URL of the login form.
        username (str): The username to use for the login.
        password (str): The password to use for the login.
    """

    def __init__(self, login_url: str, username: str, password: str):
        """
        Initialize the Login object.

        Parameters
        ----------
        login_url : str
            The URL of the login form.
        username : str
            The username to use for the login.
        password : str
            The password to use for the login.
        """
        
        self.login_url = login_url
        self.username = username
        self.password = password    

    def login(self) -> requests.Session:
        """
        Log in to the website using the login form.

        This method sends a GET request to the login form URL to retrieve the form with the CSRF token.
        It then extracts the token from the HTML form and sends a POST request to the same URL with the form data and the token.
        The method returns a requests.Session instance with the authentication cookies set.

        Returns
        -------
        requests.Session
            A requests Session instance with the authentication cookies set.
        """
        
        session = requests.Session()

        # Get the form with the token
        response = session.get(self.login_url)
        time.sleep(1)
        
        # Find the token in <input> with name csrf_token (example)
        soup = BeautifulSoup(response.text, 'html.parser')
        token_element = soup.find('input', {'name': '_token'})
        if token_element is not None:
            token_tag = cast(element.Tag, token_element)  # Cast to Tag for better typing
            val = token_tag.get('value', '')  # val can be str, _AttributeValue, or None
            csrf_token: str = str(val) if val is not None else ''
        else:
            csrf_token = ''
        print(f'csrf_token: {csrf_token}')
        
        # Login form data including the token
        payload: dict[str, str] = {
            'login': self.username,
            'password': self.password,
            '_token': csrf_token,
        }

        headers = session.headers
        headers["X-Requested-With"]="XMLHttpRequest"
        # Send POST request with form and token
        login_response = session.post(self.login_url, data=payload, headers=headers, allow_redirects=True)

        print(f'Login status: {login_response.status_code}')
        print(f'Redirect URL: {login_response.url}')
        
        # Check success
        assert login_response.status_code == 200
        
        return session
    