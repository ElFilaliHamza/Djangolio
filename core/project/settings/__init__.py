import os.path
from pathlib import Path

from split_settings.tools import include, optional

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

# Namespacing our own custom environment variables

ENV_VAR_SETTINGS_PREFIX = 'CORESETTINGS_'

# This is an additional path to look for settings files that are local on the developper settings
# that he may use if he needs to test something without touching the main dev settings file local/settings.dev.py .
LOCAL_SETTINGS_PATH = os.getenv(ENV_VAR_SETTINGS_PREFIX + 'LOCAL_SETTINGS_PATH', None)

if not LOCAL_SETTINGS_PATH:
    LOCAL_SETTINGS_PATH = 'local/settings.dev.py'

if not os.path.isabs(LOCAL_SETTINGS_PATH):
    LOCAL_SETTINGS_PATH = str(BASE_DIR / LOCAL_SETTINGS_PATH)

# This function from django-split-settings is gonna agregate different settings files into one.
include(
    'base.py',
    'logging.py',
    'custom.py',
    optional(LOCAL_SETTINGS_PATH),
    'envars.py',  # look for the system environment variables and convert them to settings variables for our project.
    'docker.py',
)
