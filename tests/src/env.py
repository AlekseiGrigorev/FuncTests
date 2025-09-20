import os

from dotenv import load_dotenv
class Env:

    def __init__(self) -> None:
        load_dotenv()
    
    def get(self, key: str, default: str ='')-> str:
        return str(os.getenv(key, default))