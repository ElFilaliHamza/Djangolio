import yaml


def yaml_coerce(value):
    """This function converts a string value into propre python
        It could convert for example a dictionnary string
        {'name': hamza, 'id': 123}
        into a python dictionnary
        {'name': 'hamza', 'id': 123}
        usefull because sometimes we need to stringfy settings
        this way like in the settings.yaml file or like in
        docker-compose.yml file
    """

    if isinstance(value, str):
        return yaml.load(f'dummy: {value}', Loader=yaml.SafeLoader)['dummy']
    else:
        return value
