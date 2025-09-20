import configparser
import os
from typing import Iterable, Union


class Config:
    StrOrBytesPath = Union[str, bytes, os.PathLike[str]]
    
    def __init__(self, filenames: StrOrBytesPath |Iterable[StrOrBytesPath], encoding: str | None = None):
        self.config = configparser.ConfigParser()
        self.config.read(filenames)

    def get(self, section: str, key: str) -> str:
        return self.config.get(section, key)
