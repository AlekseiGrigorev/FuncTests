import inspect
import os
import pytest
import http.client as http_client
import logging

from src.env import Env
from src.config import Config
from src.login import Login

env = Env(override=True)

if not env.get('FUNCTESTS_BASE_URL'):
    raise ValueError("FUNCTESTS_BASE_URL environment variable is not set")
print('.env file loaded. FUNCTESTS_BASE_URL: ' + env.get('FUNCTESTS_BASE_URL'))

config_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'config.ini')
if not os.path.exists(config_path):
    raise FileNotFoundError(f"Config file not found at {config_path}")
config = Config(config_path)
print('Config file loaded: ' + config_path)

@pytest.fixture(scope="session", autouse=True)
def debug_session():
    """
    A pytest fixture that sets up HTTP debugging if the FUNCTESTS_HTTP_DEBUG environment variable is set to true.

    This fixture sets the debuglevel of the http_client.HTTPConnection to 1, sets up the root logger to log at the DEBUG level, and sets up the requests logger to log at the DEBUG level and propagate the logs to the root logger.

    The fixture is session-scoped, meaning it will be called once per test session and the result will be cached and reused for all tests in the session.
    """
    if env.get_bool('FUNCTESTS_HTTP_DEBUG'):
        http_client.HTTPConnection.debuglevel = 1
        logging.basicConfig()
        logging.getLogger().setLevel(logging.DEBUG)
        requests_log = logging.getLogger("requests.packages.urllib3")
        requests_log.setLevel(logging.DEBUG)
        requests_log.propagate = True
        
    current_frame = inspect.currentframe()
    if current_frame is None:
        raise RuntimeError("Failed to get current frame")
    function_name = current_frame.f_code.co_name
    print(f'{function_name} fixture called')

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
    url: str = env.get('FUNCTESTS_BASE_URL')+config.get('pages', 'login')
    print()
    print(__file__)
    print("Login page: " + url)
    session = Login(url, env.get('FUNCTESTS_USERNAME'), env.get('FUNCTESTS_PASSWORD')).login()
    
    current_frame = inspect.currentframe()
    if current_frame is None:
        raise RuntimeError("Failed to get current frame")
    function_name = current_frame.f_code.co_name
    print(f'{function_name} fixture called')
    return session
