import sys
import os
import pytest
import requests
from dotenv import load_dotenv
import configparser

from src.login import Login

load_dotenv()
# load_dotenv(dotenv_path="../.env")
base_url = os.getenv('BASE_URL')
print(base_url)

config = configparser.ConfigParser()
config.read('config.ini')  # Чтение файла

@pytest.fixture(scope="session")
def auth_session():
    session = Login(base_url+config.get('pages', 'login'), os.getenv('USERNAME'), os.getenv('PASSWORD')).login()
    return session