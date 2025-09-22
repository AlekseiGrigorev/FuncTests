import inspect
import requests

from src.env import Env
from src.config import Config

def test_init(env_session: Env, config_session: Config, auth_session: requests.Session):
    """
    Test the initialization endpoint of the website.

    This test sends a GET request to the initialization endpoint with the X-Requested-With
    header set to "XMLHttpRequest". It then checks that the response status code
    is 200 and that the JSON response contains a valid client ID.

    Parameters
    ----------
    env_session : Env
        The Env instance to use for retrieving environment variables.
    config_session : Config
        The Config instance to use for retrieving configuration values.
    auth_session : requests.Session
        The requests Session instance to use for sending requests to the website.

    Returns
    -------
    None
    """
    current_frame = inspect.currentframe()
    if current_frame is None:
        raise RuntimeError("Failed to get current frame")
    function_name = current_frame.f_code.co_name
    print(f'{function_name} test called')

    headers = auth_session.headers
    headers["X-Requested-With"]="XMLHttpRequest"
    url: str = env_session.get('FUNCTESTS_BASE_URL')+config_session.get('endpoints', 'init')
    print("Endpoint: "+url)
    response: requests.Response = auth_session.get(url, headers=headers)
    print("Endpoint status: " + str(response.status_code))
    
    assert response.status_code == 200
    response_json = response.json()
    assert response_json['modules']['smartis']['client']['id'] > 0

    