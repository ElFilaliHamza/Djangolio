# flake8: noqa

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {  # how do we want to formate the text output of a log record .
        'standard': {
            'format': '%(asctime)s %(levelname)s %(name)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
            'filters': [],
        },
    },
    'loggers': {
        logger_name: {
            'level': 'WARNING',
            'propagate': True,
        } for logger_name in
        ('django', 'django.request', 'django.db.backends', 'django.template', 'core', 'urllib3', 'asyncio')
    },
    'root': {  # all the logs that are not handled by a logger will be handled by the root logger
        'level': 'DEBUG',
        'handlers': ['console'],
    }
}

# How to log ?
# # first we need to create the python builtin logger
# logger = logging.getLogger('django')

# logger = logging.getLogger(__name__)  # this is the same as above but uses the current model name

# # then we need to add a handler to the logger
# logger.addHandler(logging.StreamHandler())
# # then we need to set the level of the logger
# logger.setLevel(logging.DEBUG)
