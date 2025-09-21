import inspect
import os
import pytest

from src.env import Env
from src.config import Config
from src.login import Login

env = Env()

if not env.get('BASE_URL'):
    raise ValueError("BASE_URL environment variable is not set")
print('.env file loaded. BASE_URL: ' + env.get('BASE_URL'))

config_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'config.ini')
if not os.path.exists(config_path):
    raise FileNotFoundError(f"Config file not found at {config_path}")
config = Config(config_path)
print('Config file loaded: ' + config_path)

@pytest.fixture(scope="session")
def env_session()-> Env: 
    """
    Return an instance of Env for use in tests.

    This fixture is session-scoped, meaning it will be called once per test session and the result will be cached and reused for all tests in the session.

    Returns
    -------
    Env
        An instance of Env.
    """
    current_frame = inspect.currentframe()
    if current_frame is None:
        raise RuntimeError("Failed to get current frame")
    function_name = current_frame.f_code.co_name
    print(f'{function_name} fixture called')
    return env

@pytest.fixture(scope="session")
def config_session()-> Config: 
    """
    Return an instance of Config for use in tests.

    This fixture is session-scoped, meaning it will be called once per test session and the result will be cached and reused for all tests in the session.

    Returns
    -------
    Config
        An instance of Config.
    """
    current_frame = inspect.currentframe()
    if current_frame is None:
        raise RuntimeError("Failed to get current frame")
    function_name = current_frame.f_code.co_name
    print(f'{function_name} fixture called')
    return config

@pytest.fixture(scope="session")
def auth_session():
    """
    Return a requests.Session instance with authentication cookies set.

    This fixture is session-scoped, meaning it will be called once per test session and the result will be cached and reused for all tests in the session.

    The session is created by logging in to the website using the credentials stored in the environment variables.

    Returns
    -------
    requests.Session
        A requests.Session instance with the authentication cookies set.
    """
    url: str = env.get('BASE_URL')+config.get('pages', 'login')
    print()
    print(__file__)
    print("Login page: " + url)
    session = Login(url, env.get('USERNAME'), env.get('PASSWORD')).login()
    
    current_frame = inspect.currentframe()
    if current_frame is None:
        raise RuntimeError("Failed to get current frame")
    function_name = current_frame.f_code.co_name
    print(f'{function_name} fixture called')
    return session
