import inspect

from src.env import Env
from src.config import Config
from src.login import Login

def test_login(env_session: Env, config_session: Config):
    
    current_frame = inspect.currentframe()
    if current_frame is None:
        raise RuntimeError("Failed to get current frame")
    function_name = current_frame.f_code.co_name
    print(f'{function_name} test called')
    
    url: str = env_session.get('FUNCTESTS_BASE_URL')+config_session.get('pages', 'login')
    session = Login(url, env_session.get('FUNCTESTS_USERNAME'), env_session.get('FUNCTESTS_PASSWORD')).login()
    
    response = session.get(env_session.get('FUNCTESTS_BASE_URL'))
    #print(response.status_code)
    #print(response.url)
    #print(response.text)

    assert response.status_code == 200
    assert response.url == env_session.get('FUNCTESTS_BASE_URL')
