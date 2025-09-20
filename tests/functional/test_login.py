import requests

from src.env import Env
from src.config import Config

def test_login(env_session: Env, config_session: Config, auth_session: requests.Session):
    response: requests.Response = auth_session.post(env_session.get('BASE_URL')+config_session.get('pages', 'login'))
    assert response.status_code == 200

def test_logout(env_session: Env, config_session: Config, auth_session: requests.Session):
    response: requests.Response = (auth_session.post(env_session.get('BASE_URL')+config_session.get('pages', 'logout')))
    assert response.status_code == 200
