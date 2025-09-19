import os

def test_login(auth_session):
    print(auth_session.cookies)
    # assert auth_session.status_code == 200

def test_logout(auth_session):
    auth_session.post(base_url+config.get('pages', 'logout'))
    print(auth_session.cookies)
    # assert auth_session.status_code == 200
