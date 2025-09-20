import pytest

from src.env import Env
from src.config import Config
from src.login import Login

env = Env()
config = Config('config.ini')

@pytest.fixture(scope="session")
def env_session()-> Env: 
    return env

@pytest.fixture(scope="session")
def config_session()-> Config: 
    return config

@pytest.fixture(scope="session")
def auth_session():
    url: str = env.get('BASE_URL')+config.get('pages', 'login')
    print(url)
    session = Login(url, env.get('USERNAME'), env.get('PASSWORD')).login()
    return session
