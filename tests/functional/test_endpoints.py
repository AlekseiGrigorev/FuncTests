import requests

from src.env import Env
from src.config import Config

def test_init(env_session: Env, config_session: Config, auth_session: requests.Session):
    headers = auth_session.headers
    headers["X-Requested-With"]="XMLHttpRequest"
    url: str = env_session.get('BASE_URL')+config_session.get('endpoints', 'init')
    print(url)
    response: requests.Response = auth_session.get(url, headers=headers)
    assert response.status_code == 200
    response_json = response.json()
    assert response_json['modules']['smartis']['client']['id'] > 0

    