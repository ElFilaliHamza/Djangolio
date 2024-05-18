# This is a settings file depend on each dev that working on this project

SECRET_KEY = 'django-insecure-ny-0mc4dy-fst#^de-e8d3tlqs30g_1_ew@tsz^)=1s-d^hl4t'
DEBUG = True

LOGGING['formatters']['colored'] = {  # type: ignore
    '()': 'colorlog.ColoredFormatter',
    'format': '%(log_color)s%(asctime)s %(levelname)s %(name)s %(bold_white)s%(message)s',
}
LOGGING['loggers']['core']['level'] = 'DEBUG'  # type: ignore
LOGGING['handlers']['console']['level'] = 'DEBUG'  # type: ignore
LOGGING['handlers']['console']['formatter'] = 'colored'  # type: ignore
