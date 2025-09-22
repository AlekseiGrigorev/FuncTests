import os

from dotenv import load_dotenv

class Env:
    """
    A class to handle environment variables.

    This class provides methods to load environment variables from a .env file
    and retrieve their values with optional default fallbacks.

    Attributes
    ----------
    None
    """

    def __init__(self, override: bool = False) -> None:
        """
        Initialize the Env object.

        This method loads environment variables from the .env file in the project root.

        Returns
        -------
        None
        """
        load_dotenv(override=override)
    
    def get(self, key: str, default: str ='')-> str:
        """
        Get an environment variable by its key.

        Parameters
        ----------
        key : str
            The key of the environment variable to get.
        default : str, optional
            The default value to return if the environment variable is not set.

        Returns
        -------
        str
            The value of the environment variable or the default value if not set.
        """
        return str(os.getenv(key, default))
    
    def get_int(self, key: str, default: int =0)-> int:
        """
        Get an environment variable by its key as an integer.

        Parameters
        ----------
        key : str
            The key of the environment variable to get.
        default : int, optional
            The default value to return if the environment variable is not set.

        Returns
        -------
        int
            The value of the environment variable as an integer or the default value if not set.
        """
        return int(os.getenv(key, default))
    
    def get_float(self, key: str, default: float =0.0)-> float:
        """
        Get an environment variable by its key as a float.

        Parameters
        ----------
        key : str
            The key of the environment variable to get.
        default : float, optional
            The default value to return if the environment variable is not set.

        Returns
        -------
        float
            The value of the environment variable as a float or the default value if not set.
        """
        return float(os.getenv(key, default))
    
    def get_bool(self, key: str, default: bool =False)-> bool:
        """
        Get an environment variable by its key as a boolean.

        Parameters
        ----------
        key : str
            The key of the environment variable to get.
        default : bool, optional
            The default value to return if the environment variable is not set.

        Returns
        -------
        bool
            The value of the environment variable as a boolean or the default value if not set.
        """
        bool_str = str(os.getenv(key, default))
        return bool(bool_str.lower() in ("true", "1", "yes", "on"))