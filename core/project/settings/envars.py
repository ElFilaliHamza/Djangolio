from core.general.utils.collections import deep_update
from core.general.utils.settings import get_settings_from_environement
"""
This file is used to load the settings from the environment and make it global on our project.
so that our project can use .

example:

export CORESETTINGS_IN_DOCKER = True (environment variable)

Could then referenced as a global variable in our project as :
IN_DOCKER (Where the value would be true)
"""

# globals() is a dictionary that contains all the global variables in the current scope
# this type ignore is because we are using a dictionary that is not exist on this
# file or even imported but it will be imported using django-split-settings.
# isort: skip_file

deep_update(globals(), get_settings_from_environement(ENV_VAR_SETTINGS_PREFIX))  # type: ignore # noqa: F821
