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

    def __init__(self) -> None:
        """
        Initialize the Env object.

        This method loads environment variables from the .env file in the project root.

        Returns
        -------
        None
        """
        load_dotenv()
    
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