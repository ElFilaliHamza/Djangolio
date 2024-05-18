import os

from .misc import yaml_coerce


def get_settings_from_environement(prefix):
    """
    The function is designed to extract environment
    variables that start with a specific prefix and
    return them as a dictionary with the prefix removed
    from the keys.

    Suppose the environment variables are as follows:

    makefile :
        DB_HOST=localhost
        DB_PORT=5432
        API_KEY=abcdef
        DB_USER=admin
        EMPTY_VAR=

    And you call the function with the prefix DB_:

    python :
        settings = get_settings_from_environement('DB_')
        The resulting dictionary would be:

    python dict :
        {
            'HOST': 'localhost',
            'PORT': '5432',
            'USER': 'admin'
        }

    The variables DB_HOST, DB_PORT, and DB_USER are included in the dictionary with the prefix
    DB_ removed from their keys, and EMPTY_VAR is excluded because its value is empty.


    """

    prefix_len = len(prefix)
    return {
        key[prefix_len:]: yaml_coerce(value)  # Remove the prefix from the key
        for key, value in os.environ.items()  # Iterate over all environment variables
        if key.startswith(prefix) and value != ''  # Check if the key starts with the prefix and value is not empty
    }
