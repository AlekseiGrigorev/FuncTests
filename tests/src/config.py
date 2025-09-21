import configparser
import os
from typing import Iterable, Union


class Config:
    """A class to handle configuration files using configparser.

    This class provides methods to read configuration files and retrieve values
    from specific sections and keys. It supports reading multiple configuration
    files and provides type hints for better code clarity.

    Attributes:
        config (configparser.ConfigParser): The ConfigParser instance used to parse and store configuration data.
    """
    StrOrBytesPath = Union[str, bytes, os.PathLike[str]]
    
    def __init__(self, filenames: StrOrBytesPath |Iterable[StrOrBytesPath], encoding: str | None = None):
        """
        Initialize the Config object.

        Parameters
        ----------
        filenames : StrOrBytesPath | Iterable[StrOrBytesPath]
            A single path or an iterable of paths to configuration files.
        encoding : str | None, optional
            The encoding to use when reading the configuration files. If None, the default encoding is used.

        Returns
        -------
        None

        Notes
        -----
        The configuration files are read using the configparser.ConfigParser.read() method.
        """
        
        self.config = configparser.ConfigParser()
        self.config.read(filenames)

    def get(self, section: str, key: str) -> str:
        """
        Get a value from the configuration.

        Parameters
        ----------
        section : str
            The section of the configuration file to read from.
        key : str
            The key of the value to read from the section.

        Returns
        -------
        str
            The value associated with the key in the section.

        Raises
        ------
        KeyError
            If the section or key does not exist in the configuration file.
        """
        return self.config.get(section, key)
